person = input()
dict_people = {}
while person != '-1':
    name = person.split()[0]
    hight = person.split()[1]
    dict_people[name] = hight
    person = input()

max_hight = max(dict_people.values())
min_hight = min(dict_people.values())

for name in dict_people:
    if dict_people[name] == max_hight:
        print(f'{name} is the highest')
    if dict_people[name] == min_hight:
        print(f'{name} is the shortest')
