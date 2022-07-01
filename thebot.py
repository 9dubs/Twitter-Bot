from PIL import Image
import tweepy as tp
import os
import time

api_key = 'YOUR-API-KEY'
api_secret = 'YOUR-API-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-TOKEN-SECRET'

auth = tp.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('memes')

for meme in os.listdir('.'):
    img = Image.open(meme)
    if img.width >= 640:
        api.update_status_with_media('memes', meme)
        time.sleep(10)
    else:
        pass
    

