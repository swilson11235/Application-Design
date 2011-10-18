'''This program uses the caches class to cache websites.''' 

__author__ = 'Stephen'
__version__ = '1.0'

from caches_pkg import caches
import os

def main():
    '''Executes commands from the caches class.'''
    new_cache = caches('http://www.xkcd.com')
    new_cache.add_url('http://www.nytimes.com')

if __name__=='__main__':
    main()