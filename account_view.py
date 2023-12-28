from manage import line, game, account
from manage_dbase import current_user


def logged_in():
    while True:
        line()
        print('''
                        
    (1)Games
    (2)Account
    (3)Help
    (4)Logout
    (5)Quit
                        
    ''')
        c = int(input('>>>'))
        if c == 1:
            game()
        elif c == 2:
            account()
        elif c == 3:
            file_object = open('help.txt', 'r')
            d = file_object.readlines()
            file_object.close()
            for i in d:
                print(i.replace('\n',''))

        elif c ==4:
            current_user("")
            break
        elif c == 5:
            break
        else:
            print("Wrong input")
    print()
    line()