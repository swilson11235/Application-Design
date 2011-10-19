'''This class tests the cache class.'''

__author__ = 'Stephen'
__version__ = '1.0'

from caches import caches
import unittest,os, sqlite3

my_caches = caches('','test.db', 'n')
class test_caches(unittest.TestCase):
    def set_up(self):
        '''Create an instance of the cache object.'''
        pass
    def test_add_url(self):
        '''This function tests the add_url function.'''
        my_caches.add_url('Http://www.xkcd.com')
        output = my_caches.read_cache('''select time from cache''')
        output = my_caches.read_cache('''select count(*) from cache''')
        self.assertTrue(output==1)
        
    def tear_down(self):
        '''No tear down.'''
        pass
        
if __name__ == '__main__':
    unittest.main()
