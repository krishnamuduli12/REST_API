#API url https://reqres.in/api/users
import requests
import json
import jsonpath

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


