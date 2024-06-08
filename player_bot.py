# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 17:32:18 2022

@author: Catarina Rocha
"""

from tkinter import *
import tkinter 
from spide4 import Connect4
from logic import get_best_move, fav4
from tkinter import messagebox
c4=Connect4()
root = Tk()
root.geometry("400x400")
# set minimum window size value
root.minsize(400, 400)
 
# set maximum window size value
root.maxsize(400, 400)
frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)


Grid.rowconfigure(frame, 7)
Grid.columnconfigure(frame, 0)
player=1
default_text=""
default_color="white"

# def play():
#     menu = Tk()
#     menu.geometry("250x250")
#     menu.title("Spider Line 4")
#     #wpc = partial(main, menu)
      
#     head = Button(menu, text = "---Welcome to tic-tac-toe---",
#                   activeforeground = 'red',
#                   activebackground = "yellow", bg = "red", 
#                   fg = "yellow", width = 500, font = 'summer', bd = 5)
      
#     # B1 = Button(menu, text = "Single Player", command = wpc, 
#     #             activeforeground = 'red',
#     #             activebackground = "yellow", bg = "red", 
#     #             fg = "yellow", width = 500, font = 'summer', bd = 5)
      
#     B2 = Button(menu, text = "Multi Player", command = lambda: player_player(5), activeforeground = 'red',
#                 activebackground = "yellow", bg = "red", fg = "yellow",
#                 width = 500, font = 'summer', bd = 5)
      
#     B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'red',
#                 activebackground = "yellow", bg = "red", fg = "yellow",
#                 width = 500, font = 'summer', bd = 5)
#     head.pack(side = 'top')
#     #B1.pack(side = 'top')
#     B2.pack(side = 'top')
#     B3.pack(side = 'top')
#     menu.mainloop()
def swap_player():
    global player
    player = 2 if player == 1 else 1
    
def symbol(player):
    if player == 1:
        return 'X'
    else: return 'O'
    
def color(player):
    if player == 1:
        return 'red'
    else: return 'blue'
    
def print_win():
    box = messagebox.showinfo("Winner", "Player" + str(player) +  " (" + ("X" if player == 1 else "O") + ") Won!\n")
    root.destroy()

def print_bot_error():
    box = messagebox.showinfo("Bot couldn't calculate best move!")
    root.destroy()

def main(height=5,width=5):
    buttons = []
    for x in range(width):
        button_row = []
        for y in range(height):
            btn = tkinter.Button(frame, bg=default_color)
            btn.grid(column=x, row=y, sticky=N+S+E+W)
            btn["command"] = lambda btn=btn,x=x,y=y, buttons=buttons: click(btn,x,y,buttons)
            btn["text"] = default_text
            button_row.append(btn)
        buttons.append(button_row)

    for x in range(width):
        Grid.columnconfigure(frame, x, weight=1)

    for y in range(height):
        Grid.rowconfigure(frame, y, weight=1)

    return frame
def click(button,col,row,buttons):
     print(c4)
     if (c4.move(col,row, player)) and player == 1:
         button["text"] = symbol(player)
         button["bg"] = color(player)
         if c4.is_gameover(player):
             print_win()
         c4.c[col,row]=5
         swap_player()
         col,row = get_best_move(c4, player, fav4)
         print(buttons,col,row)
         if (c4.move(col,row, player)) and player == 2:
             print("you clicked row %s column %s" % (row, col))
             buttons[col][row].config(text=symbol(player))
             buttons[col][row].config(bg=color(player))
             #button["text"] = symbol(player)
             if c4.is_gameover(player):
                 print_win()
                
             c4.c[col,row]=5
             swap_player()
         else:
            print_bot_error()
            
            
def play_bot():            
    w= main(5,5)
    tkinter.mainloop()
