

import platform
import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk

from functools import partial
from tkinter import messagebox
from tkinter import *
import tkinter 

from spide4 import Connect4
from logic import get_best_move, fav4
from tkinter import messagebox
c4=Connect4()

import tkinter as tk                
from tkinter import font  as tkfont 
from tkinter import Entry

class App():
    def __init__(self, root):
        self.root = root
        self.TopFrame = Frame(root) # Create a top frame to place the original grid
        self.BottomFrame = Frame(root) # Create a frame for the additional buttons
        self.TopFrame.grid(row=0) # Place the Frame itself
        self.BottomFrame.grid(row=6) # Place the new Frame directly below the first
        self.player=1
        # Changed to an instance variable to reference in Function method
        buttonQ = Button(self.BottomFrame, text="Quit", command=self.endProgam)
        #buttonS = Button(self.BottomFrame, text="Start", command=self.start)
        #buttonS.grid(row=0, column=0, padx=10)
        buttonQ.grid(row=0, column=1, padx=10)

    def Function(self):
        self.grid = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append(Button(self.TopFrame,width=6,height=3,command=lambda i=i, j=j: self.click(i, j),background='white'))
                row[-1].grid(row=i,column=j)
            self.grid.append(row)
            

    def click(self,row,col):
        if c4.move(col,row, self.player):
            #button["text"] = symbol(player)
            self.grid[row][col]["bg"]=self.color(self.player)
            if c4.is_gameover(self.player):
                self.print_win()
            self.swap_player()

            
    def endProgam(self):
        # top.quit()
        self.root.destroy() 

            
    def swap_player(self):
        
        self.player = 2 if self.player == 1 else 1
        
    def symbol(self,player):
        if player == 1:
            return 'X'
        else: return 'O'
        
        
    def color(self,player):
        if player == 1:
            return 'red'
        else: return 'blue'
        
    def print_win(self):
        box = messagebox.showinfo("Winner", "Player" + str(self.player) +  " (" + ("Red" if self.player == 1 else "Blue") + ") Won!\n")
        self.root.destroy()
        
    def print_tie(self):
        box = messagebox.showinfo("Tied Game","It is a tie")
        self.root.destroy()

def fplays():
    root = Tk()
    app = App(root)
    app.Function()
    root.mainloop()