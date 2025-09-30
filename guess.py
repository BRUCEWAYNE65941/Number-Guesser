import random

def play_game():
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
                if guess_count == 3:  # Provide hint after 3 guesses
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
