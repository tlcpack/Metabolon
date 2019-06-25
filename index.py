import feedparser
import datetime

# *Task*: Given a Dictionary keyed by Company and valued by RSS feed url, write a function that determines which companies had no activity for a given number of days.
# *Hints*:
# • Some companies might have more than one feed.
# • Our code has unit tests.
# • Our code is made in incremental commits and with meaningful comments.
# • Reply with questions if necessary, or document assumptions used to make progress.

test_dict = {
    'Craigslist' : ['https://www.craigslist.org/about/best/all/index.rss'],
}

print(test_dict)