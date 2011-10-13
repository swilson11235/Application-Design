''' This class allows for editing of bookmark files.'''

__author__ = 'Stephen'
__version__ = '1.0'
from bookmark import bookmark
import time

class UserBookmarks():
    def __init__(self, username):
        ''' Initializes the class. Takes a username string.'''
        self.username = username
        self.user_ls = []
    def setUsername(self,username):
        '''Sets the username when given a string.'''
        self.username = username
    def getUsername(self):
        '''Returns the username.'''
        return self.username
    def addBookmark(self,bookmark_name, URL, time_added):
        '''Adds a bookmark from the bookmark class to the user's list. If not importing from an HTML file, pass an empty string as the time created added.'''
        if time_added == '':
            time_added = time.time()
        self.user_ls.append(bookmark(bookmark_name,URL,time_added))
    def removeBookmark(self,bookmark_name):
        '''Removes a bookmark given the bookmark's name.'''
        i=0
        for item in self.user_ls:
            if item.getName() == bookmark_name:
                del self.user_ls[i]
            i+=1
    def __len__(self):
        '''Allows the returning of how many bookmarks are present.'''
        return len(self.user_ls)
    def __str__(self):
        '''Allows printing of the UserBookmark class.'''
        for item in self.user_ls:
            tmp += '\n' + str(item)
        return tmp
    def toLinks(self):
        ''' Returns a string with HTML links for each bookmark.'''
        tmp =''
        for item in self.user_ls:
            tmp += '\n' +item.toLink()
        return tmp
