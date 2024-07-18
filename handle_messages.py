from random import randint
from rory import get_random_rory_fact_payload

GROUPME_BOT_ID = "aed3cc26b4e763add79c53b3a6"

def handle_message(message_text,sender_name ="simp"):
    payload = ""
    
    if "bryson" in message_text.lower():
        payload = {
            "bot_id"  : GROUPME_BOT_ID,
            "attachments" : [
                {
                "type"  : "image",
                "url"   : "https://i.groupme.com/542x406.png.7867989eb8bb4feab6adecaab94a68f9.large"
                }
            ]
            } 
    elif "!roryfact" in message_text.lower()[0:12]:
        payload = rory_facts(sender_name)
    elif "rory" in message_text.lower():
        payload = rory_response(sender_name)
    elif "rors" in message_text.lower():
        payload = rory_response(sender_name)
    elif "mcilroy" in message_text.lower():
        payload = rory_response(sender_name)
        
    return payload   


def rory_facts(sender_name:str="simp"):
    payload = get_random_rory_fact_payload(GROUPME_BOT_ID)
    return payload

def rory_response(sender_name):
    
    if not sender_name:
        sender_name = "simp"
    payload = ""
    
    
    # choose a random result
    x = randint(1,4)
   

    if x==6:
        pass
        # payload = {
        #     'bot_id': GROUPME_BOT_ID,
        #     'text': f"Hey, {sender_name}. Stop trying to make Rory happen. It's not going to happen."
        # }
            
    elif x==1:
        
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
        
        
    elif x==2:
        payload = {
            "bot_id"  : GROUPME_BOT_ID,
            "attachments" : [
                {
                "type"  : "image",
                "url"   : "https://i.groupme.com/480x270.gif.9a4b943354ed4796896f2a9699f5360b.large"
                }
            ]
            }
         
    elif x==3:
        payload = {
            "bot_id"  : GROUPME_BOT_ID,
            "attachments" : [
                {
                "type"  : "image",
                "url"   : "https://i.groupme.com/2094x1572.jpeg.726e68e391bd43c48840bed10626481c.large"
                }
            ]
            } 
    
    elif x==4:
        payload = get_random_rory_fact_payload()
    
    
    return payload