


email = input('whats your email? ').strip()

"""
username , domain = email.split('@')

#if (username) and ('.' in domain):
if (username) and (domain.endswith('.com')):
    # if username in email has at least one caracter it will be True
    print('valid')
else:
    # if username has no caracter it will be False
    print('invalid')
    
    """
    
import re

if re.search(r"^(\w|\S)+@(\w|\s)+\.(com|org|gov|edu)$", email, re.IGNORECASE):
    print('valid')
else:
    print('invalid')
    
    
    
