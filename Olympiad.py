n = int(input('please enter number of Participants: '))
list_people = []
list_empty = []
for i in range(n):
    list_people.append(input('please enter your information: ').split('.'))
for i in list_people:
    if i[0] == 'f':
        print(i[0], i[1].capitalize(), i[2])
for i in list_people:
    if i[0] == 'm':
        print(i[0], i[1].capitalize(), i[2])
