import re
email = input()
if re.search(r'.+\@.+\..{2,3}', email) == None:
    print('Not Valid')
else:
    print('Valid')
