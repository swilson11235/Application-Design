'''This class tests the cache class.'''

__author__ = 'Stephen'
__version__ = '1.0'

from caches import caches
import unittest,os, sqlite3


class test_caches(unittest.TestCase):
    def setUp(self):
        '''Create an instance of the cache object.'''
        self.my_caches = caches('','test.db', 'n')

    def test_add_url(self):
        '''This function tests the add_url function.'''
        self.my_caches.add_url('Http://www.xkcd.com')
        output = self.my_caches.read_cache('''select time from cache''')
        output = self.my_caches.read_cache('''select count(*) from cache''')
        self.assertTrue(output==1)
        
    def tearDown(self):
        '''No tear down.'''
        pass
        
if __name__ == '__main__':
    unittest.main()
