import base64
import json
import requests
from requests.exceptions import HTTPError

#API Credentials
username = ''
password = ''
userpass = username + ':' + password
#Encode API Creds as base64
auth = base64.b64encode(userpass.encode()).decode()

#updateMessage takes channel as a param which can be toggled as: internal-note (or) email
def updateMessage(ticket_id, auth, body_html, channel, from_address, to_address):
    base_url = "https://{domain}.gorgias.com/api/" #Please update {domain} with your respective domain
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": ""
    }
    headers.update({
        "Authorization": "Basic %s" % auth
    })
    url = base_url + "tickets/" + ticket_id + "/" + "messages"
    payload = {
        'body_html': '',
        'channel': '',
        'from_agent': True,
        'source': {
            'type': 'email',
            'from': {
                'address': ''
            },
            'to': [{
                'address': ''
            }]
        },
        'via': 'api',
    }

    payload.update({
        'body_html': body_html,
        'channel': channel,
        'source': {
            'type': 'email',
            'from': {
                'address': from_address
            },
            'to': [{
                'address': to_address
            }]
        }
    })
    print(payload)

    try:
        response = requests.post(url, json = payload, headers = headers)
        response.raise_for_status()
        jsonResponse = response.json()
        return response.status_code

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

#Populate params to config message and channel
ticket_id = ""
body_html = "Please be advised that your order has been shipped."
channel = ""
from_address = ""
to_address = ""

res = updateMessage(ticket_id, auth, body_html, channel, from_address, to_address)
print(res)
