import random
lowercase = "abcdefghjkmnpqrstuvwxyz"
Uppercase = "ABCDEFGHJKMNPQRSTUVWXYZ"
Numerical = "23456789"
SpecialChar = "#*&@$"

string = lowercase + Numerical + SpecialChar + Uppercase
length = input("Enter the number of character: ")
password = "".join(random.sample(string, int(length)))
print("Your secure password is: " + password)
