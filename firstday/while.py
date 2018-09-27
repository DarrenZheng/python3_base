number = 90
running = True

while running:
    guess = int(input("enter an integer:"))

    if guess == number:
        print("you win")
        running = False
    elif guess > number:
        print("higher")
    else :
        print("lower")

print("end!")