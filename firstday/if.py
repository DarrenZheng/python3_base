number = 90

guess = int(input("enter an integer:"))

if guess == number:
    print("you win")
elif guess > number:
    print("higher")
else :
    print("lower")

print("end!")