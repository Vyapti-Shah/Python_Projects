#animations
from tkinter import * 
import time

WIDTH = 500
HEIGHT = 324
xVelocity = 1
yVelocity = 1

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

earthImage = PhotoImage(file='python/images/earth.png')
myearth = canvas.create_image(0,0,image=earthImage,anchor=NW)

ufoImage = PhotoImage(file='python/images/ufo.png')
myUFO = canvas.create_image(0,0,image=ufoImage,anchor=NW)

ufo_width = ufoImage.width()
ufo_height = ufoImage.height()

while True:
    coordinates = canvas.coords(myUFO)
    print(coordinates)

    if(coordinates[0]>WIDTH-ufo_width or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>HEIGHT-ufo_height or coordinates[1]<0):
        yVelocity = -yVelocity

    canvas.move(myUFO,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()