import feedparser
import datetime

# *Task*: Given a Dictionary keyed by Company and valued by RSS feed url, write a function that determines which companies had no activity for a given number of days.
# *Hints*:
# • Some companies might have more than one feed.
# • Our code has unit tests.
# • Our code is made in incremental commits and with meaningful comments.
# • Reply with questions if necessary, or document assumptions used to make progress.

test_dict_1 = {
    'Diane Rehm' : ['https://dianerehm.org/rss/npr/dr_podcast.xml'],
    'Bill Maher' : ['http://billmaher.hbo.libsynpro.com/rss'],
    'NYT' : ['https://rss.nytimes.com/services/xml/rss/nyt/US.xml', 'https://rss.nytimes.com/services/xml/rss/nyt/Business.xml', 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml']
    
}

test_dict_2 = {
    'Diane Rehm' : ['https://dianerehm.org/rss/npr/dr_podcast.xml'],
    'Bill Maher' : ['http://billmaher.hbo.libsynpro.com/rss'],
    'NYT' : ['https://rss.nytimes.com/services/xml/rss/nyt/US.xml', 'https://rss.nytimes.com/services/xml/rss/nyt/Business.xml', 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml'],
    'MTP' : ['http://podcastfeeds.nbcnews.com/meetthepress']
    
}
def Activity_test (feed, days):
    sample = []
    for blogs in feed:
        for blog in feed[blogs]: 
            rss = feedparser.parse(blog)
            parsed_date = rss.entries[0].published_parsed
            month = parsed_date.tm_mon
            day = parsed_date.tm_mday
            year = parsed_date.tm_year

            days_since = datetime.date.today() - datetime.date(year, month, day)
            if days_since.days > days:
                sample.append(blogs)
    print(f"The RSS feeds with the requested inactivity are: {sample}")
    return sample

def get_day_request():
    while True:
        user_input = input("How many days of inactivity should we check for? ")
        if user_input.isnumeric():
            guess = int(user_input)
            return guess
        print("Oops, that input was invalid")


days = get_day_request()
x = Activity_test(test_dict_1, days)
y = Activity_test(test_dict_2, days)
