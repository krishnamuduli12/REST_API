list1 = ["Python", "CSharp", "Java", "Go"]

list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]

# function that filters duplicate string
def filterDuplicate(string_to_check):
    if(string_to_check in newlist):
        return False
    else:
        return True
    
 # Demonstrating filter() to remove duplicate strings
 
newlist = list2

out_filter = list(filter(filterDuplicate, list1))

newlist = list1

out_filter = list(filter(filterDuplicate, list2))

print("The new filtered list is: ", out_filter)
    