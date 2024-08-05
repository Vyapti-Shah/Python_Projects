#canvas - widget that is used to draw graphs, plot, image in a window

from tkinter import * 

window = Tk()

canvas = Canvas(window,height=500,width=500)

canvas.create_arc(0,0,500,500,fill="red",width=10,extent=180) 
canvas.create_arc(0,0,500,500,fill="white",width=10,start=180,extent=180) 
canvas.create_oval(190,190,310,310,fill="white",width=10)

canvas.pack()

window.mainloop()