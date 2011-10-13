
__author__ = 'Stephen'
__version__ = '1.0'

class bookmark():
    '''This class takes bookmark information and stores it. It can also create HTML information for that bookmark.'''
    def __init__ (self, name, URL, time):
        '''Initializes the class. The class takes the name, URL, and time of the bookmark.'''
        self.name = name
        self.URL = URL
        self.time_created = time
    def setName(self, newname):
        '''This function sets the bookmark's name when given a string with the new name.'''
        self.name = newname
    def getName(self):
        '''Gets the name of the bookmark.'''
        return self.name
    def setURL(self, newURL):
        '''This function sets the bookmark's URL when given a string with the new name.'''
        self.URL = newURL
    def getURL(self):
        '''Gets the URL of the bookmark.'''
        return self.URL
    def getTime(self):
        '''Gets the time the bookmark was created.'''
        return self.time_created
    def __str__(self):
        '''Allows for the printing of a bookmark.'''
        result = 'Name: '+ str(self.name)
        result += '\nURL: ' + str(self.URL)
        result += '\nTime: ' + str(self.time_created) + '\n'
        return result
    def toLink(self):
        '''Generates an HTML string of the bookmark.'''
        self.toLinkstring = '<A HREF="{URL}" ADD_DATE="{time}">{name}</A>'.format(URL=self.URL, time = self.time_created, name=self.name)
        return self.toLinkstring
