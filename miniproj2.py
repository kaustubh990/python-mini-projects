#random password generator
import string #importing string module to get ascii letters and digits  
import random #importing random module to generate random password
password_length = int(input("Enter the desired password length: ")) #taking user input for password length
charvar = string.ascii_letters + string.digits+string.punctuation #combining ascii letters and digitss
password=""
for i in range(password_length):
    password+=random.choice(charvar) #generating random password
print("Generated Password:", password) #printing the generated password
