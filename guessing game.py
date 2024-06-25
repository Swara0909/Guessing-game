import random

def guessing_game():

    x=int(input("enter the starting range of number: "))
    y= int (input("enter the ending range of number: "))

    for i in range(x,y):
        random_number = random.randint(x,y)
        guess_count=0

    while True:
        guess = int(input(f"Guess the number between {x} and {y}: "))
        guess_count += 1
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {guess_count} guesses.")
            print("Want to play again?")
            break

# Start the game
guessing_game()