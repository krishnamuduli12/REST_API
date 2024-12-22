travelling = input("yes or no:")

while travelling == 'yes':
    num = int(input("Number of passenger travelling:"))
    
    for num in range(1, num+1):
        name = input("Name: ")
        age = input("Age: ")
        sex = input("male or Female: ")
        
        print(name, age, sex)
        