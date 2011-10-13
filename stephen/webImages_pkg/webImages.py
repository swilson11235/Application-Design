'''This class processes ''' 

__author__ = 'Stephen'
__version__ = '1.0'

#import webImages
import urllib2,re

class webImages():
    def __init__(self, url='http://www.nytimes.com'):
        '''Initializes a new webpage's images.'''
        self.URL=url
        self.HTML = self.get_HTML()
    def __add__(self):
        ''''''
        pass
    def __len__(self):
        '''Returns the number of frames.'''
        pass
#        return len(self.frames)
    def __str__(self):
        '''Returns a string representation of the class (the frames, in other words data, are in a string).'''
        pass
#        return str(self.frames)
    def __getitem__(self,index):
        '''Defines the default getitem function.'''
        pass
        #return self.frames[index]
    def __setitem__(self, index, value):
        '''Defines the default setitem function.'''
        pass
#self.frames[index] = value
    def append(self,value):
        '''Appends a single value to the frames.'''
        pass
        #self.frames.append(value)
    def __getslice__(self,index1,index2):
        '''Defines the default getslice function.'''
        pass
        #return self.frames[index1:index2]
    def get_HTML(self):
        '''Gets an HTML document from the URL. Is called by __init__.'''
        url_file = urllib2.urlopen(self.URL)
	url_text = url_file.read()
	return url_text	
    def parse_file(self):
        '''Parses an HTML file to find images.'''
        regex='''src=".*"\>'''
        results = re.findall(regex, self.HTML)
        regex2 = '''"\<http:/...*"'''
        tmp=[]
        for line in results:
            tmp.append(re.findall(regex2,line))
        for i in range(0, len(results)):
            results[i] = results[i].lstrip("img src")
        for result in results:
            print '\n'
            print result 
    def download_images(self):
        pass

