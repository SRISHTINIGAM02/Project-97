import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9):")

while chances > 5:

    guess = int(input("Enter your guess:- "))
    if guess == number:
        print("Congratulations You Won!!!")
        break

        elif guess < number:
            print("Your Guess Was Too Low: Guess a number greater than", guess)

            else:
                print("Your Guess Was Too High: Guess A Number Lesser Than",guess)

                chances += 1

                if not chances< 5:
                    print("You Lose!! The Number is", number)