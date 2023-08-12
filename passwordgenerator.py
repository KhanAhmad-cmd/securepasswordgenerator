#Import random library
import random

#Initilaze the characters to include in the password
lowercase = "abcdefghjkmnpqrstuvwxyz"
Uppercase = "ABCDEFGHJKMNPQRSTUVWXYZ"
Numerical = "23456789"
SpecialChar = "#*&@$"

#Add the strings
string = lowercase + Numerical + SpecialChar + Uppercase

#Specify the length of the password to generate
length = input("Enter the number of character: ")

#The generator
password = "".join(random.sample(string, int(length)))
print("Your secure password is: " + password)
