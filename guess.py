import random

def show_instructions(min_num, max_num, max_guesses):
    print("Welcome to the Number Guessing Game!")
    print("------------------------------------")
    print("Rules:")
    print(f"- Guess a number between {min_num} and {max_num}.")
    print(f"- You have up to {max_guesses} guesses.")
    print("- You'll get feedback if your guess is too high or too low.")
    print("- After 3 guesses, you'll receive a hint about whether the number is even or odd.")
    print("- Try to guess the number in as few tries as possible!")
    print("------------------------------------\n")

def choose_difficulty():
    print("Choose difficulty: 1) Easy (1-50, 10 guesses), 2) Medium (1-100, 7 guesses), 3) Hard (1-200, 5 guesses)")
    while True:
        try:
            choice = int(input("Enter 1, 2, or 3: "))
            if choice == 1:
                return 1, 50, 10
            elif choice == 2:
                return 1, 100, 7
            elif choice == 3:
                return 1, 200, 5
            else:
                print("Please choose 1, 2, or 3!")
        except ValueError:
            print("Enter a valid number!")

def play_game():
    min_num, max_num, max_guesses = choose_difficulty()
    show_instructions(min_num, max_num, max_guesses)
    number = random.randint(min_num, max_num)
    guess = None
    guess_count = 0

    while guess != number and guess_count < max_guesses:
        try:
            guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
            guess_count += 1
            if guess < min_num or guess > max_num:
                print(f"Please enter a number between {min_num} and {max_num}!")
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
    if guess == number:
        print(f"Congratulations! You guessed the number in {guess_count} tries!")
    else:
        print(f"Game over! The number was {number}.")
    return guess_count

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
