import random
user_choice=int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if user_choice < 0 or user_choice>2:
    print("You entered a Invalid number, You lose.")
else:
    computer_choice= random.randint(0,2)
    print(f"Computer choice: {computer_choice}")
    if computer_choice == user_choice:
        print("It's a draw.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win.")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose.")
    elif computer_choice > user_choice:
        print("you lose.")
    elif user_choice > computer_choice:
        print("you win.")
