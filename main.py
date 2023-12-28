from manage_dbase import current_user, line, title
from manage import login, sign_in
from account_view import logged_in
from guest_view import guest_view



while True:
    line ()                                                                
    print("Welcome to                                              To Close(X)")
    title()                    
    print('                      Press Any Key \n')
    print()
    line()
    inp = input('>>>')
    if inp.lower() == 'x':
        break
    while True:
        try:
            if current_user() != '':
                logged_in()
                break
            else:
                while True:
                    print()
                    line()
                    print('''
                            
                (1) Login                            #GAME
                (2) Sign in                           -SPACE 
                (3) sign in as guest
                (4) Quit

                ''')
                    while True:
                        inp = input('>>>')
                        if inp.isdigit():
                            inp = int(inp)
                            break
                    if inp == 4:
                        a = 10/0
                    if inp == 1:
                        login()
                        break
                    elif inp == 2:
                        sign_in()
                        break
                    elif inp == 3:
                        guest_view()
                        break
        except ZeroDivisionError:
            line()
            print()
            break      
                        

    