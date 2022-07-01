import requests
from bs4 import BeautifulSoup as bs
import os

url1 = 'https://www.reddit.com/r/memes/'

page = requests.get(url1)
soup = bs(page.text, 'html.parser')

img = soup.findAll('img')
if not os.path.exists('memes'):
    os.makedirs('memes')

os.chdir('memes')

img_no = 0

for image in img:
    try:
        url = image['src']
        source = requests.get(url1)
        if source.status_code == 200:
            with open('meme-' + str(img_no) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close
                img_no += 1
    
    except:
        pass
