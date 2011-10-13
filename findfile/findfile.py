'''Recursively finds files from a directory according to a search parameter.'''
__author__ = 'Stephen'
__version__ = '1.0'

import os
import sys

def findfile(search, path):
    ''' This function finds files according to the search parameter and returns a list of those files.'''
    myfiles = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.find(search) != -1:
                myfiles.append(str(root + os.sep + file))
    return myfiles

if __name__ == '__main__':
    findfile(sys.argv[2], sys.argv[1])
