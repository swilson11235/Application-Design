'''This class tests the webImages class.'''

__author__ = 'Stephen'
__version__ = '1.0'

from webImages import webImages
import unittest,os
my_webImages = webImages()

class test_webImages(unittest.TestCase):
    def set_up(self):
        '''No set-up.'''
        pass
    def test_parsefile(self):
        '''This function tests the parsing of html.'''
        HTML = '''<img width="119" height="82" usemap="#cnn_hdrimap" alt="CNN" src="http://i.cdn.turner.com/cnn/.element/img/3.0/main/blackout/hdr-main-bk.gif">'''
        result=my_webImages.parse_file(HTML)
        self.assertEqual(result[0],"http://i.cdn.turner.com/cnn/.element/img/3.0/main/blackout/hdr-main-bk.gif")
    def test_download_images(self):
        '''This function tests the downloading of images.'''
        HTML = '''<img width="119" height="82" usemap="#cnn_hdrimap" alt="CNN" src="http://i.cdn.turner.com/cnn/.element/img/3.0/main/blackout/hdr-main-bk.gif">'''
        my_webImages.parse_file(HTML)
        my_webImages.download_images("tmp")
        self.assertTrue(os.access("0.gif",os.F_OK))
        os.remove("0.gif")
        os.chdir("..")
        os.rmdir("tmp")
        

    def tear_down(self):
        '''No tear down.'''
        pass

if __name__ == '__main__':
    unittest.main()
