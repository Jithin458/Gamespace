from random import choice
from time import sleep

''' global variable ----------------------------------------------------------------------------------------------------------'''
slot = [
  1,2,3,
  4,5,6,
  7,8,9]

col = [
  0,0,0, 
  0,0,0,
  0,0,0 ]


item = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]

''' functions ------------------------------------------------------------------------------------------------------'''
def con(z):
  a,b,c,d = z
  if col[a] == col[b] and col[a] == d :
    return(True,c)
  if col[b] == col[c] and col[b] == d:
    return(True,a)
  if col[a] == col[c] and col[a] == d:
    return(True,b)
  else:
    return(False,0)

    
'''---------------------------------------------------------------------------------------------------------------'''
def bot():
  global slot, col
  print('Pc BOT >>>')
  t = False
  for j in ['O','X']:
    if t:
      break
    for i in item:
      t,c = con(i + [j])
      if t:
        if (c+1) in slot:
          pc = c + 1
          slot.remove(pc)
          break
  if not t:
    pc = choice(slot)
    slot.remove(pc)
  col[pc-1] = 'O'
        

'''---------------------------------------------------------------------------------------------------------------'''
def check():
  if col[0] == col[1] and col[0] == col[2] and col[2] != 0:
    return(True,0)
  if col[3] == col[4] and col[4] == col[5]and col[5] != 0:
    return(True,3)
  if col[6] == col[7] and col[8] == col[7]and col[7] != 0:
    return(True,6)
  if col[0] == col[3] and col[3] == col[6]and col[6] != 0:
    return(True,0)
  if col[1] == col[4] and col[4] == col[7]and col[7] != 0:
    return(True,1)
  if col[2] == col[5] and col[5] == col[8]and col[8] != 0:
    return(True,2)
  if col[0] == col[4] and col[4] == col[8]and col[8] != 0:
    return(True,0)
  if col[2] == col[4] and col[4] == col[6]and col[6] != 0:
    return(True,2)
  if len(slot) == 0:
    return('True',99)
  else:
    return(False,0)
  
  
'''---------------------------------------------------------------------------------------------------------------'''
def dis():
  a = 0
  for i in col:
    if a%3 == 0 :
      print('')
      print('+---+---+---+')
      print('! ',end ='')
    if i == 0:
      print('  ! ',end='')
    if i in ['X','O']:
      print(i+' ! ',end='')
    a += 1
  print()
  print('+---+---+---+')
  print()


''' Main ------------------------------------------------------------------------------------------------------'''
def xox_game():
  global slot,col
  slot = [1,2,3,4,5,6,7,8,9]
  col = [0,0,0,0,0,0,0,0,0] 


  print('+' + 50*'=' + '+','\n')
  print('''

  place :
  +---+---+---+
  ! 1 ! 2 + 3 !
  +---+---+---+
  ! 4 ! 5 + 6 !
  +---+---+---+
  ! 7 ! 8 + 9 !
  +---+---+---+

  ''')

  while True:
    while True:
      
      inp = input('Player >>>')
      if inp in 'cancel':
        a = 10/0
      if inp.isdigit():
        inp = int(inp)
      if inp in slot:
        break
    slot.remove(inp)
    col[inp-1] = 'X'
    dis()
    b,c = check()
    if b:
      if c == 99:
        print(' its a tie')
        t = -5
      elif col[c] == 'X':
        print('You won')
        t = 20
      else:
        print('PC won')
        t = -5
      break
    bot()
    dis()
    b,c = check()
    if b:
      if c == 99:
        print(' its a tie')
        t = -5
      elif col[c] == 'X':
        print('You won')
        t = 20
      else:
        print('PC won')
        t = -10
      break
  return t
  
  
  
    
      
