from tkinter import *
from tkinter import colorchooser #submodule

def click():
    colour = colorchooser.askcolor()
    print(colour)
    colourHex = colour[1]
    print(colourHex)
    window.config(bg=colourHex) #changes the bagckground colour
    #window.config(bg=colorchooser.askcolour()[1]) #changes the bagckground colour


window = Tk()
window.geometry("500x500")
button = Button(window,text="click",command=click,fg="white",bg="black",font=("Times New Roman",20))
button.pack()
window.mainloop()