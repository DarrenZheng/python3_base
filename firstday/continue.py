while  True:
    guess = input("input something")
    if guess == 'quit':
        break
    if len(guess) < 3:
        continue
    print("bigger than 2")

print("done!")