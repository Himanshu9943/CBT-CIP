import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        print("\nMake your move:")
        print("Rock")
        print("Paper")
        print("Scissors")
        user_input = input("Enter your choice: ").lower()
        if user_input in choices:
            return user_input
        else:
            print(" Oops! That's not a valid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return " It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return " cong.You win!"
    else:
        return " Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        result = determine_winner(user_choice, computer_choice)
        print(f"\nResult: {result}")
        play_again = input("\nWould you like to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print(" Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
