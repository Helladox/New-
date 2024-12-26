import os
import requests
import logging
import asyncio
from pyrogram import filters
from Extractor import app
from config import SUDO_USERS

ACCOUNT_ID = "6206459123001"
BCOV_POLICY = "BCpkADawqM1474MvKwYlMRZNBPoqkJY-UWm7zE1U769d5r5kqTjG0v8L-THXuVZtdIQJpfMPB37L_VJQxTKeNeLO2Eac_yMywEgyV9GjFDQ2LTiT4FEiHhKAUvdbx9ku6fGnQKSMB8J5uIDd"
bc_url = f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos/"
bc_hdr = {"BCOV-POLICY": BCOV_POLICY}

async def careerdl(app, message, headers, raw_text2, class_id, notes_id, prog, name):
    if '/' in name:
        name1 = name.replace("/", "")
    else:
        name1 = name
    
    try:
        num_id = class_id.split('&')
        output_text = ""

        for id_text in num_id:
            details_url = f"https://elearn.crwilladmin.com/api/v5/batch-detail/{raw_text2}?topicId={id_text}"
            response = requests.get(details_url, headers=headers)
            data = response.json()

            details_list = data.get("data", {}).get("class_list", {})
            batch_class = details_list.get("classes", [])
            batch_class.reverse()

            for data in batch_class:
                try:
                    vid_id = str(data['id'])
                    lesson_name = data['lessonName']
                    lessonExt = data['lessonExt']
                    url = f"https://elearn.crwilladmin.com/api/v5/class-detail/{vid_id}"
                    lessonUrl = requests.get(url, headers=headers).json().get('data', {}).get('class_detail', {}).get('lessonUrl', '')

                    if lessonExt == 'brightcove':
                        token_url = "https://elearn.crwilladmin.com/api/v5/livestreamToken"
                        params = {
                            "base": "web",
                            "module": "batch",
                            "type": "brightcove",
                            "vid": vid_id
                        }
                        response = requests.get(token_url, headers=headers, params=params)
                        stoken = response.json().get("data", {}).get("token", '')
                        link = f"{bc_url}{lessonUrl}/master.m3u8?bcov_auth={stoken}"
                        output_text += f"{lesson_name}: {link}\n"
                    elif lessonExt == 'youtube':
                        link = f"https://www.youtube.com/embed/{lessonUrl}"
                        output_text += f"{lesson_name}: {link}\n"
                except Exception as e:
                    logging.error(f"Error processing lesson: {e}")

            with open(f"{name1}.txt", 'a') as f:
                f.write(f"{output_text}")
    except Exception as e:
        await message.reply_text(str(e))

    try:
        n_id = notes_id.split('&')
        text = ""

        for id in n_id:
            details_url = f"https://elearn.crwilladmin.com/api/v5/batch-notes/{raw_text2}?topicId={id}"
            response = requests.get(details_url, headers=headers)
            notes_data = response.json()['data']['notesDetails']

            for data in notes_data:
                title = data['docTitle']
                url = data['docUrl'].replace("\\/", "/")
                text += f"{title}: {url}\n"

            with open(f"{name1}.txt", 'a') as f:
                f.write(f"{text}")

    except Exception as e:
        await message.reply_text(str(e))
        
    c_txt = f"**App Name: CareerWill\nBatch Name: `{name}`**"
    try:
        await app.send_document(message.chat.id, document=f"{name1}.txt", caption=c_txt)
    except Exception as e:
        await message.reply_text(f"Error sending document: {e}")

    await prog.delete()
    try:
        os.remove(f"{name1}.txt")
    except Exception as e:
        logging.error(f"Error deleting file: {e}")

async def career_will(app, message):
    try:
        input1 = await app.ask(message.chat.id, text="**Send ID & Password in this manner otherwise bot will not respond.\n\nSend like this:-  ID*Password\n\n OR Send Your Token**")
        login_url = "https://elearn.crwilladmin.com/api/v5/login-other"
        raw_text = input1.text

        if "*" in raw_text:
            headers = {
                "Host": "elearn.crwilladmin.com",
                "Apptype": "web",
                "accept": "application/json",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            }

            email, password = raw_text.split("*")
            data = {
                "deviceType": "web",
                "password": password,
                "deviceModel": "chrome",
                "deviceVersion": "Chrome+122",
                "email": email
            }

            response = requests.post(login_url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error if the request was unsuccessful
            token = response.json()["data"]["token"]
            await message.reply_text(f"**Login Successful**\n\n`{token}`")
        else:
            token = raw_text
    except Exception as e:
        await message.reply_text(f"An error occurred during login: {e}")
        return

    headers = {
        "Host": "elearn.crwilladmin.com",
        "Apptype": "web",
        "usertype": "2",
        "token": token,
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.9.1"
    }

    await input1.delete(True)
    batch_url = "https://elearn.crwilladmin.com/api/v5/my-batch"
    response = requests.get(batch_url, headers=headers)
    data = response.json()
    topicid = data["data"]["batchData"]

    FFF = "**BATCH-ID     -     BATCH NAME**\n\n"
    for data in topicid:
        FFF += f"`{data['id']}`     -    **{data['batchName']}**\n\n"

    await message.reply_text(f"**HERE IS YOUR BATCH**\n\n{FFF}")
    input2 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")
    raw_text2 = input2.text
    class_url = f"https://elearn.crwilladmin.com/api/v5/batch-topic/{raw_text2}?type=class"
    response = requests.get(class_url, headers=headers)
    topic_data = response.json()
    class_data = topic_data['data']['batch_topic']
    name = topic_data["data"]["batch_detail"]["name"]

    class_id = ""
    for data in class_data:
        topic_id = data["id"]
        class_id += f"{topic_id}&"

    notes_url = f"https://elearn.crwilladmin.com/api/v5/batch-topic/{raw_text2}?type=notes"
    r1 = requests.get(notes_url, headers=headers).json()
    notes_data = r1['data']['batch_topic']
    notes_id = ""
    for data in notes_data:
        topic_id = data["id"]
        notes_id += f"{topic_id}&"

    prog = await message.reply_text("**Extracting Videos Links Please Wait  📥 **")

    try:
        asyncio.create_task(careerdl(app, message, headers, raw_text2, class_id, notes_id, prog, name))
    except Exception as e:
        await message.reply_text(str(e))
