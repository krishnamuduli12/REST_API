#There are 2 lists merrge 2 lists to form a dictionary with key:value pair 

def list_to_dict():
    key = [1,2,3,4,5]
    value = ["one", "two", "three", "four", "five"]
    
    result = dict(zip(key, value))
    
    print(result)
    
list_to_dict()