#API url https://reqres.in/api/users?page=2
import requests

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
#display content from response 
#print(response.content)

#response header
print(response.headers)



