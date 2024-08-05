# scale slider project
from tkinter import *

def submit():
    print("The temperature is "+str(scale.get())+"°C")

window = Tk()

icon = PhotoImage(file='python/images/scaleslider.png')
window.iconphoto(True,icon)

hotImage = PhotoImage(file='python/images/fire.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,from_=100,to=0,length=600,orient=VERTICAL,font=("Times New Roman",20),
              tickinterval=10, #adds numeric indicators on the scale
              #showvalue=0, #hides the current value 
              resolution=1, #increment of slider
              troughcolor="lightblue",
              fg="white",
              bg="black",
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to']) #to set current value of the slider
scale.pack()

coldImage = PhotoImage(file='python/images/snowflake.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text="submit",command=submit,font=("Times New Roman",20),fg="white",bg="black")
button.pack()

window.mainloop()