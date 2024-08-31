# feed parser basic 101

import feedparser
from pprint import pprint

url = 'http://hnrss.org/frontpage'

feed = feedparser.parse(url)


for entry in feed['entries']:
    pprint(entry.title)
    pprint(entry.published)

