# TIC TAC TOE
from tkinter import *
import random

def next_turn():
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False: #check to see if buttons are empty and there is no winner 
        if player == players[0]: #player[0] if any other symbol to be used or "X" if only X to be used 
            buttons[row][column]['text'] = player

        if check_winner() is False:
            player = players[1]
            label.config(text=(players[1]+" turn"))
        elif check_winner() is True:
            label.config(text=player[0]+" wins")
        elif check_winner() == "Tie":
            label.config(text=("Tie"))
    else:
        buttons[row][column]['text'] == player
        if check_winner() is False:
            player = players[0]
            label.config(text=(players[0]+" turn"))
        elif check_winner() is True:
            label.config(text=player[1]+" wins")
        elif check_winner() == "Tie":
            label.config(text=("Tie"))

def check_winner():
    pass
def empty_spaces():
    pass
def new_game():
    pass

window = Tk()

window.title("Tic-Tac-Toe")
players = ["X","O"]
player = random.choice(players)
buttons = [[0,0,0],[0,0,0],[0,0,0]]
label = Label(text=player + " turn", font=("Times New Roman",40))
label.pack(side="top")

reset_button = Button(text="restart",font=("Times New Roman",20),command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("Times New Roman",20),width=5,height=2,command=lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
        buttons[row][column].grid(row=row,column=column)

window.mainloop(row,column)