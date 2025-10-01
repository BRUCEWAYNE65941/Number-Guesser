import random

def show_instructions():
    print("Welcome to the Number Guessing Game!")
    print("------------------------------------")
    print("Rules:")
    print("- Guess a number between 1 and 100.")
    print("- You'll get feedback if your guess is too high or too low.")
    print("- After 3 guesses, you'll receive a hint about whether the number is even or odd.")
    print("- Try to guess the number in as few tries as possible!")
    print("------------------------------------\n")

def play_game():
    show_instructions()
    number = random.randint(1, 100)
    guess = None
    guess_count = 0

    while guess != number:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            guess_count += 1
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
            elif guess < number:
                print("Too low!")
                if guess_count == 3:
                    print(f"Hint: The number is {'even' if number % 2 == 0 else 'odd'}.")
            elif guess > number:
                print("Too high!")
                if guess_count == 3:
                    print(f"Hint: The number is {'even' if number % 2 == 0 else 'odd'}.")
        except ValueError:
            print("Please enter a valid integer!")
    print(f"Congratulations! You guessed the number in {guess_count} tries!")
    return guess_count

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
