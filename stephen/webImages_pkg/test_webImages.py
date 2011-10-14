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
        HTML = '''<img width="119" height="82" usemap="#cnn_hdrimap" alt="CNN" src="http://i.cdn.turner.com/cnn/.element/img/3.0/main/blackout/hdr-main-bk.gif">'''
        result=my_webImages.parse_file(HTML)
        self.assertEqual(result,"i.cdn.turner.com/cnn/.element/img/3.0/main/blackout/hdr-main-bk.gif")
    def test_download_images(self):
        '''This function tests the downloading of images.'''
        pass
    def tear_down(self):
        '''No tear down.'''
        pass

if __name__ == '__main__':
    unittest.main()
