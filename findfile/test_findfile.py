'''Recursively finds files from a directory according to a search parameter (with test functions).'''
__author__ = 'Stephen'
__version__ = '1.0t'

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

def test_findfile():
    ''' Tests the findfile function by creating a few .py files and searching for a single one (tmp/1.py).'''
    os.mkdir("tmp")
    os.system("touch tmp/1.py tmp/2.py")
    data = findfile("1.py", "tmp")
    os.remove("tmp/1.py")
    os.remove("tmp/2.py")
    os.rmdir("tmp")
    assert data == ["tmp/1.py"]

def test_findnone():
    ''' Tests if the findfile function finds no files when there are none to find.'''
    data = findfile("notarealfile12324.txt", "./")
    assert data == []

if __name__ == '__main__':
    test_findfile()
    test_findnone()

