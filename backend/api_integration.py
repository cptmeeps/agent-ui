import requests

def call_external_api(endpoint, payload, headers):
    response = requests.post(endpoint, json=payload, headers=headers)
    return response.json()