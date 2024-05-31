import json
import os
import requests
from pyrogram import filters
from Extractor import app



async def neon_txt(app, message):
    input1 = await app.ask(message.chat.id, text="**Send ID & Password in this manner otherwise bot will not respond.\n\nSend like this:-  ID*Password**")

    login_url = "https://neonclasses.com/testapi/register/loginWithpassword"
    raw_text = input1.text

    headers = {
    "Host": "neonclasses.com",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.9.2"
    }


    data = {
    "user_email": "",
    "user_password": "",
    }

    data["user_email"] = raw_text.split("*")[0]
    data["user_password"] = raw_text.split("*")[1]
    await input1.delete(True)

    response = requests.post(login_url, headers=headers, data=data)
    if response.status_code == 200:
        res = response.json()
        std_id = res['results']["student_id"]            
        await message.reply_text("**Login Successful**")
    else:
        await message.reply_text("Go back to response")
           
    data = {
    "student_id": std_id
    }

    url = "https://neonclasses.com/testapi/video/testing"
    response = requests.post(url, headers=headers, data=data)
    response = response.json()

    FFF = "**BATCH-ID  BATCH-NAME**\n\n"
    if 'results' in response:
        for item in response['results']: 
            bcat_id = item.get('bcat_id')
            bcat_name = item.get('bcat_name')
        
            FFF += f"{bcat_id} - {bcat_name}\n\n"
        
            if 'child' in item:
                for child_item in item['child']:
                    bcat_id = child_item.get('bcat_id')
                    bcat_name = child_item.get('bcat_name')
                    FFF += f"{bcat_id} - {bcat_name}\n\n"

    
    input2 = await app.ask(message.chat.id, text=FFF)
    raw_text2 = input2.text
    

    url = "https://neonclasses.com/testapi/video/testvideosubcategory"

    data = {
      "student_id": std_id,
      "parent_id": raw_text2
    }
    
    response = requests.post(url, headers=headers, data=data)
    response = response.json()

    lol_id = ""
    if 'results' in response:
        for item in response['results']:
            bcat_id = item.get('bcat_id')            
            lol_id += f"{bcat_id}&"
                   
            if 'child' in item:
                for child_item in item['child']:
                    bcat_id = item.get('bcat_id')
                    lol_id += f"{bcat_id}&"
                    
    await input2.delete(True)
    await message.reply_text(lol_id)
                   
                

    
    

    



  
