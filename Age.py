# input has to be like this : yyyy/mm/dd
from datetime import date

birthday = input().split('/')
if (int(birthday[1]) > 12) or (int(birthday[2]) > 31):
    print('WRONG')
else:
    today = date.today()
    age = today.year - \
        int(birthday[0]) - ((today.month, today.day)
                            < (int(birthday[1]), int(birthday[2])))
    print(age)
