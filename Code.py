from tkinter import *
from tkinter import messagebox
import os
import fnmatch
import matplotlib.pyplot as plt
import random
from tkinter import *
from PIL import ImageTk,Image

win=Tk()
win.title("Main window")
win.configure(bg='GRAY')
win.geometry('300x300+0+0')

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []
print("Scanning drive ")
for root, dirnames, filenames in os.walk("D:/"):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))
m=matches
print("Scan complete")
    

def openimg():
    global img
    top=Toplevel()
    top.title("Randomly selected Image")
    r=random.choice(m)
    img=ImageTk.PhotoImage(Image.open(r))
    label=Label(top, image=img)
    label.pack()
    
def iexit():
    iExit=messagebox.askyesno("Exit","Are you sure you want to exit" )
    if iExit > 0:
        win.destroy()
        return            
btn=Button(win,text="Click to view random image", command=openimg).pack()
btn2=Button(win,text='Exit program',command=iexit).pack()
    
win.mainloop()



