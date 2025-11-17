print("Simple Password Generator")

name = input("Enter your name: ")
fav = input("Enter your favourite word: ")
num = input("Enter any number: ")

base = name + fav + num

password = ""

for i in range(len(base)):
    ch = base[i]

    if i % 2 == 0:
        password += ch.upper()
    else:
        password += ch.lower()

    password += str(i)

print("\nYour Generated Password:")
print(password)
