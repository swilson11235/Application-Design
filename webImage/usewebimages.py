'''This function processes image tags from a website and downloads those images using the webImage class.''' 

__author__ = 'Stephen'
__version__ = '1.0'

from webImages_pkg import webImages
import os,re
import Tkinter 
from tkSimpleDialog import *
import Image,ImageTk

class Application:
    '''Creates a GUI to interact with.'''
    def __init__(self,master):
        '''Initializes the GUI.'''
        master.title("webImages")
        self.index=0
        self.image = Label()

        top_frame = Frame(master)
        top_frame.pack(fill=X, expand=1)
        
        self.get_website = Button(top_frame, text="Load a new website", command=self.get_website)
        self.get_website.pack(side=LEFT, fill=X)

        self.right_button = Button(top_frame, text="-->", command=self.right) 
        self.right_button.pack(side=RIGHT, fill=X)

        self.left_button = Button(top_frame, text="<--", command=self.left) 
        self.left_button.pack(side=RIGHT, fill=X)

        bottom_frame = Frame(master)
        bottom_frame.pack(fill=X,expand=1)
        self.montage= Button(bottom_frame, text='Create Montage',command=self.montage)
        self.montage.pack(side=BOTTOM, fill=X)
        self.image.pack()
    def get_website(self):
        '''Loads a website into the webImages class and calls the view_image module.'''
        self.website =''
        self.website = askstring('Website?','Enter the website (with HTTP://): ')
        if self.website =='':
            self.web_object = webImages()
        else:
            self.web_object = webImages(self.website)
        self.web_object.parse_file()
        self.web_object.download_images()
        self.view_image(self.index)
    
    def view_image(self,i='0'):
        '''Allows the viewing of images.'''
        images= os.listdir(os.getcwd())
        self.image_string=''
        for image in images:
            self.image_string+=image
            self.image_string+=' '
        self.photo = ImageTk.PhotoImage(file=images[i])
        self.image.destroy()
        self.image = Label(image=self.photo)
        self.image.pack()

    def left(self):
        '''Moves to another image.'''
        if not self.index == 0:
            self.index-=1
            self.view_image(self.index)
    def right(self):
        '''Move to another image.'''
        images=os.listdir(os.getcwd())
        if os.access(images[self.index], os.F_OK):
            self.index+=1
            self.view_image(self.index)

    def montage(self):
        '''Creates a montage and displays it. This is automatically saved as montage.jpg.'''
        os.system('montage'+' '+self.image_string+ '-frame 5 -shadow'+' montage.jpg')
        self.photo = ImageTk.PhotoImage(file='montage.jpg')
        self.image.destroy()
        self.image = Label(image=self.photo)
        self.image.pack()
            
    

def main():
    '''Executes commands from the webImage class.'''
    root = Tk()
    app=Application(master=root)
    root.mainloop()
if __name__=='__main__':
    main()
