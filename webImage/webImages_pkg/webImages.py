'''This class processes ''' 

__author__ = 'Stephen'
__version__ = '1.0'

#import webImages
import urllib2,re,string
import os

class webImages():
    def __init__(self, url='http://www.nytimes.com'):
        '''Initializes a new webpage's images.'''
        self.URL=url
        self.HTML=self.get_HTML()
        self.links=[]
    def __add__(self,link_list):
        '''Adds two link lists together.'''
        for i in range(0, len(link_list)):
            self.links.append(link_list[i])
        return self.links
    def __len__(self):
        '''Returns the number of images.'''
        return len(self.links)
    def __str__(self):
        '''Returns a string representation of the class, specifically the links.'''
        return str(self.links)
    def __getitem__(self,index):
        '''Defines the default getitem function.'''
        return self.links[index]
    def __setitem__(self, index, value):
        '''Defines the default setitem function.'''
        self.links[index] = value
    def append(self,value):
        '''Appends a single link to the links.'''
        self.links.append(value)
    def __getslice__(self,index1,index2):
        '''Defines the default getslice function.'''
        return self.links[index1:index2]
    def get_HTML(self):
        '''Gets an HTML document from the URL. Is called by __init__.'''
        url_file = urllib2.urlopen(self.URL)
	url_text = url_file.read()
	return url_text	
    def parse_file(self, HTML=''):
        '''Parses HTML code to find images. By default, the code is the initialized file.'''
        regex='''\<img[^\>]*src="http://[^\"]*"''' #referenced regex cheatsheet at http://www.cheatography.com/davechild/cheat-sheets/regular-expressions/
        if HTML=='':
            HTML=self.HTML
        results = re.findall(regex,HTML)
        tmp=[]
        for result in results:
            result = re.findall('''http://[^\"]*''',result)
            tmp.append(result[0])
        results = tmp
        tmp =[]
        for i in range(0,len(results)):
            if results[i][-4] != '.'and results[i][-5] != '.' or results[i][-1]== '?':
                tmp.append(i)
        tmp.sort(reverse=True)
        for item in tmp:
           del results[item]
        self.links= results
        return results

    def download_images(self, path ='images'):
        '''Downloads images to a path.'''
        if not os.access(path, os.F_OK):
            os.mkdir(path)
        os.chdir(path)
        i=0
        for link in self.links:
            urlish = urllib2.urlopen(link)
            data = urlish.read()
            fname = re.findall('''...\.(gif|jpg|jpeg|svg|tiff|png)''',link)
            if fname==[]:
                print 'This link does not have a supported file type: ' + link
            else:
                f = open(str(i)+'.'+fname[0], 'w')
                f.write(data)
            i+=1

