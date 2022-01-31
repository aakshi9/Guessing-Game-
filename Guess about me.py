# Question 1 - Age
num_of_attempts = 4
answer = 20
guess = int(input("How old do you think aakshi is?"))
for i in range(3):
    if guess == answer:
        print("YAY! You got it!")
        break 
    elif guess > answer:
        print("Woah that's a little too high")
        num_of_attempts -= 1
        guess = int(input("How old do you think aakshi is?"))
    elif guess < answer:
        print("Woah that's too low")
        num_of_attempts -= 1
        guess = int(input("How old do you think aakshi is?"))
    print()
    
# Question 2 - Birthday Month
num_of_attempts = 4
answer = 9
guess = int(input("What is aakshi's birthday month?"))
for i in range(3):
    if guess == answer:
        print("YAY! You got it!")
        break 
    elif guess > answer:
        print("Woah that's a little too high")
        num_of_attempts -= 1
        guess = int(input("What is aakshi's birthday month?")) 
    elif guess < answer:
        print("Woah that's too low")
        num_of_attempts -= 1
        guess = int(input("What is aakshi's birthday month?")) 
    print()

# Question 3 - Duration in Canada
num_of_attempts = 4
answer = 15
guess = int(input("How long has aakshi lived in Canada for?"))
for i in range(3):
    if guess == answer:
        print("YAY! You got it!")
        break 
    elif guess > answer:
        print("Woah that's a little too high")
        num_of_attempts -= 1
        guess = int(input("How long has aakshi lived in Canada for?")) 
    elif guess < answer:
        print("Woah that's too low")
        num_of_attempts -= 1
        guess = int(input("How long has aakshi lived in Canada for?")) 
    print()

# Question 4 - Programming Languages (Python, R, Java)
num_of_attempts = 4
answer = 3
guess = int(input("How many programming languages does aakshi know?"))
for i in range(3):
    if guess == answer:
        print("YAY! You got it!")
        break 
    elif guess > answer:
        print("Woah that's a little too high")
        num_of_attempts -= 1
        guess = int(input("How many programming languages does aakshi know?")) 
    elif guess < answer:
        print("Woah that's too low")
        num_of_attempts -= 1
        guess = int(input("How many programming languages does aakshi know?")) 
    print()

# Question 5 - Hobby
num_of_attempts = 4
answer = 13
guess = int(input("How many years of professional experience does aakshi have in dancing?"))
for i in range(3):
    if guess == answer:
        print("YAY! You got it!")
        break 
    elif guess > answer:
        print("Woah that's a little too high")
        num_of_attempts -= 1
        guess = int(input("How many years of professional experience does aakshi have in dancing?")) 
    elif guess < answer:
        print("Woah that's too low")
        num_of_attempts -= 1
        guess = int(input("How many years of professional experience does aakshi have in dancing?")) 
    print()
    
