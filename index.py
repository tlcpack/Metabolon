import feedparser
import datetime
import re

# *Task*: Given a Dictionary keyed by Company and valued by RSS feed url, write a function that determines which companies had no activity for a given number of days.
# *Hints*:
# • Some companies might have more than one feed.
# • Our code has unit tests.
# • Our code is made in incremental commits and with meaningful comments.
# • Reply with questions if necessary, or document assumptions used to make progress.

test_dict = {
    'Diane Rehm' : ['https://dianerehm.org/rss/npr/dr_podcast.xml'],
}

_my_date_pattern = re.compile(
    r'(\d{,2})/(\d{,2})/(\d{4}) (\d{,2}):(\d{2}):(\d{2})')

def myDateHandler(aDateString):
    """parse a UTC date in MM/DD/YYYY HH:MM:SS format"""
    month, day, year, hour, minute, second = \
        _my_date_pattern.search(aDateString).groups()
    return (int(year), int(month), int(day), \
        int(hour), int(minute), int(second), 0, 0, 0)

feedparser.registerDateHandler(myDateHandler)


rss = feedparser.parse('https://dianerehm.org/rss/npr/dr_podcast.xml')
print(rss.feed.published)

print(datetime.datetime.now())