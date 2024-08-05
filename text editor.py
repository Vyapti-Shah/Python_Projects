#text editor
import os
from tkinter import *
from tkinter import filedialog,colorchooser,font
from tkinter.messagebox import * 
from tkinter.filedialog import * 

def change_colour():
    colour = colorchooser.askcolor(title="Pick a colour....or else")
    print(colour)
    text_area.config(fg=colour[1])
  
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    window.title("Untitled")
    text_area.delete(1.0,END)

def open_file():
    filepath = filedialog.askopenfilename(defaultextension=".txt",
                                          filetypes=(("text files","*.txt"),("all files","*.*")))
    try:
        window.title(os.path.basename(filepath))
        text_area.delete(1.0,END)
        file = open(filepath,"r") #r=read
        text_area.insert(1.0,file.read())
    except Exception:
        print("Couldn't open file")
    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfile(initialdir="OM\\text.txt",
                                    defaultextension=".txt",
                                    filetypes=[("text files","*.txt"),
                                               ("All files","*.*")])
    
    if file is None: # if this was not written then the program throws an exception
        return
    else:
        try:
            window.title(os.path.basename(file.name))
            with open(file.name, "w") as f:
                f.write(text_area.get(1.0,END))
        except Exception:
            print("Couldn't save file")
        finally:
            file.close()

def cut_file():
    text_area.event_generate("<<Cut>>")
def copy_file():
    text_area.event_generate("<<Copy>>")
def paste_file():
    text_area.event_generate("<<Paste>>")

def about_file():
    showinfo("About this program", "This is a program written by YOU!")
def quit_file():
    window.destroy()

window = Tk()
window.title("Text Editor")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

font_name = StringVar(window)
font_name.set("Times New Roman")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window,font = (font_name.get(),font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT,fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

colour_button = Button(frame,text="colour",command=change_colour)
colour_button.grid(row=0,column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0,column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0,column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)

edit_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=cut_file)
edit_menu.add_command(label="Copy",command=copy_file)
edit_menu.add_command(label="Paste",command=paste_file)

help_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About",command=about_file)

window.mainloop()