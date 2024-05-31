from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ------------------------------------------------------------------------------- #

buttons = InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("ᴍ ᴏ ᴅ ᴇ s", callback_data="modes_")
                ],[
                  InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/Mohitag24"),
                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/Mohitag24")
                ],[
                  InlineKeyboardButton("ᴘ ʟ ᴀ ɴ s", callback_data="premium_")
                ]])


modes_button = [[
                  InlineKeyboardButton("ᴄᴜsᴛᴏᴍ", callback_data="custom_"),
                  InlineKeyboardButton("ᴍᴀɴᴜᴀʟ", callback_data="manual_"),
                ],[
                  InlineKeyboardButton("ᴛʜᴜᴍʙɴᴀɪʟ", callback_data="thumb_"),
                  InlineKeyboardButton("ʙᴜꜱɪɴᴇꜱꜱ", callback_data="business_")
                ],[
                  InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="home_")
                ]]


custom_button = [[
                  InlineKeyboardButton("Appex V2", callback_data="v2_"),
                  InlineKeyboardButton("Appex V3", callback_data="v3_"),
                ],[
                  InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="modes_")
                ]]


thumb_button = [[
                  InlineKeyboardButton("ᴀᴅᴅ-ᴛʜᴜᴍʙ", callback_data="set_thumb"),
                  InlineKeyboardButton("ᴠɪᴇᴡ-ᴛʜᴜᴍʙ", callback_data="views_thumb"),
                ],[  
                  InlineKeyboardButton("ʀᴇᴍᴏᴠᴇ-ᴛʜᴜᴍʙ", callback_data="rm_thumb"),
                ],[
                  InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="modes_")
                ]]


business_button = [[
                  InlineKeyboardButton("ᴜꜱᴇʀꜱ ᴅᴀᴛᴀ", callback_data="maintainer_")
                ],[
                  InlineKeyboardButton("ᴘᴀɴɴᴇʟꜱ", callback_data="maintainer_"),
                  InlineKeyboardButton("ꜱᴛᴀᴛᴜꜱ", callback_data="maintainer_")
                ],[
                  InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="modes_")
                ]]









button1 = [              
                [
                    InlineKeyboardButton("Ashish Sing Lec", callback_data="Ashish_lec"), 
                    InlineKeyboardButton("Exampur", callback_data="exampur_"),
                    InlineKeyboardButton("Acharya Classes", callback_data="acharya_classes")
                ],
                [
                    InlineKeyboardButton("Aman Sir", callback_data="aman_sir"), 
                    InlineKeyboardButton("Goal Yaan", callback_data="goal_yaan"),
                    InlineKeyboardButton("Army Study", callback_data="army_study")    
                ],
                [
                    InlineKeyboardButton("App Exampur", callback_data="app_exampur"),
                    InlineKeyboardButton("Gk Cafe", callback_data="gk_cafe"),
                    InlineKeyboardButton("Anil Sir iti", callback_data="anilsir_iti")             
                ],
                [
                    InlineKeyboardButton("Achievers Academy", callback_data="achievers_acc"), 
                    InlineKeyboardButton("Khan", callback_data="khan_"),
                    InlineKeyboardButton("Classplus", callback_data="classplus_")                  
                ],
                [
                    InlineKeyboardButton("Careerwill", callback_data="careerwill_"), 
                    InlineKeyboardButton("Md Classes", callback_data="md_classes"),
                    InlineKeyboardButton("Cammando Academy", callback_data="commando_acc")                    
                ],
                [
                    InlineKeyboardButton("Dhananjay IAS", callback_data="dhananjay_ias"), 
                    InlineKeyboardButton("Note Book", callback_data="note_book"),
                    InlineKeyboardButton("E1 Coaching", callback_data="e1_coaching")         
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_3"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_1")
                ]
                ]


