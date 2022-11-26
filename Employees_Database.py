import mysql.connector
cnx = mysql.connector.connect(
    user='root', password='', host='127.0.0.1', database='Employees')
cursor = cnx.cursor()
name = input('please enter your name: ')
height = int(input('please enter your height: '))
weight = int(input('please enter your weight: '))
cursor.execute('INSERT INTO information VALUES(\'%s\',\'%i\',%i)' %
               (name, height, weight))
cnx.commit()
cursor.close()
cnx.close()
