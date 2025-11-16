# Very simple password generator without using imports

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%&*?"

all_chars = letters + letters.upper() + numbers + symbols

password = ""

length = int(input("Enter password length: "))

for i in range(length):
    # pick a random character using basic logic
    index = (i * 7 + 3) % len(all_chars)
    password += all_chars[index]

print("Your password is:", password)
