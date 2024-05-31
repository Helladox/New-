import requests, os, sys, re
import threading
import json, asyncio
import subprocess
import datetime
from Extractor import app
from config import SUDO_USERS
from pyrogram import filters, idle
from subprocess import getstatusoutput




api = 'https://api.classplusapp.com/v2'

headers = {
    "Host": "api.classplusapp.com",
    "x-access-token": "",
    "User-Agent": "Mobile-Android",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en",
    "Origin": "https://web.classplusapp.com",
    "Referer": "https://web.classplusapp.com/",
    "Region": "IN",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
}


 # ------------------------------------------------------------------------------------------------------------------------------- #


def get_course_content(course_id, folder_id=0):
        fetched_contents = ""

        params = {
            'courseId': course_id,
            'folderId': folder_id,
        }

        res = requests.get(f'{api}/course/content/get', headers=headers, params=params)

        if res.status_code == 200:
            res_json = res.json() 

            contents = res_json.get('data', {}).get('courseContent', [])

            for content in contents:
                if content['contentType'] == 1:
                    resources = content.get('resources', {})

                    if resources.get('videos') or resources.get('files'):
                        sub_contents = get_course_content(course_id, content['id'])
                        fetched_contents += sub_contents
                
                elif content['contentType'] == 2:
                    name = content.get('name', '')
                    id = content.get('contentHashId', '')
         
                    params = {
                        'contentId': id
                    }

                    r = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
                    url = r.json()['url']

                    content = f'{name}:{url}\n'
                    fetched_contents += content

                else:
                    name = content.get('name', '')
                    url = content.get('url', '')
                    content = f'{name}:{url}\n'
                    fetched_contents += content

        return fetched_contents



# ------------------------------------------------------------------------------------------------------------------------------- #

async def classplus_txt(app, message):   
    
    hdr = {
      "Api-Version": "43",
      "Content-Type": "application/json;charset=UTF-8",
      "Device-Id": "",
      "Origin": "https://web.classplusapp.com",
      "Referer": "https://web.classplusapp.com/",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    }
    try:
        input = await app.ask(message.chat.id, text="SEND YOUR CREDENTIALS AS SHOWN BELOW\n\nORGANISATION CODE:\n\nPHONE NUMBER:\n\nOR SEND\nACCESS TOKEN:")
        creds = input.text    
        logged_in = False

        if '\n' in creds:
            org_code, phone_no = [cred.strip() for cred in creds.split('\n')]

            if org_code.isalpha() and phone_no.isdigit() and len(phone_no) == 10:
                res = requests.get(f'{api}/orgs/{org_code}')

                if res.status_code == 200:
                    res = res.json()

                    org_id = int(res['data']['orgId'])

                    data = {
                        'countryExt': '91',
                        'mobile'    : phone_no,
                        'orgCode'   : org_code,
                        'orgId'     : org_id,
                        'viaSms'    : 1,
                    }
                            
        
                    res = requests.post(f'{api}/otp/generate', data=data, headers=headers)

                    if res.status_code == 200:
                        res = res.json()
                        session_id = res['data']['sessionId']
                        user_otp = await app.ask(message.chat.id, text="SEND YOUR OTP")

                        if user_otp.text.isdigit():
                            otp = user_otp.text.strip()

                            data = {
                                "otp": otp,
                                "countryExt": "91",
                                "sessionId": session_id,
                                "orgId": org_id,
                                "fingerprintId": "",
                                "mobile": phone_no
                            }
                            

                            res = requests.post(f'{api}/users/verify', data=data, headers=headers)
                            res = res.json()
                            if res['status'] == 'success':
                                user_id = res['data']['user']['id']
                                token = res['data']['token']
                                headers['x-access-token'] = token

                                await message.reply_text(f"Login Successfully\n\n`{token}`")                     
                                logged_in = True

                            else:
                                raise Exception('Failed to verify OTP.')  
                        raise Exception('Failed to validate OTP.')
                    raise Exception('Failed to generate OTP.')    
                raise Exception('Failed to get organization Id.')
            raise Exception('Failed to validate credentials.')

        else:

            token = creds.strip()
            headers['x-access-token'] = token


            res = requests.get(f'{api}/users/details', headers=headers)

            if res.status_code == 200:
                res = res.json()
                user_id = res['data']['responseData']['user']['id']
                logged_in = True
            
            else:
                raise Exception('Failed to get user details.')


        if logged_in:
            thread = threading.Thread(target=lambda: asyncio.run(classplus_data(message, user_id, api)))
            thread.start()

    except Exception as e:
        print(f"Error: {e}")



async def classplus_data(message, user_id, api): 
    try:
        params = {
            'userId': user_id,
            'tabCategoryId': 3
        }
        res = requests.get(f'{api}/profiles/users/data', headers=headers, params=params)
        if res.status_code == 200:
            res = res.json()
            courses = res['data']['responseData']['coursesData']

            if courses:
                text = ''
                for cnt, course in enumerate(courses):
                    name = course['name']
                    text += f'{cnt + 1}. {name}\n'

                num = await app.ask(message.chat.id, text=f"send index number of the course to download\n\n{text}")   
                if num.text.isdigit() and len(num.text) <= len(courses):
                    selected_course_index = int(num.text.strip())
                    course = courses[selected_course_index - 1]
                    selected_course_id = course['id']
                    selected_course_name = course['name']
                    msg  = await message.reply_text("Now your extracting your course")     

                    course_content = get_course_content(selected_course_id)
                    await msg.delete()

                    if course_content:
                        caption = (f"App Name : Classplus\nBatch Name : {selected_course_name}")

                        text_file = "Classplus"
                        with open(f'{text_file}.txt', 'w') as f:
                            f.write(f"{course_content}")
                         
                        await message.reply_document(document=f"{text_file}.txt", caption=caption)                                     
                        os.remove(f'{text_file}.txt')
                        
                            
                    else:
                        raise Exception('Did not found any content in course.')
                raise Exception('Failed to validate course selection.')
            raise Exception('Did not found any course.')
        raise Exception('Failed to get courses.')

    except Exception as e:
        print(f"Error: {e}")
