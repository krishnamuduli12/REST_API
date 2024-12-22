import random

n =20
to_be_guessed = int(n * random.random()) + 1

guess = 0
while guess != to_be_guessed:
    num = input("Enter the guessed number: ")
    guess = int(num)
    
    if guess > 0: 
        if guess > to_be_guessed:
            print("Number is long large !!!")
        elif guess < to_be_guessed:
            print("Number is too small")
    else:
        print("Sorry you are giving up")
        break
else:
    print("Congratulation you made it")
