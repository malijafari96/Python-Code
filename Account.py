import mysql.connector
import re
cnx = mysql.connector.connect(
    user='root', password='', host='127.0.0.1', database='Account')
cursor = cnx.cursor()
email = input('please enter your email: ')

if re.search(r'.+\@.+\..{2,3}', email) == None:
    print('a valid email has to be like this :expretion@string.string')
    email = input('please enter your email again: ')

password = input('please enter your password: ')
cursor.execute('INSERT INTO information VALUES(\'%s\',\'%s\')' %
               (email, password))
cnx.commit()
cursor.close()
cnx.close()