button2 = [
                [
                    InlineKeyboardButton("Neo Spark", callback_data="neo_spark"),
                    InlineKeyboardButton("Ng Learners", callback_data="ng_learners"),   
                    InlineKeyboardButton("Education Adda", callback_data="education_adda"),
                ],
                [
                    InlineKeyboardButton("Neet Kakajee", callback_data="neet_kakajee"),
                    InlineKeyboardButton("Officers Academy", callback_data="officers_acc"),   
                    InlineKeyboardButton("Grow Academy", callback_data="grow_acc")
                ],
                [
                    InlineKeyboardButton("Ocean Gurukul", callback_data="ocean_gurukul"),
                    InlineKeyboardButton("Perfect Academy", callback_data="perfect_acc"),   
                    InlineKeyboardButton("Gyan Bindu", callback_data="gyan_bindu")     
                ],
                [
                    InlineKeyboardButton("Parmar Ssc", callback_data="permar_ssc"),
                    InlineKeyboardButton("Physics Wallah", callback_data="pw_"),   
                    InlineKeyboardButton("Mg Concept", callback_data="mg_concept")              
                ],
                [
                    InlineKeyboardButton("Rg Vikramjeet", callback_data="rg_vikramjeet"),
                    InlineKeyboardButton("Rk Sir", callback_data="rk_sir"),   
                    InlineKeyboardButton("Nimisha Bansal", callback_data="nimisha_bansal")     
                ],
                [
                    InlineKeyboardButton("Rwa", callback_data="rwa_"),
                    InlineKeyboardButton("Samyak", callback_data="samyak_ras"),   
                    InlineKeyboardButton("Nirman IAS", callback_data="nirman_ias")       
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="manual_"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_2")
                ]
                ]



button3 = [              
                [   
                    InlineKeyboardButton("Sachin Academy", callback_data="sachin_acc"),
                    InlineKeyboardButton("Vidya Bihar", callback_data="vidya_bihar"),
                    InlineKeyboardButton("Space IAS", callback_data="space_ias")
                ],
                [   
                    InlineKeyboardButton("Ssc Gurkul", callback_data="ssc_gurukul"),
                    InlineKeyboardButton("Winners", callback_data="winners_"),
                    InlineKeyboardButton("Sankalp", callback_data="sankalp_")
                ],
                [
                    InlineKeyboardButton("Study Mantra", callback_data="study_mantra"),
                    InlineKeyboardButton("Neon", callback_data="neon_"),
                    InlineKeyboardButton("Science Fun", callback_data="science_fun")
                ],
                [   
                    InlineKeyboardButton("Ssc Maker", callback_data="ss_maker"),
                    InlineKeyboardButton("Yodha", callback_data="yodha_"),
                    InlineKeyboardButton("Target Plus", callback_data="target_plus")
                ],
                [
                    InlineKeyboardButton("Tutors Adda", callback_data="tutors_adda"),
                    InlineKeyboardButton("SS Bharti", callback_data="SSBharti_tx"),
                    InlineKeyboardButton("Think Ssc", callback_data="think_ssc")
                ],
                [              
                    InlineKeyboardButton("Target Upsc", callback_data="target_upsc"),
                    InlineKeyboardButton("Mission", callback_data="Mission_tx"),
                    InlineKeyboardButton("Uc Live", callback_data="uc_live")
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_1"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_3")
                ]
                ]


button4 = [              
                [   
                    
                    InlineKeyboardButton("Civil Guruji", callback_data="civilguru_tx"),
                    InlineKeyboardButton("Vj Education", callback_data="vj_education"),
                    InlineKeyboardButton("Kautilya Alp", callback_data="Kautilya_tx")
                  
                ],
                [
                    InlineKeyboardButton("Study lab", callback_data="study_lab"),
                    InlineKeyboardButton("SK JHA ALP", callback_data="sk_jha"),
                    InlineKeyboardButton("SCIENCE MAGNET", callback_data="science_mg")
                    
                ],
                [              
                    InlineKeyboardButton("Cadets Defence", callback_data="Cadets_tx"),
                    InlineKeyboardButton("Soon", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_2"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="manual_")
                ]
                ]




back_button  = [[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="modes_"),                    
                ]]

