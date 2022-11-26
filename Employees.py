import mysql.connector
cnx = mysql.connector.connect(
    user='root', password='', host='127.0.0.1', database='Employees')

cursor = cnx.cursor()
query = 'SELECT * FROM information'
cursor.execute(query)
dict_high = {}
dict_weight = {}
for (name, high, weight) in cursor:
    dict_high[name] = (high)
    dict_weight[name] = (weight)
dict_high = dict(
    sorted(dict_high.items(), key=lambda item: item[1], reverse=True))
dict_weight = dict(sorted(dict_weight.items(), key=lambda item: item[1]))
list_high = dict_weight.values()
list_weight = dict_weight.values()

for key in dict_high:
    dict_high[key] = (dict_high[key], dict_weight[key])
nummber = list(dict_high.keys())
nummber = len(nummber)
list_info = []
for key in dict_high:
    list_info.append((key, dict_high[key][0], dict_high[key][1]))
list_info = sorted(list_info, key=lambda item: item[1], reverse=True)

for i in list_info:
    print(i)


cursor.close()
cnx.close()
