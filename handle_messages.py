import re
from datetime import datetime
from random import randint

GROUPME_BOT_ID = "aed3cc26b4e763add79c53b3a6"

def handle_message(message_text,sender_name ="simp"):
    payload = ""
    
    if "bryson" in message_text.lower():
        payload ={
            "bot_id"  : GROUPME_BOT_ID,
            "attachments" : [
                {
                "type"  : "image",
                "url"   : "https://i.groupme.com/542x406.png.7867989eb8bb4feab6adecaab94a68f9.large"
                }
            ]
            } 
    elif "rory" in message_text.lower():
        payload = rory_response(sender_name)
    elif "rors" in message_text.lower():
        payload = rory_response(sender_name)
    elif "mcilroy" in message_text.lower():
        payload = rory_response(sender_name)
        
    return payload   


def rory_response(sender_name):
    
    if not sender_name:
        sender_name = "simp"
    payload = ""
    
    
    # choose a random result
    x = randint(1,5)
    
    # if then switch for the funny jokes
    if x == 1:
        # Define the target date
        target_date = datetime(2014, 8, 10)
        current_date = datetime.now()

        # Calculate the difference in days
        days_since = (current_date - target_date).days
        payload = {
            'bot_id': GROUPME_BOT_ID,
            'text': f"{sender_name}, it has been {days_since} days since Rory McIlroy has won a major."
        }
        
    elif x==2:
        # Define the target date
        target_date = datetime(2024, 6, 16)
        current_date = datetime.now()

        # Calculate the difference in days
        days_since = (current_date - target_date).days

        payload = {
            'bot_id': GROUPME_BOT_ID,
            'text': f"{sender_name}, it has been {days_since} days since Rory McIlroy missed a 3 foot putt in a major."
        }
        
        

    elif x==6:
        pass
        # payload = {
        #     'bot_id': GROUPME_BOT_ID,
        #     'text': f"Hey, {sender_name}. Stop trying to make Rory happen. It's not going to happen."
        # }
            
    elif x==8:
        
        payload = {
            "bot_id"  : GROUPME_BOT_ID,
            "attachments" : [
                {
                "type"  : "image",
                "url"   : "https://i.groupme.com/542x406.png.7867989eb8bb4feab6adecaab94a68f9.large"
                }
            ]
            }
        
        
    elif x==7:
        pass
        # payload = {
        #     "bot_id"  : GROUPME_BOT_ID,
        #     "message" : "Rory addiction is a serious disease that affects millions of golf fans around the world.",
        #     "attachments" : [
        #         {
        #         "type"  : "image",
        #         "url"   : "https://i.groupme.com/480x358.gif.2d2aa3e614524c2eb5b03437ae927eb0.large"
        #         }
        #     ]
        #     }
        
        
    elif x==4:
            payload = {
                "bot_id"  : GROUPME_BOT_ID,
                "attachments" : [
                    {
                    "type"  : "image",
                    "url"   : "https://i.groupme.com/480x270.gif.9a4b943354ed4796896f2a9699f5360b.large"
                    }
                ]
                }
         
    elif x==5:
                payload = {
                    "bot_id"  : GROUPME_BOT_ID,
                    "attachments" : [
                        {
                        "type"  : "image",
                        "url"   : "https://i.groupme.com/2094x1572.jpeg.726e68e391bd43c48840bed10626481c.large"
                        }
                    ]
                    } 
    
    
    
    
    return payload