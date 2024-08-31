import feedparser, datetime
import os
from datetime import timezone
# send message to line notify
from songline import Sendline

# get the environment variable in windows
LINE_TOKEN = os.environ.get('LINE_TOKEN')


RSS_URLS_FILE = 'feed_url.txt'
LAST_CHECK_TIME = 'last_checked_time.txt'

def get_rss_urls():
    # read rss urls from file
    with open(RSS_URLS_FILE, 'r') as f:
        rss_urls = f.read().splitlines()
    return rss_urls

def get_last_checked_time():
    # check if the file exists
    if os.path.exists(LAST_CHECK_TIME):
        with open(LAST_CHECK_TIME, "r") as f:
            return datetime.datetime.fromisoformat(f.read().strip()).replace(tzinfo=timezone.utc)

    return None

def save_last_checked_time(last_checked_time):
    with open(LAST_CHECK_TIME, "w") as f:
        f.write(last_checked_time.isoformat())

def check_rss_feeds():
    rss_urls = get_rss_urls()
    last_checked = get_last_checked_time()
    last_date = last_checked

    for rss_url in rss_urls:
        feed = feedparser.parse(rss_url)

        new_entries = []

        for entry in feed['entries']:
            format_str = "%a, %d %b %Y %H:%M:%S %z"
            published = datetime.datetime.strptime(entry.published, format_str)
 

            if published > last_checked:
                new_entries.append(entry.link)
                if published > last_date:
                    last_date = published
        msg = ''
        if new_entries:
            for url in new_entries:
                msg += url + '\n'

    bot_line = Sendline(LINE_TOKEN)
    bot_line.sendtext(msg)
        

    if last_date > last_checked:
        save_last_checked_time(last_date)

        print(new_entries)


if __name__ == '__main__':
    check_rss_feeds()