import re

def valid_password(password):
        if len(password) < 7:
            return False
        elif re.search('[0-9]',password) is None:
            return False
        elif re.search('[A-Z]',password) is None: 
            return False
        elif re.search('[a-z]',password) is None: 
            return False
        else:
            return True
