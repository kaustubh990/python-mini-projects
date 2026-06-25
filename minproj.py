import random 
targetNum = random.randint(1, 100) 
while True:
    userNum = int(input("Guess the number between 1 and 100: "))
    if userNum==targetNum:
        print("Congratulations! You guessed the number correctly.")
        break
    elif userNum<targetNum:
        print("Too low! Try again.")
    else:        print("Too high! Try again.")






