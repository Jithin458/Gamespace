import mysql.connector
from time import sleep

#Global variable===========================================================

'''password for mysql connector'''
pswd = 'adhidev'

#==========================================================================


def current_user(username = None ):
    if username != None:
        file_object = open('current_user.txt', 'w')
        file_object.write(username)
    else :
        file_object = open('current_user.txt', 'r')
        username = file_object.read()
    
    file_object.close() 
    return(username.replace('\n',''))

#==========================================================================


def up_data(tname, column_names, value,username=''):
    if username == '':
        username = current_user()
    mydb = mysql.connector.connect(host="localhost", user ="root", passwd=pswd, database='accountinfo')
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE " + tname +" SET " + column_names +" = "+ value +" where username = '" + username + "'" )
    mydb.commit()
    mycursor.close()
    mydb.close()

#==========================================================================


def getdata(tname, column_names, condition = ""):
    mydb = mysql.connector.connect(host="localhost", user ="root", passwd=pswd, database='accountinfo')
    mycursor = mydb.cursor()
    mycursor.execute("select " + column_names + " from " + tname + " "+ condition)
    res=mycursor.fetchall()
    return res
    mycursor.close()
    mydb.close()

#==========================================================================


def title():
    file_object = open('title.txt', 'r')
    txt = 'adad'
    while txt != '':
        txt = file_object.readline()
        if txt == '\n':
            continue
        sleep(0.5)
        print(txt.replace('\n',''))
    file_object.close() 

def line():
    print('+'+'='*65+'+')

def breaker():
    a = 3/0

#==========================================================================