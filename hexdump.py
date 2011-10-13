import sys
import string

filename = sys.argv[1]

f = open(filename, 'r')
my_bytes=f.read(16)
while my_bytes:
    for char in my_bytes:
        print hex(ord(char))[2:].zfill(2),#',' removes end of line character
    print "   "*(16-len(my_bytes)),
    print '|',
    for char in my_bytes:
        if char not in string.lowercase +string.uppercase:
            print '.',
        else:
            print char,#',' removes end of line character

    print '\n'
    my_bytes = f.read(16)
    
