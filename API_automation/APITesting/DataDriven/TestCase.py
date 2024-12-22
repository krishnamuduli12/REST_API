import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library

def test_add_multiple_student():
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    f = open("C:\\workspace\\Learning\\Python\\API_automation\\APITesting\\Student\\AddNewStudent.json","r")
    json_request = json.loads(f.read())
     
    obj = Library.Common("C:\\workspace\\Learning\\Python\\API_automation\\APITesting\\Student\\test_data.xlsx","Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()
    
    
    
    
    for i in range(2, row+1):
        updated_json_request = obj.update_request_with_data(i, json_request, keyList)
        response = requests.post(url,updated_json_request)
        print(response)
        
                
        
       
    
    
    
    