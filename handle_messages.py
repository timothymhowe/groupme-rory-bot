from random import randint
import os
from rory import get_random_rory_fact_payload, get_random_rory_fact

GROUPME_BOT_ID = "8c57401d35ebfc04348db5c20e"


def handle_message(message_text, sender_name="simp"):
    payload = ""

    if "bryson" in message_text.lower():
        payload = {
            "bot_id": GROUPME_BOT_ID,
            "attachments": [
                {
                    "type": "image",
                    "url": "https://i.groupme.com/542x406.png.7867989eb8bb4feab6adecaab94a68f9.large",
                }
            ],
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


def rory_facts(sender_name: str = "simp"):
    payload = get_random_rory_fact_payload(GROUPME_BOT_ID)
    return payload


def rory_response(sender_name):

    if not sender_name:
        sender_name = "simp"
    payload = ""

    # choose a random result
    x = randint(1, 4)

    last_random_main = get_last_generated_number()
    new_number = randint(2, 5)
    while new_number == last_random_main:
        new_number = randint(2, 5)
    set_last_generated_number(new_number)
    x = new_number

    # switch for the different message options.  not great, but not terrible.  
    if x == 1:
        payload = {
            "bot_id": GROUPME_BOT_ID,
            "attachments": [
                {
                    "type": "image",
                    "url": "https://i.groupme.com/542x406.png.7867989eb8bb4feab6adecaab94a68f9.large",
                }
            ],
        }

    elif x == 2:
        payload = {
            "bot_id": GROUPME_BOT_ID,
            "attachments": [
                {
                    "type": "image",
                    "url": "https://i.groupme.com/480x270.gif.9a4b943354ed4796896f2a9699f5360b.large",
                }
            ],
        }

    elif x == 3:
        payload = {
            "bot_id": GROUPME_BOT_ID,
            "attachments": [
                {
                    "type": "image",
                    "url": "https://i.groupme.com/2094x1572.jpeg.726e68e391bd43c48840bed10626481c.large",
                }
            ],
        }

    elif x == 4:
        payload = {
            "bot_id": GROUPME_BOT_ID,
            "text": f"Fun Fact: {get_random_rory_fact()}",
        }

    elif x == 5:
        payload = {"bot_id": GROUPME_BOT_ID, "text": "cope harder"}

    return payload


def get_last_generated_number():
    if os.path.exists("last_random_main.txt"):
        with open("last_random_main.txt", "r") as file:
            return int(file.read())
    return None


def set_last_generated_number(number):
    with open("last_random_main.txt", "w") as file:
        file.write(str(number))
