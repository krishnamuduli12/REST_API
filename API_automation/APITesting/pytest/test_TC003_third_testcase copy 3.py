#Write POST request and the url is https://reqres.in/api/users
import requests
import json
import jsonpath
import pytest

#URL path
url = "https://reqres.in/api/users"

@pytest.mark.Smoke
def test_create_user():
    #Read the input file
    file = open("C:\workspace\Learning\Python\API_automation\create_json1.json",'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    #Make POST call 
    response = requests.post(url, request_json)

    #print(response.content)
    assert response.status_code == 201

    #print response header
    #print(response.headers.get('Content-Length'))

    #parse response in Json format
    response_json = json.loads(response.text)

    #pick content from response json
    content_json = jsonpath.jsonpath(response_json, 'job')
    print(content_json)

@pytest.mark.Sanity
def test_GET_User():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    #display content from response 
    #print(response.content)

    #parse response in json format
    json_response = json.loads(response.text)
    #print(json_response)

    #fetch values using jsonpath
    pages = jsonpath.jsonpath(json_response,'total_pages')
    #print(pages[0])
    assert pages[0] == 2
def test_delete_resource():
    #API url https://reqres.in/api/users/2
    url = "https://reqres.in/api/users/2"

    response = requests.delete(url)

    #Fetch response code
    #print(response.status_code)
    assert response.status_code == 204
def test_PUT_resource():
    #API url
    url = "https://reqres.in/api/users/2"

    file = open("C:\\workspace\\Learning\\Python\\API_automation\\create_json1.json",'r')
    json_input = file.read()  #This just loads the contents in form of strings to a object called json_input
    #print(json_input)
    request_json = json.loads(json_input)

    #make a PUT call 
    response = requests.put(url,request_json)
    #print(response.content) 

    assert response.status_code == 200 #response code is 200


    response_json = json.loads(response.text)
    content_check = jsonpath.jsonpath(response_json,'updatedAt')
    print(content_check[0])




