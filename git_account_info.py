#WRITTEN BY MR.DIPTO
#FOLLOW MY GITHUB : https://github.com/MR-DIPTO-143
from os import system as c
try:
    import requests
except:
    c('pip install requests')
user_input=input(' ENTER GITHUB USERNAME : ')
url=f'https://api.github.com/users/{user_input}'
req=requests.get(url).json()
print(' USER : ',req['login'])
print(' NAME : ',req['name'])
print(' BIO  : ',req['bio'])
print(' ID   : ',req['id'])
print(' FOLLOWERS  : ',req['followers'])
print(' FOLLOWING  : ',req['following'])
print(' AVATAR URL : ',req['avatar_url'])
