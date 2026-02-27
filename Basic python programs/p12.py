
import random

Lowest_num= 1
highest_num=100
answer = random.randint(Lowest_num,highest_num)
guesses=0
is_running=True

print("Number guessing game!")
print(f"Select Number between {Lowest_num} and  {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess=int(guess)
        guesses += 1

        if guess>highest_num or guess<Lowest_num:
            print("That is our of range")
            print(f"Select Number between {Lowest_num} and  {highest_num}")
        elif guess<answer:
            print("To Low! Please try again!")
        elif guess>answer:
            print("To High! Please try again!")
        else:
            print("Correct guess!!")
            print(f"The answer was {answer}")
            print(f"Total number of guesses required: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Select Number between {Lowest_num} and  {highest_num}")
       
