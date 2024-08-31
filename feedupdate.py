import feedparser, datetime
import os

# get the environment variable in windows
LINE_TOKEN = os.environ.get('LINE_TOKEN')


RSS_URLS_FILE = 'feed_url.txt'

def get_rss_urls():
    # read rss urls from file
    with open(RSS_URLS_FILE, 'r') as f:
        rss_urls = f.read().splitlines()
    return rss_urls

def get_last_checked_time():
    # check if the file exists
    if os.path.exists('last_checked_time.txt'):
        with open("last_checked_time.txt", "r") as f:
            return datetime.datetime.fromisoformat(f.read().strip())

    return None

def save_last_checked_time(last_checked_time):
    with open("last_checked_time.txt", "w") as f:
        f.write()

def check_rss_feeds():
    rss_urls = get_rss_urls()
    last_checked = get_last_checked_time()
    last_date = last_checked

    for rss_url in rss_urls:
        feed = feedparser.parse(rss_url)

        new_entries = []

        for entry in feed['entries']:
            published = datetime.datetime.fromtimestamp(datetime.datetime.strftime(entry.published, "%Y-%m-%d %H:%M:%S").timestamp())

        if published > last_checked:
            new_entries.append(entry.link)
            if published > last_date:
                last_date = published
        
        if new_entries:
            for url in new_entries:
                print(url)

    if last_date > last_checked:
        save_last_checked_time(last_date)

        print(new_entries)