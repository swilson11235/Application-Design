''' This file allows for storing and editing of bookmark HTML files.'''

__author__ = 'Stephen'
__version__ = '1.0'
from UserBookmarks import UserBookmarks

def process_HTMLfile(filename):
    '''Processes HTML files and returns a list of HTML links.'''
    tmp = open(filename)
    text = tmp.read()
    tmp.close
    text = text.splitlines()
    HTML_link_ls = []
    for item in text:
        if item.find("HREF") != -1:
            item= item.strip()
            HTML_link_ls.append(item)
    return HTML_link_ls

def create_user():
    ''' Creates a set of bookmarks under a certain user.'''
    user = raw_input('What is your name: ')
    newuser = UserBookmarks(user)
    return newuser

def process_linkHTML(HTML_ls,bkmks):
    '''Tokenizes and processes a single HTML string that represents a link.'''
    for HTML_link in HTML_ls:
        tmps= HTML_link.split('<') #slicing according to index would be nice
        HTML_link = []
        for item in tmps:
            HTML_link += item.split('>')
        bkmks = init_var(HTML_link,bkmks)
    return bkmks

def init_var(link_ls,bkmarks):
    '''Aids the process_linkHTML function by searching the already tokenized HTML string and assigning the name, URL, and time to bookmarks.'''
    i=0
    time_created = ''
    for item in link_ls: # for i in range(len(link_ls))
        if item == '/A':
            name = link_ls[i-1]
        i+=1
    tmps =[]
    for item in link_ls:
        tmps += item.split()
        link_ls = tmps
    for item in link_ls:
        i = item.find('HREF')
        if i != -1:
            item = item.strip('"HREF="')
            URL = item 
    for item in link_ls:
        i = item.find('ADD_DATE=')
        if i != -1:
            time_created = item[i+10:-1]
    bkmarks.addBookmark(name,URL,time_created)
    return bkmarks

def write_bookmarks(bkmarks):
    '''Writes bookmarks to file(savedbookmarks.html) according to the template.txt'''
    t = open("template.txt")
    template = t.read()
    tmp = template.format(links=bkmarks.toLinks())
    t.close()
    f = open("savedbookmarks.html", "w")
    f.write(tmp)
    f.close()
    
def main():
    flname = raw_input("Filename: ")
    link_list = process_HTMLfile(flname)
    bookmarks = create_user()
    bookmarks = process_linkHTML(link_list,bookmarks)
    write_bookmarks(bookmarks)

if __name__ =='__main__':
    main()
