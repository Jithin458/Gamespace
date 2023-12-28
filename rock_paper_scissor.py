import random

def rockpaperscissors():
    user_points = 15
    computer_points = 15
    print(f"User points: {user_points} | Computer points: {computer_points}")

    def get_user_choice():
        user_choice = input("Choose Rock(r), Paper(p), or Scissors(s) or 'q' to quit: ").lower()
        while user_choice not in ['r', 'p', 's', 'q']:
            print("Invalid choice. Please choose Rock(r), Paper(p), or Scissors s), or 'q' to quit.")
            user_choice = input("Choose Rock(r), Paper(p), or Scissors(s) or 'q' to quit: ").lower()
        return user_choice

    def get_computer_choice():
        return random.choice(['r', 'p', 's'])

    def display_choice_name(choice):
        if choice == 'r':
            return 'Rock'
        elif choice == 'p':
            return 'Paper'
        elif choice == 's':
            return 'Scissors'

    def check_winner(user_choice, computer_choice):
        if user_choice == 'q':
            print("Quitting the game.")
            return 0, 0
        print('-' * 30)
        print(f"You chose {display_choice_name(user_choice)}.")
        print(f"The computer chose {display_choice_name(computer_choice)}.")

        if user_choice == computer_choice:
            print("It's a draw! You both get -5 points.")
            return -5, -5
        elif (user_choice == 'r' and computer_choice == 's') or \
             (user_choice == 'p' and computer_choice == 'r') or \
             (user_choice == 's' and computer_choice == 'p'):
            print("You win! You get +5 points.")
            return 5, -5
        else:
            print("Computer wins! You lose -5 points.")
            return -5, 5
    def final_score(user_points,computer_points):
        print("Game over.")
        if user_points > computer_points:
            print("Congratulations! You won!")
        elif user_points < computer_points:
            print("You lost. Better luck next time!")
        else:
            print("It's a draw! Good game!")
        print('+'+'=' * 50+'+')
        print("Final Scores:")
        print(f"User points: {user_points} | Computer points: {computer_points}")
        print('+'+'=' * 50+'+')

    while user_points > 0 and computer_points > 0:
        print('+'+'=' * 50+'+')
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        ru, rc = check_winner(user_choice, computer_choice)
        user_points += ru
        computer_points += rc
        if user_choice == 'q':
            final_score(user_points,computer_points)
            return user_points
            
        
        if user_points <= 0 or computer_points <= 0:
            final_score(user_points,computer_points)
            return user_points
        else:
            print('+'+'=' * 50+'+')
            print(f"Total points - User: {user_points} | Computer: {computer_points}")

            
         
           

    




