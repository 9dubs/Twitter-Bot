from PIL import Image
import tweepy as tp
import os
import time

api_key = '8IFmSFIMJeBVT5gSolE91KxcM'
api_secret = 'Z6haGDO4tnNxzKeXMzhiIbqrUtLbRcKD4d3conxJjLET98mlhj'
access_token = '1542132473060278272-wK0hkFp7nLLYyOrpjKJpOPDrkfumBD'
access_secret = 'GKhiS4m094PbtlkRi05qcAQ3W5hnJlh9DEAil05kJCBrb'

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

