import re
email = input()
if re.search(r'.+\@.+\..{2,3}',email) == None :
    print ('WRONG')
else : 
    print ('OK')