# PYTHON CODE TO GENERATE THE PASSWORD

import random as rd
# creating the string that contains all the characters and numbers
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_+=?"

# taking the length of the password from the user 
length = int(input("Enter the length of the password: "))

password =  ""
for i in range(length):
  password += rd.choice(char)
print("Password: ", password)
