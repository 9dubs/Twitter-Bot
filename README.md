# Twitter-Bot
A simple Twitter bot that essentially grabs memes(images) from Reddit(r/memes) and uploads it in the Twitter profile, at an interval of 10s

Please install the following dependencies:

Python module to send HTTP requests:

```
pip install requests
```

BeautifulSoap, a Python module to scrap images from websites

```
pip install bs4
```

Tweepy, open source Python library to access the Twitter API

```
pip install tweepy
```

Run the get-memes.py file first.

This would create a local folder in your computer to store the scrapped images from website (Reddit, in this case).

then run thebot.py file to post images.

In case of tweepy.errors.Forbidden 403 errors, please check your api credentials and verify if you have turned OAuth 1.0a on, on your twitter app settings in the developer portal, with read and write mode selected and required details filled.
