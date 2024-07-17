from flask import Flask, jsonify, request
import requests
from handle_messages import handle_message

app = Flask(__name__)

@app.route('/test/me', methods=['GET'])
def test_me():
    
    url = 'https://api.groupme.com/v3/bots/post'

    incoming_message = {
        "attachments": [],
        "avatar_url": "https://i.groupme.com/123456789",
        "created_at": 1302623328,
        "group_id": "1234567890",
        "id": "1234567890",
        "name": "John",
        "sender_id": "12345",
        "sender_type": "user",
        "source_guid": "GUID",
        "system": False,
        "text": "Hello rory, you little bumbolina bryson .",
        "user_id": "1234567890"
        }

    response = ""
    
    if incoming_message['sender_type'] != 'bot':
        message_text = incoming_message['text']
        message_sender = incoming_message['name']
        response = handle_message(message_text,message_sender)
    
    if response:
        print(response)
        requests.post(url, json=response)
        
        
    
    return response


@app.route('/groupme/inbox', methods=['POST'])
def inbox_webhook():
    
    url = 'https://api.groupme.com/v3/bots/post'

    incoming_message = request.json
    response = ""
    
    if incoming_message['sender_type'] != 'bot':
        message_text = incoming_message['text']
        message_sender = incoming_message['name']
        response = handle_message(message_text,message_sender)
    
    if response:
        print(response)
        requests.post(url, json=response)
        
        
    
    return "ok",200
        

def send_response():
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8001)
    
    test_data = {
        "attachments": [],
        "avatar_url": "https://i.groupme.com/123456789",
        "created_at": 1302623328,
        "group_id": "1234567890",
        "id": "1234567890",
        "name": "John",
        "sender_id": "12345",
        "sender_type": "user",
        "source_guid": "GUID",
        "system": False,
        "text": "Hello rory",
        "user_id": "1234567890"
        }
    
    data = jsonify(test_data)
    app.post('/groupme/inbox',data)
    
    print("I guess its, Hello World!")
