import re
import random
from pyrogram import filters
from Extractor import app
from config import OWNER_ID, SUDO_USERS
from Extractor.core import script
from Extractor.core.func import subscribe, chk_user, add_thumb, view_thumb, remove_thumb
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Extractor.core.buttons import *
from Extractor.modules.appex_v2 import appex_v2_txt
from Extractor.modules.classplus import classplus_txt
from Extractor.modules.pw import pw_mobile, pw_token
from Extractor.modules.appex_v3 import appex_v3_txt
from Extractor.modules.careerwill import career_will
from Extractor.modules.khan import khan_login
from Extractor.modules.rg_vikramjeet import rgvikram_txt
from Extractor.modules.neon_classes import neon_txt
from Extractor.modules.civilguruji import civil_guru


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("start") & filters.user(SUDO_USERS))
async def start(_,message):
  join = await subscribe(_,message)
  if join ==1:
    return
  await message.reply_photo(photo=random.choice(script.IMG), 
                            caption=script.START_TXT.format(message.from_user.mention),
                            reply_markup=buttons)



@app.on_callback_query()
async def handle_callback(_, query):

    if query.data=="home_":                
        await query.message.edit_text(
              script.START_TXT.format(query.from_user.mention),
              reply_markup=buttons
            )
        
    elif query.data=="modes_":        
        reply_markup = InlineKeyboardMarkup(modes_button)
        await query.message.edit_text(
              script.MODES_TXT,
              reply_markup=reply_markup)
        
        
    elif query.data=="custom_":        
        reply_markup = InlineKeyboardMarkup(custom_button)
        await query.message.edit_text(
              script.CUSTOM_TXT,
              reply_markup=reply_markup
            )
        
     
    elif query.data=="manual_":        
        reply_markup = InlineKeyboardMarkup(button1)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="business_":        
        reply_markup = InlineKeyboardMarkup(business_button)
        await query.message.edit_text(
              script.BUSINESS_TXT,
              reply_markup=reply_markup
            )
       
    elif query.data=="thumb_":        
        reply_markup = InlineKeyboardMarkup(thumb_button)
        await query.message.edit_text(
              script.THUMB_TXT,
              reply_markup=reply_markup
            )
      
      
    elif query.data=="set_thumb":
        await add_thumb(query)

    elif query.data=="rm_thumb":
        await remove_thumb(query)

    elif query.data=="views_thumb":
        await view_thumb(query)  

  
    elif query.data=="v2_": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = await app.ask(query.message.chat.id, text="**SEND APPX API\n\n✅ Example:\ntcsexamzoneapi.classx.co.in**")
        api_txt = api.text
        name = api_txt.split('.')[0].replace("api", "") if api else api_txt.split('.')[0]
        await appex_v2_txt(app, query.message, api_txt, name)

    elif query.data=="v3_": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return 
        api = await app.ask(query.message.chat.id, text="**SEND APPX API\n\n✅ Example:\ntcsexamzoneapi.classx.co.in**")
        api_txt = api.text
        name = api_txt.split('.')[0].replace("api", "") if api else api_txt.split('.')[0]
        await appex_v3_txt(app, query.message, api_txt, name)
      
    elif query.data=="next_1":        
        reply_markup = InlineKeyboardMarkup(button2)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="next_2":        
        reply_markup = InlineKeyboardMarkup(button3)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="next_3":        
        reply_markup = InlineKeyboardMarkup(button4)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
          
        
    elif query.data=="maintainer_":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)


    elif query.data=="careerwill_":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        await career_will(app, query.message)
  
    elif query.data=="khan_":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return 
        await khan_login(app, query.message)

    elif query.data=="ss_maker": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "sscmakerexampreparationapi.classx.co.in"
        name = "SSC Makers"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="perfect_acc":  
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "perfectionacademyapi.appx.co.in"
        name = "Perfection Academy"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="e1_coaching":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "e1coachingcenterapi.classx.co.in"
        name = "e1 coaching"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="samyak_ras":  
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "samyakapi.classx.co.in"
        name = "Samyak"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="vj_education": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "vjeducationapi.appx.co.in"
        name = "VJ Education"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="gyan_bindu": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "gyanbinduapi.appx.co.in"
        name = "Gyan Bindu"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="dhananjay_ias": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "dhananjayiasacademyapi.classx.co.in"
        name = "Dhananjay IAS"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="think_ssc": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "thinksscapi.classx.co.in"
        name = "Think SSC"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="Ashish_lec":  
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "ashishsinghlecturesapi.classx.co.in"
        name = "Ashish Singh"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="tutors_adda": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "tutorsaddaapi.classx.co.in"
        name = "Tutors Adda"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="nimisha_bansal": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "nimishabansalapi.appx.co.in"
        name = "Nimisha Bansal"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="sachin_acc":  
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "sachinacademyapi.classx.co.in"
        name = "Sachin Academy"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="acharya_classes":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "acharyaclassesapi.classx.co.in"
        name = "Acharya Classes"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="target_plus": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "targetpluscoachingapi.classx.co.in"
        name = "Target Plus Coaching"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="rwa_":  
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "rozgarapinew.teachx.in"
        name = "Rojgar with Ankit"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="winners_": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "winnersinstituteapi.classx.co.in"
        name = "Winners"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="ocean_gurukul":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "oceangurukulsapi.classx.co.in"
        name = "Ocean Gurukul"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="mg_concept": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "mgconceptapi.classx.co.in"
        name = "MG Concept"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="yodha_":  
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "yodhaappapi.classx.co.in"
        name = "Yodha"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="note_book":  
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "notebookapi.classx.co.in"
        name = "Note Book"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="uc_live":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "ucliveapi.classx.co.in"
        name = "UC LIVE"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="space_ias": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "spaceiasapi.classx.co.in"
        name = "Space IAS"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="rg_vikramjeet": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "rgvikramjeetapi.classx.co.in"
        name = "RG Vikramjeet"
        await rgvikram_txt(app, query.message, api, name)
      
    elif query.data=="vidya_bihar": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "vidyabiharapi.teachx.in"
        name = "Vidya Vihar"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="aman_sir": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "amansirenglishapi.classx.co.in"
        name = "Aman Sir English"
        await appex_v2_txt(app, query.message, api, name)
      
    elif query.data=="nirman_ias": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "nirmaniasapi.classx.co.in"
        name = "Nirman IAS"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="permar_ssc": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "parmaracademyapi.classx.co.in"
        name = "Parmar Academy"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="neo_spark":  
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return 
        api = "neosparkapi.classx.co.in"
        name = "Neo Spark"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="md_classes":  
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "mdclassesapi.classx.co.in"
        name = "MD Classes"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="ng_learners": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "nglearnersapi.classx.co.in"
        name = "NG Learners"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="ssc_gurukul":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "ssggurukulapi.appx.co.in"
        name = "SSC Gurukul"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="army_study": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "armystudyliveclassesapi.classx.co.in"
        name = "Army Study Live"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="sankalp_": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "sankalpclassesapi.classx.co.in"
        name = "Sankalp"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="target_upsc": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "targetupscapi.classx.co.in"
        name = "Target UPSC"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="gk_cafe": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "gkcafeapi.classx.co.in"
        name = "GK Cafe"
        await appex_v3_txt(app, query.message, api, name)

    elif query.data == 'officers_acc':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "theofficersacademyapi.classx.co.in"
        name = "Officers Academy"
        await appex_v3_txt(app, query.message, api, name)

    elif query.data == 'rk_sir':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "rksirofficialapi.classx.co.in"
        name = "Rk Sir Official"
        await appex_v3_txt(app, query.message, api, name) 
      
    elif query.data == 'study_mantra':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "studymantraapi.classx.co.in"
        name = "Study Mantra"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'science_fun':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "sciencefunapi.classx.co.in"
        name = "Science Fun"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'grow_acc':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "growacademyapi.classx.co.in"
        name = "Grow Academy"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'goal_yaan':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "goalyaanapi.appx.co.in"
        name = "Goal Yaan"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'anilsir_iti':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "anilsiritiapi.classx.co.in"
        name = "Anil Sir Iti"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'education_adda':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "educationaddaplusapi.classx.co.in"
        name = "Education Adda Plus"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'achievers_acc':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "achieversacademyapi.classx.co.in"
        name = "Achievers Academy"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'commando_acc':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "commandoacademyapi.appx.co.in"
        name = "Commando Academy"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'exampur_':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "exampurapi.classx.co.in"
        name = "Exampur"
        await appex_v3_txt(app, query.message, api, name) 

  
    elif query.data == 'neet_kakajee':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "neetkakajeeapi.classx.co.in"
        name = "Neet Kaka JEE"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'app_exampur':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "exampurapi.classx.co.in"
        name = "App Exampur"
        await appex_v2_txt(app, query.message, api, name) 
  
    elif query.data=="classplus_":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        await classplus_txt(app, query.message)
      
    elif query.data=="neon_": 
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        await neon_txt(app, query.message)
  
    elif query.data=="Kautilya_tx":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "kautilyaalpjeapi.classx.co.in"
        name = "Kautilya Alp"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data=="SSBharti_tx":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "bhartilearningapi.appx.co.in"
        name = "Ss Bharti"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data=="Mission_tx":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "missionapi.appx.co.in"
        name = "Mission"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data=="Cadets_tx":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return 
        api = "cadetsdefenceacademyapi.classx.co.in"
        name = "Cadets Defence"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data=="civilguru_tx":
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return 
        await civil_guru(app, query.message)

    elif query.data == 'pw_':
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        await query.message.reply_text(
            "**CHHOSE FROM BELOW **",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("Mobile No.", callback_data='mobile_'),
                    InlineKeyboardButton("Token", callback_data='token_'),
                ]]))

    elif query.data == 'mobile_':
        await pw_mobile(app, query.message)

    elif query.data == 'token_':
        await pw_token(app, query.message)

  
    elif query.data=="sk_jha":  
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "aashapi.appx.co.in"
        name = "Sk jha Alp"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="science_mg":  
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "sciencemagnetapi.classx.co.in"
        name = "Science Magnet"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="study_lab":  
        lol = await chk_user(query, query.from_user.id)
        if lol == 1:
          return
        api = "learnamanbarkhaapi.classx.co.in"
        name = "Study lab"
        await appex_v3_txt(app, query.message, api, name)
      
      

  
      


  
       

                
  
    elif query.data == "premium_":
            button = [[
              InlineKeyboardButton(' ʙʀᴏɴᴢᴇ ', callback_data='bronze_'),
              InlineKeyboardButton(' ꜱɪʟᴠᴇʀ ', callback_data='silver_')
            ],[
              InlineKeyboardButton(' ɢᴏʟᴅ ', callback_data='gold_'),
              InlineKeyboardButton(' ᴏᴛʜᴇʀ ', callback_data='other_')
            ],[            
              InlineKeyboardButton(' ʙ ᴀ ᴄ ᴋ ', callback_data='home_')
            ]]
        
            reply_markup = InlineKeyboardMarkup(button)
            await query.message.edit_text(
             text=script.PLANS_TXT,
             reply_markup=reply_markup
            )
            
    
          
    elif query.data == "bronze_":
            button = [[
              InlineKeyboardButton('☎️ ᴄᴏɴᴛᴀᴄᴛ ', user_id=int(OWNER_ID))
            ],[
              InlineKeyboardButton('⋞', callback_data='other_'),
              InlineKeyboardButton('ʙ ᴀ ᴄ ᴋ', callback_data='premium_'),
              InlineKeyboardButton('⋟', callback_data='silver_')
            ]]
      
            reply_markup = InlineKeyboardMarkup(button)
            await query.message.edit_text(
             text=script.BRONZE_TXT,
             reply_markup=reply_markup             
            )

    elif query.data == "silver_":
            button = [[
              InlineKeyboardButton('☎️ ᴄᴏɴᴛᴀᴄᴛ ', user_id=int(OWNER_ID))
            ],[
              InlineKeyboardButton('⋞', callback_data='bronze_'),
              InlineKeyboardButton('ʙ ᴀ ᴄ ᴋ', callback_data='premium_'),
              InlineKeyboardButton('⋟', callback_data='gold_')
            ]]
      
            reply_markup = InlineKeyboardMarkup(button)
            await query.message.edit_text(
             text=script.SILVER_TXT,
             reply_markup=reply_markup             
            )
            
    elif query.data == "gold_":
            button = [[
              InlineKeyboardButton('☎️ ᴄᴏɴᴛᴀᴄᴛ ', user_id=int(OWNER_ID))
            ],[
              InlineKeyboardButton('⋞', callback_data='silver_'),
              InlineKeyboardButton('ʙ ᴀ ᴄ ᴋ', callback_data='premium_'),
              InlineKeyboardButton('⋟', callback_data='other_')
            ]]
      
            reply_markup = InlineKeyboardMarkup(button)
            await query.message.edit_text(
             text=script.GOLD_TXT,
             reply_markup=reply_markup
            )
      
    elif query.data == "other_":
            button = [[
              InlineKeyboardButton('☎️ ᴄᴏɴᴛᴀᴄᴛ ', user_id=int(OWNER_ID))
            ],[
              InlineKeyboardButton('⋞', callback_data='gold_'),
              InlineKeyboardButton('ʙ ᴀ ᴄ ᴋ', callback_data='premium_'),
              InlineKeyboardButton('⋟', callback_data='bronze_')
            ]]
      
            reply_markup = InlineKeyboardMarkup(button)
            await query.message.edit_text(
             text=script.OTHER_TXT,
             reply_markup=reply_markup         
            )

  

    elif query.data=="close_data":
        await query.message.delete()
        await query.message.reply_to_message.delete()
