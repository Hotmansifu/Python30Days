import string
import random

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

account = input("Enter Account/Username name: ")
length = int(input("Enter password length: "))
password = generate_password(length)

with open("passwords.txt", "a") as file:
    file.write(f"Account: {account} Password: {password}\n")

print("Password saved to passwords.txt")
