import requests
import json
webhook_url = 'http://127.0.0.1:5000/webhook'

data = {
    'name': 'brad',
    'Channel URL': 'test url'
}

r = requests.post(webhook_url,data=json.dumps(data),headers={'Contet-Type': 'application/json'})