'''This class processes ''' 

__author__ = 'Stephen'
__version__ = '1.0'

#import webImages
import sys,urllib2

class webImages():
    def __init__(self, sys.arv[1]='www.nytimes.com'):
        '''Initializes the .'''
        self.URL=sys.argv[1]
        self.HTML = self.get_HTML()
    def __add__(self, your_wave):
        ''''''
    def __len__(self):
        '''Returns the number of frames.'''
        return len(self.frames)
    def __str__(self):
        '''Returns a string representation of the class (the frames, in other words data, are in a string).'''
        return str(self.frames)
    def __getitem__(self,index):
        '''Defines the default getitem function.'''
        return self.frames[index]
    def __setitem__(self, index, value):
        '''Defines the default setitem function.'''
        self.frames[index] = value
    def append(self,value):
        '''Appends a single value to the frames.'''
        self.frames.append(value)
    def __getslice__(self,index1,index2):
        '''Defines the default getslice function.'''
        return self.frames[index1:index2]
    def get_HTML(self):
        url_file = urllib2.urlopen(self.URL)
	url_text = url_file.read()
	return url_text	
    def parse_file(self):
        pass
    def download_images(self):
        pass

