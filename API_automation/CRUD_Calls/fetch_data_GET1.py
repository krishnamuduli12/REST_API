#API url https://reqres.in/api/users?page=2
import requests
import json
import jsonpath

url = "https://httpbin.org/get"

headerdata = {'T1':'First_Header','T2':'Second_Header'}
param = {'name':'cyberworld','email':'cipher@ciph.com','number':'12334465'}

response = requests.get(url, headers=headerdata, params=param)
print(response.text)

#display content from response 
#print(response.content)

#parse response in json format
# json_response = json.loads(response.text)
#print(json_response)

#fetch values using jsonpath
# pages = jsonpath.jsonpath(json_response,'data[3].avatar')
# print(pages)
# #assert pages[0] == 2

# for i in range(0, 3):
#     first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
#     print(first_name[0])                             