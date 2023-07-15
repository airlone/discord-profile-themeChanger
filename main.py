import requests
import time
import random

token = '' # your token


while True:
    rand1 = random.randrange(0, 16777215) # creating random color
    rand2 = random.randrange(0, 16777215) # creating random color
    
    clur = [rand1, rand2] # putting them in the format
     # sending request with json data and auth headers with token
    r = requests.patch(f'https://discord.com/api/v9/users/@me/profile', headers={'Authorization': token, 'Content-Type': 'application/json'}, json={'theme_colors': clur})
    if r.status_code == 200:
        print('Changed color') # if it changed, it will print this
       
    elif r.status_code == 429:  # jus a lil rate limit sleep shit
        try:
            time.sleep(r.json()['retry_after'])
        except:
            time.sleep(2)
       
    time.sleep(2) # waiting more cause i don wanna get termed
