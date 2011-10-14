'''This class processes image tags from a website and downloads those images using the webImage class.''' 

__author__ = 'Stephen'
__version__ = '1.0'

from webImages_pkg import webImages
import sys



def main():
    '''Executes commands from the webImage class.'''
    nytimes = webImages(sys.argv[1])
    nytimes.parse_file()
    nytimes.download_images()

if __name__=='__main__':
    main()
