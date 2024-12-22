import json
import jsonpath
import requests

def test_oAuth_api():
    token_url = ''https://thetestingworldapi.com/Token'
    data = {'grant_type':'password','username':'admin','password': 
    response1 = requests.post(token_url, data)
    print(response1.text)
    API_URL = 'https://thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(API_URL)
    print(response.text)