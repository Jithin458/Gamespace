from manage import login, games


highscore1 = 0
highscore2 = 0
highscore3 = 0
current_score = 0


def guest_view():
    global highscore1, current_score, highscore2, highscore3
    print('+' + '='*80 + '+')
    print('','\n')
    print(' '*70,'User:guest')
    print('''

(1) Games
(2) Login
(3) quit
          
          ''')
    while True:
        inp = input('>>>')
        if inp.isdigit():
            inp = int(inp)
            if inp == 2:
                login()
                break
            elif inp ==3:
                break
            elif inp == 1:
                print('+' + '='*80 + '+')
                print('','\n')
                print(' '*70,'User:guest')
                
                while True:
                    print('''
                  
(1) Rock Paper Scissors
(2) XOX
(3) Guess the colour
(4) Back
                
                ''')
                    inp = input('>>>')
                    if inp.isdigit():
                        inp = int(inp)
                        if inp == 1:
                            highscore1 = games(1,highscore1)
                        elif inp == 2:
                            highscore2 = games(2,highscore2)
                        elif inp == 3:
                            highscore3 = games(3,highscore3)
                        elif inp == 4:
                            print('+' + '='*80 + '+')
                            print('','\n')
                            print(' '*70,'User:guest')
                            print('''

(1) Games
(2) Login
(3) quit
          
                                ''')
                            break
            
    print('+' + '='*80 + '+')
    


