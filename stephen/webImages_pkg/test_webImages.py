'''This class tests the webImages class.'''

__author__ = 'Stephen'
__version__ = '1.0'

from webImages import webImages
import unittest
my_webImages = webImages()

class test_webImages(unittest.TestCase):
    def set_up(self):
        '''No set-up.'''
        pass
    def test_parsefile(self):
        '''This function tests the parsing of html.'''
        pass
    def test_download_images(self):
        '''This function tests the downloading of images.'''
        pass
    def tear_down(self):
        '''No tear down.'''
        pass

if __name__ == '__main__':
    unittest.main()
