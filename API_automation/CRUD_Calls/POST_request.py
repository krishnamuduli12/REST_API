#API url https://reqres.in/api/users
import requests
import json
import jsonpath

#API url
url = "https://reqres.in/api/users"

file = open("C:\\workspace\\Learning\\Python\\API_automation\\create_json1.json",'r')
json_input = file.read()  #This just loads the contents in form of strings to a object called json_input
#print(json_input)

request_json = json.loads(json_input) # converts the string to json format 

#print(request_json)

#Make post request with json input body
response = requests.post(url,request_json)
#print(response.content)

assert response.status_code == 201 #for successful POST call its 201 status code

#fetch header from response
#print(response.headers.get('Content-Length'))

#prse response in json format
response_json = json.loads(response.text)

#pick a value e.g. id from response 
job1 = jsonpath.jsonpath(response_json, 'name')
print(job1)

