

# try:
#     user_input1 = input("please Enterfirst number: ")
#     user_input2 = input("please Enter second  number: ")
#     c = int(user_input1) + int(user_input2)
#     print(c)
# except:
#     print("ERROR : Your input is incorrect please correct data !!!")
# finally:
#     print("this code i want to execute in the end !!!")

import configParser

#created an object of Configparser class
config = configParser

# To read data from config file
config.read("./InputFiles/config.cfg")

print(config.get("Krishna", "username"))


