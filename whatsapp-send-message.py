import os
import requests
import json

auth_token = os.environ['WHATSAPP']
phone_from = os.environ['WHATSAPP_PHONE_FROM']
phone_to = os.environ['WHATSAPP_PHONE_TO']

print(auth_token)
print(phone_from)
print(phone_to)

factura = '''
C h a l e t   O c a m p o\n
-------------------------\n
No.: 10-0023  07-Oct-2022\n

2 Balde Nac.    14.000,00\n
1 Patacon Chal.  3.000,00\n
3 Chiliguaro     3.000.00\n
                ---------\n
         Total: 20.000,00\n

'''

headers = {
    'Authorization': 'Bearer '+auth_token+"'",
    'Content-Type': 'application/json'
}

data = '''
{ "messaging_product": "whatsapp", 
  "to": "{phone_to}", 
  "type": "template", 
  "template": { 
    "name": "oferta_chalet_ocampo", 
    "language": { "code": "es" },
     "components" : 
             [
                    {
                        "type": "body",
                        "parameters": [ { "type": "text", "text": "- Balde nacional a 7 mil!" } ]
                    }
            ]           
        
    }
}
'''

# El destinatario tiene que llamar primero para poder responder
# IMPORTANT: If a customer has not messaged you first, then the first time you send a message to a user, 
# WhatsApp requires that the message contains a template. This is explained in more detail in the Understanding WhatsApp topic.
# ref: https://developer.vonage.com/messages/code-snippets/whatsapp/send-text

data2 =  '''
{ "messaging_product": "whatsapp", 
  "recipient_type": "individual",
  "to": "{phone_to}", 
  "type": "text", 
  "text": { 
            "preview_url": false, 
            "body": "This is a message from Cesar Vezga" 
          } 
}
'''

body = data.replace("{phone_to}", phone_to)
body2 = data2.replace("{phone_to}", phone_to)

response = requests.post(f'https://graph.facebook.com/v15.0/{phone_from}/messages', headers=headers, data=body)

print(response.text)
