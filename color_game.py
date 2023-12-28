import random
from manage_dbase import line


def color_game():
    line()
    print()
    colors = [ "blue   ", "black  ", "green  ", "red    ", "yellow " , "violet ", "green  " , "white  " , "pink   "]
    user_points = 0
    computer_points = 0
    

    while True:
        a = 0 
        for i in colors:
            a += 1
            if a in [4,7]:
                print()
            print('('+str(a)+')',i.title(),end =" ")
        print()
        choice = input("Select your choice (or type 'exit' to end the game): ")
        
        if choice.lower() == 'exit':
            break

        computer_choice = random.choice(colors)
        print("Computer's answer is:", computer_choice)
        
        if choice.isdigit():
            if colors[int(choice)] == computer_choice.lower():
                user_points += 1
                print("You won!!")
        else:
            computer_points += 1
            print("Sorry, try again..")
        
        print()
        print("Your points:", user_points)
        print("Computer points:", computer_points)
        print()

    print("Game over. Your final score:", user_points)
    print()
    line()
    return user_points
