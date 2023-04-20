"""
this app checks if an email is valid or not
"""

import re

email = input()
if re.search(r'.+\@.+\..{2,3}', email) is None:
    print('Not Valid')
else:
    print('Valid')
