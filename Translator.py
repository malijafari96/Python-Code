n = int(input())
translator = {}
for i in range(0, n):
    a = input().split()
    for j in range(1, len(a)):
        translator[a[j]] = a[0]

final = []
text = input().split()
for i in range(0, len(text)):
    if text[i] in translator.keys():
        final.append(translator[text[i]])
    else:
        final.append(text[i])

translate = ''
for item in final:
    translate += item + ' '


print(translate)
