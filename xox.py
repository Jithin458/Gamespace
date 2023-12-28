from x0xmod import xox_game
from time import sleep

life = 3
current = 0 
def xox():
    print(' '*int((52 - len('XOX'))/2)+'XOX')
    print('+' + 50*'=' + '+','\n')
    print()
    print('''
  
  type cancel to exit
  you have 3 life
  Win  = +20 Points +1 Life
  tie  = -5  Points
  lose = -10 Points 
          ''')
    
    global life ,current
    try:
        while life != 0:
            
            print(' '*int((52 - len('XOX'))/2)+'XOX')
            print('+' + 50*'=' + '+','\n')
            print('Life','* '*life) 
            t = xox_game()
            life -= 1
            if t == 20:
                print("+1  Life")
                life += 1
                print('+20 Points')
            if t < 0:
                print(str(t),'Points')
            current += t
            sleep(3)
      
    except ZeroDivisionError:
        print()
        print('game closed')
        print()
    return current
