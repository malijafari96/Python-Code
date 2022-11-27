n = int(input())
dehkhoda = {}
for i in range(0, n):
    a = input().split()
    for j in range(1, len(a)):
        dehkhoda[a[j]] = a[0]

final = []
text = input().split()
for i in range(0, len(text)):
    if text[i] in dehkhoda.keys():
        final.append(dehkhoda[text[i]])
    else:
        final.append(text[i])

translate = ''
for item in final:
    translate += item + ' '


print(translate)
