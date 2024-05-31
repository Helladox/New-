import requests, os, sys, re
import math
import threading
import json, asyncio
import subprocess
import datetime
from Extractor import app
from pyrogram import filters
from subprocess import getstatusoutput


async def get_otp(message, phone_no):
    url = "https://api.penpencil.co/v1/users/get-otp"
    query_params = {"smsType": "0"}

    headers = {
        "Content-Type": "application/json",
        "Client-Id": "5eb393ee95fab7468a79d189",
        "Client-Type": "WEB",
        "Client-Version": "2.6.12",
        "Integration-With": "Origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    }

    payload = {
        "username": phone_no,
        "countryCode": "+91",
        "organizationId": "5eb393ee95fab7468a79d189",
    }

    try:
        response = requests.post(url, params=query_params, headers=headers, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        await message.reply_text("**Failed to Generate OTP**")



async def get_token(message, phone_no, otp):
    url = "https://api.penpencil.co/v3/oauth/token"
    payload = {
        "username": phone_no,
        "otp": otp,
        "client_id": "system-admin",
        "client_secret": "KjPXuAVfC5xbmgreETNMaL7z",
        "grant_type": "password",
        "organizationId": "5eb393ee95fab7468a79d189",
        "latitude": 0,
        "longitude": 0
    }

    headers = {
        "Content-Type": "application/json",
        "Client-Id": "5eb393ee95fab7468a79d189",
        "Client-Type": "WEB",
        "Client-Version": "2.6.12",
        "Integration-With": "",
        "Randomid": "990963b2-aa95-4eba-9d64-56bb55fca9a9",
        "Referer": "https://www.pw.live/",
        "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }

    try:
        r = requests.post(url, json=payload, headers=headers)
        r.raise_for_status()
        resp = r.json()
        token = resp['data']['access_token']
        return token
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        await message.reply_text("**Failed to Generate Token**")


async def pw_mobile(app, message):
    lol = await app.ask(message.chat.id, text="**ENTER YOUR PW MOBILE NO. WITHOUT COUNTRY CODE.**")
    phone_no = lol.text
    await lol.delete()
    await get_otp(message, phone_no)
    lol2 = await app.ask(message.chat.id, text="**ENTER YOUR OTP SENT ON YOUR MOBILE NO.**")
    otp = lol2.text
    await lol2.delete()
    token = await get_token(message, phone_no, otp)
    await message.reply_text(F"**YOUR TOKEN** => `{token}`")
    await pw_login(app, message, token)


async def pw_token(app, message):
    lol3 = await app.ask(message.chat.id, text="**ENTER YOUR PW ACCESS TOKEN**")
    token = lol3.text
    await lol3.delete()
    await pw_login(app, message, token)


async def pw_data(message, hh, batch_slug, batch_name, headers, prog):
    try:
        uu = ""
        xv = hh.split('&')
        for y in range(0,len(xv)):
            t =xv[y]

            mm = ""            
            params = {
                'page': '1',
                'limit': '100'
            }
            try:
                response3 = requests.get(f"https://api.penpencil.co/v2/batches/{batch_slug}/subject/{t}/topics", params=params, headers=headers).json()["data"]
                for data in response3:
                    mm += f"{data['slug']}:{data['videos']}:{data['notes']}:{data['exercises']}&"

                xz = mm.split('&')
                for m in range(0, len(xz) - 1):
                    y = xz[m]
                    print(y)
                    tag, videos, notes, exercises = y.split(':')
                    p1 = {
                        "page": "1",
                        "contentType": "videos",
                        "tag": tag
                    }
                    p2 = {
                        "page": "1",
                        "contentType": "notes",
                        "tag": tag
                    }
                    p3 = {
                        "page": "1",
                        "contentType": "DppNotes",
                        "tag": tag
                    }

                    if videos != 0:
                        try:
                            r1 = requests.get(f"https://api.penpencil.co/v2/batches/{batch_slug}/subject/{t}/contents", params=p1, headers=headers).json()["data"]
                            r1.reverse()
                            for data in r1:
                                uu += f"{data['topic']} : {data['url']}\n"
                        except Exception as e:
                            print(f"Error fetching videos: {e}")

                    if notes != 0:
                        try:
                            r2 = requests.get(f"https://api.penpencil.co/v2/batches/{batch_slug}/subject/{t}/contents", params=p2, headers=headers).json()["data"]
                            r2.reverse()
                            for data in r2:
                                content1 = data.get('homeworkIds', [])
                                for item in content1:
                                    topic = item['topic']
                                    attachmentIds = item['attachmentIds']
                                    for attachment in attachmentIds:
                                        baseUrl = attachment['baseUrl']
                                        key = attachment['key']
                                        uu += f"{topic} : {baseUrl}{key}\n"
                        except Exception as e:
                            print(f"Error fetching notes: {e}")

                    if exercises != 0:
                        try:
                            r3 = requests.get(f"https://api.penpencil.co/v2/batches/{batch_slug}/subject/{t}/contents", params=p3, headers=headers).json()["data"]
                            r3.reverse()
                            for data in r3:
                                content1 = data.get('homeworkIds', [])
                                for item in content1:
                                    topic = item['topic']
                                    attachmentIds = item['attachmentIds']
                                    for attachment in attachmentIds:
                                        baseUrl = attachment['baseUrl']
                                        key = attachment['key']
                                        uu += f"{topic} : {baseUrl}{key}\n"
                        except Exception as e:
                            print(f"Error fetching exercises: {e}")

            except Exception as e:
                print(f"Error fetching topics: {e}")
 
        if '/' in batch_name:
            name1 = batch_name.replace("/", "")
        else:
            name1 = batch_name

        with open(f"{name1}.txt", 'a') as f:
            f.write(f"{uu}")

        c_txt = f"**App Name: Physics-Wallah\nBatch Name:** `{batch_name}`"
        await message.reply_document(document=f"{name1}.txt", caption=c_txt)
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")
        print(str(e))
    await prog.delete()



async def pw_login(app, message, token):
    try:
        headers = {
            'Host': 'api.penpencil.co',
            'authorization': f"Bearer {token}",
            'client-id': '5eb393ee95fab7468a79d189',
            'client-version': '12.84',
            'user-agent': 'Android',
            'randomid': 'e4307177362e86f1',
            'client-type': 'MOBILE',
            'device-meta': '{APP_VERSION:12.84,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.physicswalb}',
            'content-type': 'application/json; charset=UTF-8',
        }

        params = {
           'mode': '1',
           'filter': 'false',
           'exam': '',
           'amount': '',
           'organisationId': '5eb393ee95fab7468a79d189',
           'classes': '',
           'limit': '100',
           'page': '1',
           'programId': '',
           'ut': '1652675230446', 
        }

        response = requests.get('https://api.penpencil.co/v3/batches/my-batches', params=params, headers=headers).json()["data"]
        aa = "**BATCH ID   :   BATCH NAME**\n\n"
        for data in response:
            batch = data["name"]
            aa += f"**{batch}**   :   `{data['_id']}`\n"
        await message.reply_text(aa)

        input3 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")
        raw_text3 = input3.text
        for data in response:
            if data['_id'] == raw_text3:
                batch_slug = data['slug']

        response2 = requests.get(f'https://api.penpencil.co/v3/batches/{raw_text3}/details', headers=headers, params=params).json()        
        batch_name = response2['data']['name']          
        subjects = response2.get('data', {}).get('subjects', [])     
        bb = "**SUBJECT   :   SUBJECT ID**\n\n"
        vj = ""
        
        for subject in subjects:
            bb += f"**{subject.get('subject')}**   :   `{subject.get('subjectId')}`\n"
            vj += f"{subject.get('subjectId')}&"
        await message.reply_text(bb)

        input4 = await app.ask(message.chat.id, text=f"Now send the **Subject IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n`{vj}`")
        raw_text4 = input4.text
        xu = raw_text4.split('&')
        hh = ""
        for x in range(0,len(xu)):
            s =xu[x]
            for subject in subjects:
                if subject.get('subjectId') == s:
                    hh += f"{subject.get('slug')}&"
        print(hh)
    
        prog = await message.reply_text("**Extracting Videos Links Please Wait  📥 **")

        thread = threading.Thread(target=lambda: asyncio.run(pw_data(message, hh, batch_slug, batch_name, headers, prog)))
        thread.start()

    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")
        print(str(e))




