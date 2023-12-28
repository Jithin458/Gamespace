from manage_dbase import current_user, getdata, up_data, pswd, line
from xox import xox
from rock_paper_scissor import rockpaperscissors
from color_game import color_game
import datetime
import mysql.connector


#Global variable===========================================================+


#title=====================================================================+




#+==========================================================================+


def sign_in():
    try:
        print('+' + '='*50 + '+')
        print('','\n')
        print('Type cancel to exit sign in process','\n')
        while True:
            same = False
            username = input("UserName :")
            if username == 'cancel':
                breaker()
            a = getdata('users', 'username')
            for i in a:
                if (username,) == i:
                    print('\n',"username alredy taken",'\n')
                    same = True
                    break
            if not same:
                break
        print()

        while True:
            password = input("password :")
            # def break
            if password == 'cancel':
                breaker()
            if len(password) >= 8 :
                break
            else:
                print('\n','Password must me atleast 8 digit long','\n')
        while True:
            print('Re enter password to confirm')
            check_pass = input('password :')
            # def break
            if check_pass == 'cancel':
                breaker()
            if password == check_pass:
                break
            else:
                print('\n',"password does not match",'\n')
        print()
        
        while True:    
            email = input('Email id :')
            # def break
            if email == 'cancel':
                breaker()
            if '@gmail.com' in email:
                a = getdata('info', 'email')
                for i in a:
                    if (email,) == i:
                        print('\n',"email alredy exist",'\n')
                        same = True
                        break
                else:
                    break
            else:
                print('\n',"must have '@gmail.com'",'\n')
        print()

        while True:
            print('Date.O.B : YYYY-MM-DD')
            dob = input('Date.O.B : ')
            # def break
            if dob == 'cancel':
                breaker()
            year = datetime.datetime.now().year
            a = dob.split('-')
            if int(a[0]) <= int(year) and int(a[1]) < 13 and int(a[2]) < 31:
                break
            else:
                print('\n',"enter valid date of birth",'\n') 

        mydb = mysql.connector.connect(host="localhost",user ="root",passwd=pswd,database='accountinfo')
        mycursor = mydb.cursor()
        mycursor.execute("insert into {} values('{}','{}')".format('users',username,password))
        mycursor.execute("insert into {} (username,email,dob) values ('{}','{}','{}')".format('info',username,email,dob))
        mydb.commit()
        mycursor.close()
        mydb.close()
        print('\n','sign in complete now login using this information','\n')
        print('+' + '='*50 + '+')
    except ZeroDivisionError:
        print('\n','sign in process cancelled','\n')
        print('+' + '='*50 + '+')

#==========================================================================#


def login():
    while True:
        print("Login")
        username = input("Username:")
        passwrd = input("Password:")
        res=getdata(tname="users",column_names=" username, password ",condition=f" where username = '{username}'")
        s = input("Enter L to login or Q to quit:")
        if s.lower() == "l":
            if res[0][0]==username and res[0][1] == passwrd:
                current_user(username)
                return True
            else:
                print("Wrong password or username!!!")
                c = int(input("Enter (1) to reset password or (2) to enter details again:"))
                if c == 1:
                    while True:
                        username = input("Username:")
                        res=getdata(tname="users",column_names=" username ",condition=f" where username = '{username}'")
                        if res[0][0]==[]:
                            print("Username doesnt exist")
                            k = input("Enter (1) to enter username again or (2) to start from beginning:")
                            if k  == 1:
                                continue
                            elif k ==2:
                                break
                            else:
                                print("Wrong input")
                        elif res[0][0] == username:
                            reset(username)
                            print("Enter details again")
                            break
                        
        else:
            break

#==========================================================================#


def old_password(old_pass):
    while True:
        old_check = input("Current Password :")
        breaker(old_check)
        if old_pass == old_check:
            return(True)
        
        else:
            print('Password does not match','\n')
         

def old_email(username):
    while True:
        old_check = input('Email Address    :')
        email = (getdata('info','email',"where username ='"+username+"'"))[0][0]
        breaker(email)
        if old_check == email:
            return(True)
        else:
            print('Email does not match','\n')


def breaker(inp):
    if inp.lower() == 'cancel':
            a = 10/0


