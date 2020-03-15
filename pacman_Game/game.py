
from tkinter import * 
from tkinter.ttk import *
  
# creating tkinter window 
root = Tk() 
  
# Adding widgets to the root window 
Label(root, text = 'Packman Game', font =( 
  'Verdana', 15)).pack(side = TOP, pady = 10) 
  
# Creating a photoimage object to use image 
photo = PhotoImage(file = r"C:/Users/student/Pictures/Pacman_HD.png") 

# load = Image.open("C:/Users/student/Pictures/Pacman_HD.png")
# render = ImageTk.PhotoImage(load)  

def show_image():
    root = Tk()
 
    canvas = Canvas(root,  width=400, height=400)
    canvas.pack()
 
    img = PhotoImage(file="C:/Users/student/Pictures/Pacman_HD.png")
    canvas.create_image(10, 10, anchor=NW, image=img)
 
    mainloop()
 
if __name__ == '__main__':
    show_image()
  
mainloop() 
