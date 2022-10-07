import os
import requests

auth_token = os.environ['WHATSAPP']
phone_from = os.environ['WHATSAPP_PHONE_FROM']
phone_to = os.environ['WHATSAPP_PHONE_TO']

headers = {
    'Authorization': 'Bearer '+auth_token+"'",
    'Content-Type': 'application/json'
}

data = '''
{ "messaging_product": "whatsapp", 
  "to": "{phone_to}", 
  "type": "template", 
  "template": { 
    "name": "hello_world", 
    "language": { "code": "en_US" } 
    } 
}
'''

data2 =  '''
{ "messaging_product": "whatsapp", 
  "recipient_type": "individual",
  "to": "50671400049", 
  "type": "text", 
  "text": { 
            "preview_url": false, 
            "body": "This is a message from Cesar Vezga" 
          } 
}
'''

body = data.replace("{phone_to}", phone_to)

response = requests.post(f'https://graph.facebook.com/v15.0/{phone_from}/messages', headers=headers, data=body)

print(response)

