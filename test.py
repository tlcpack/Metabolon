import unittest
from index import Activity_test

class TestRSS(unittest.TestCase):

    def test_one(self):
        test_dict = {
        'Diane Rehm' : ['https://dianerehm.org/rss/npr/dr_podcast.xml'],
        'Bill Maher' : ['http://billmaher.hbo.libsynpro.com/rss'],
        'NYT' : ['https://rss.nytimes.com/services/xml/rss/nyt/US.xml', 'https://rss.nytimes.com/services/xml/rss/nyt/Business.xml', 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml']
        }
        x = Activity_test(test_dict, 1)
        self.assertListEqual(x, ['Diane Rehm', 'Bill Maher'])
    

if __name__ == '__main__':
    unittest.main()