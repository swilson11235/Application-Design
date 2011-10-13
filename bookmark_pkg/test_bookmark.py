''' This class allows for testing of the bookmark class.'''

__author__ = 'Stephen'
__version__ = '1.0'

from bookmark import bookmark
import unittest

class test_bookmark(unittest.TestCase):
    def set_up(self):
        pass
    def test_getName(self):
        '''Tests if an arbitrary name in a bookmark is correct.'''
        self.name = 'Ubuntu'
        my_bookmark = bookmark(self.name,'URL','Time')
        self.get_name = my_bookmark.getName()
        self.assertEqual(self.get_name,self.name)
    def test_setName(self):
        '''Tests the changing of a bookmark name.'''
        my_bookmark = bookmark('Name','URL','time')
        my_bookmark.setName('Bob')
        self.assertEqual(my_bookmark.getName(),'Bob')
    def test_setURL(self):
        '''Tests the changing of a bookmark name.'''
        my_bookmark = bookmark('Name','URL','time')
        my_bookmark.setURL('Bob')
        self.assertEqual(my_bookmark.getURL(),'Bob')
                    
    def test_getURL(self):
        '''Tests if an arbitrary URL in a bookmark is correct.'''
        self.URL = 'http://www.ubuntulinux.org/' 
        my_bookmark = bookmark('name',self.URL,'time')
        self.get_URL = my_bookmark.getURL()
        self.assertEqual(self.get_URL,self.URL)

    def test_getTime(self):
        '''Tests if an arbitrary time in a bookmark is correct.'''
        self.time = '1181129907'
        my_bookmark = bookmark('name', 'URl', self.time)
        self.get_time = my_bookmark.getTime()
        self.assertEqual(self.get_time, self.time)
        
    def tear_down(self):
        pass

if __name__ == '__main__':
    unittest.main()
