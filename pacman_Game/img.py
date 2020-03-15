from tkinter import *
master = Tk()
w = Canvas(master, width=1600, height=1400)
w.pack()
#canvas_height=400
#canvas_width=300
w['background']= '#AEB6BF'
#w.create_line(0,100,canvas_width,300)
#w.create_oval(50,50,100,100)


for i in range(1, 20):
    x = 50 + 50 * i
    for j in range(1,20):
    	y=50+50*j
    	w.create_oval(x, y, x + 10, y + 10, fill="red")




	
w.create_oval(25,25,50,50,fill="#A52222")
w.create_rectangle(250,60,620,100, fill="green")
mainloop()