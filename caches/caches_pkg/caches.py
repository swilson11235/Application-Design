'''This class grabs a url file and caches it''' 

__author__ = 'Stephen'
__version__ = '1.0'


import urllib2,sqlite3
import os
from time import localtime
import time

def recreate_database():
    os.remove('cache.db')
    conn = sqlite3.connect('cache.db')
    c = conn.cursor()
    conn.commit()
    c.close()
    
class caches():
    def __init__(self, url='', cache='cache.db',save='y'):
        '''Initializes a new webpage's images. Pass a 'n' for save if you wish to save the database after the program exits.'''
        self.save=save
        self.URL=url
        self.cache=cache
        self.url_miss=0
        self.url_replace=0
        if not self.URL=='':
            self.cache_urlopen()
    def __del__(self):
        '''The database will be deleted if a parameter is passed when the class is created.'''
        if self.save=='n':
            os.remove(self.cache)
    def add_url(self,url):
        '''Adds the given url to the cache.'''
        self.URL=url
        self.cache_urlopen()
    def cache_urlopen(self):
        '''Is called by __init__ and add_url(url) to open and cache a url.''' 
        try:
            url_file = urllib2.urlopen(self.URL)
            url_text = url_file.read().decode('UTF-8')
            conn = sqlite3.connect(self.cache)
            c = conn.cursor()
            c.execute('''create table if not exists {table_name} (html text,time TEXT)'''.format(table_name='cache'))
            #gets number of items in table
            c.execute('''select count(*) from cache''')
            for row in c:
                count = row[0]
            # ensures that there are no more than 10 items in the table
            if count > 9:
                self.url_replace+=1
                min_time = c.execute('''select MIN(time) from cache''')
                for row in min_time:
                    min_t=row[0]
                c.execute('''delete from cache where time="{time}"'''.format(time=min_t))
            ctime=time.strftime("%y%m%d%H%M%s", localtime())
            c.execute( '''insert into cache values (?, ?)''',(url_text,ctime))
            conn.commit()
            c.close()
        except:
            self.url_miss +=1
        
    def read_cache(self, command):
        '''Gives a command to the current database given a command, and returns the output.'''
        conn = sqlite3.connect(self.cache)
        c = conn.cursor()
        c.execute(command)
        for row in c:
            output=row[0]
        conn.commit()
        c.close()
        return output
    def stats (self):
        '''Returns stats that relate to if a URL was missed, hit, or if a URL has been replaced.'''
        conn = sqlite3.connect(self.cache)
        c = conn.cursor()
        c.execute('''select count(*) from cache''')
        for row in c:
            counter=row[0]
        conn.commit()
        c.close()
        output = (self.url_miss, counter, self.url_replace)
        return output
