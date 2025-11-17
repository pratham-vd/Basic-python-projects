
score = 0  

print("Welcome to the Quiz Game!\n")

# Question 1
print("1) What is the capital of India?")
print("a) Mumbai")
print("b) New Delhi")
print("c) Kolkata")

answer = input("Your answer: ")

if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong!\n")

# Question 2
print("2) How many states are there in India?")
print("a) 28")
print("b) 29")
print("c) 27")

answer = input("Your answer: ")

if answer.lower() == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong!\n")

# Question 3
print("3) Which planet is known as the Red Planet?")
print("a) Earth")
print("b) Mars")
print("c) Venus")

answer = input("Your answer: ")

if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong!\n")

print("Your final score is:", score, "/ 3")
print("Thanks for playing!")
