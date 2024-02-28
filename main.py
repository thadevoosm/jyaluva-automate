import pandas as pd
import requests
import json

URL = "https://graph.facebook.com/v17.0/${YourNumberID}/messages"
head = {
    "Authorization": "Bearer ${APIKEY}",
    "Content-Type": "application/json"
}

def send_mail():
    data = pd.read_csv('phone_numbers.csv')

    for index, row in data.iterrows():
        no = f"91{row['phone_number']}"
        print(f"Message sent to {row['phone_number']}. Status: ")
        name = row['name']

        print(no)
        print(name)

        body = {
            "messaging_product": "whatsapp",
            "to": no,
            "type": "template",
            "template": {
                "name": "09sept",
                "language": {
                    "code": "ml"
                },
              
                "components": [
                    {
                        "type": "header",
                        "parameters": [
                            {
                                "type": "image",
                                "image": {
                                    "link": "https://imagelin.com/image.jpg"
                                }
                            }
                        ]
                    },
                     {"type": "body",
                "parameters": [
                	# {
                	# 	"type": "text",
                	# 	"text": name
                    #  }
                    ]}
                ]
            }
        }
        
        try:
            # Send the POST request
            response = requests.post(URL, headers=head, data=json.dumps(body))
            response.raise_for_status()  # Raise an exception if the response status is not 200
            
            # Check the response status
            if response.status_code == 200:
                print("Message sent successfully")
            else:
                print("Failed to send message")
        
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

send_mail()
