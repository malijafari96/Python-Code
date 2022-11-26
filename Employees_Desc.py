import mysql.connector
cnx = mysql.connector.connect(
    user='root', password='', host='127.0.0.1', database='Employees')

cursor = cnx.cursor()
query = 'SELECT * FROM information;'
cursor.execute(query)
for (name, height, weight) in cursor:
    print('%s is %i cm and %i kg' % (name, height, weight))

cnx.close()
