# progress bar
from tkinter import *
from tkinter.ttk import *
import time

def start():
    task = 10
    x = 0
    while(x<task):
        time.sleep(1)
        bar['value']+=10
        x+=1
        percent.set(str(int((x/task)*100))+"%")
        text.set(str(x)+"/"+str(task)+" tasks completed")
        window.update_idletasks() #after each iteration it will update the task

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(padx=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()

window.mainloop()