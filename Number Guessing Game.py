import random         
print("\nWelcome To The Number Guessing Game")
print("You'll Be Given 3 Chances To Guess The Right Number Between 1 and 10")
print("Let's Test Your Luck Or Maybe Your Intuition")
print("-" * 80)
while True:
    randnum = random.randint(1, 10)
    for i in range(3):
        try:
            guess = int(input(f"Attempt {i+1}/3 - Guess the Number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if randnum == guess:
            print("🎉 You Win!")
            break
        elif guess < randnum:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print(f"😢 Better Luck Next Time! The number was {randnum}")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye")
        break