def repass(username=''):
    if username == '':
        username = current_user()

    print('\n','Password change >>>')
    while True:
        password = input("New password :")
        breaker(password)
        if len(password) >= 8 :
            break
        else:
            print('\n','Password must me atleast 8 digit long','\n')
    while True:
        print('Re enter password to confirm')
        check_pass = input('password :')
        breaker(check_pass)
        if password == check_pass:
            break
        else:
            print('\n',"password does not match",'\n')
    up_data('users','password',"'"+check_pass+"'",username)
    print('\n',"password updated")
    print()
    


# main
def reset(username = ''):
    try:
        usernames = list(getdata('users','username'))
        if (username,) not in usernames + [('',)]:
            print('No account with username',username)
            print('being send to login page ......')
            breaker('cancel')
    
        print()
        print("type Cancel to exit reset protocol",'\n')

        if username == '' :
            username = current_user()
            old_pass = getdata('users','password',"where username ='"+username+"'")[0][0]
            a = old_password(old_pass)
            if a and a!= None:
                repass()
        
        else:
            old_pass = getdata('users','password',"where username ='"+username+"'")[0][0]
            print("Do you remember your old password(P) or email(E)")
            while True:
                a = (input("Enter choice:")).lower()
                breaker(a)
                if a == 'p':
                    b = old_password(old_pass)
                    break
                if a == 'e':
                    b = old_email(username)
                    break
            repass(username)
    except ZeroDivisionError:
        print('\n','Password reset canceled')

#+==========================================================================+

def account():
    line()
    print()
    while True:
        c = int(input('''
                      
(1)Account details
(2)Reset password
(3)Logout
(4)Back                     
>>>'''))
        if c == 1:
            print()
            print("Account information")
            print('-------------------')
            res=getdata(tname="info",column_names=" email, dob, game1h, game2h, game3h",condition= f"where username = '{current_user()}' ")
            print("Username:",current_user())

            for i in res:
                print("Email   :",res[0][0])
                print("D.O.B   :",res[0][1])
                print()
                print('game highscores \n')
                print("Rock Paper :",res[0][2])
                print("XOX        :",res[0][3])
                print("Guess game :",res[0][4])
        elif c == 2:
            reset()
        elif c == 3:
            current_user('')
            a = 10/0
        elif c == 4:
            break
        else:
            print("Wrong input")
    line()
    print()
        
#+==========================================================================+


def games(game_no,high = None):
    if game_no == 1:
        current = rockpaperscissors()
    if game_no == 2:
        current = xox()
    if game_no == 3:
        current = color_game() 
    if high == None:  
        l_display(current,game_no)
    else:
        g_display(high,current,game_no)
    
ga_me = [int((82-len('rock paper scissors'))/2)*' '+'rock paper scissors',
        int((82-len('xox'))/2)*' '+'XOX',
        int((82-len('game 3'))/2)*' '+'Game 3']

def g_display(high,current,game_no):
    print(ga_me[game_no-1])
    print()
    high= display(current,game_no,high)
    print()
    print('+' + '='*80 + '+')
    print()
    return high

def l_display(current,game_no):
    print(ga_me[game_no-1])
    display(current,game_no)



def display(current, game_no, high = None):
    new = False
    username = current_user()
    if high == None:
        high = getdata('info','game'+str(game_no)+'h',"where username ='"+username+"'")
        high = high[0][0]
    if current> high :
        high = current
        if username != '':
            up_data('info','game'+str(game_no)+'h',str(high),username)   
        new = True
     
    
    print('+' + '='*80 + '+')
    print()
    print(    'Current score :',current )
    print('High score    :',high,end=' ')
    if new:
        print('(new record)')
    else:
        print()

    print()
    print('(1) play again : (2) quit ','\n')
    while True:
        inp = input('>>>')
        if inp.isdigit():
            inp = int(inp)
            if inp in [1,2]:
                break
    if high != None:
        if inp == 1:
            if game_no == 1:
                high =games(1,high)
            elif game_no == 2:
                high = games(2,high)
            elif game_no == 3:
                high = games(3,high)
        return(high)
    else:
        if inp == 1:
            if game_no == 1:
                games(1)
            elif game_no == 2:
                games(2)
                print('game2')
            elif game_no == 3:
                games(3)


#+==========================================================================+
def game():
    while True:
        game_no = int(input('''
                            
(1)Rock Paper Scissor
(2)XOX
(3)Guess Game
(4)Back
:'''))
        if game_no == 1:
            games(1)
        elif game_no == 2:
            games(2)
        elif game_no == 3:
            games(3)
        elif game_no == 4:
            break
        else:
            print("Wrong input")

#+==========================================================================+