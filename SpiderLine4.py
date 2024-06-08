# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:18:44 2022

@author: Catarina Rocha
"""

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
import tkinter.font as font
c4=Connect4()

import tkinter as tk                
from tkinter import font  as tkfont 
from tkinter import Entry
from player_player2 import fplays
from player_bot import play_bot
from bot_bot import fbot_bot
from player_bot2 import fplay_bot

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=30, 
        weight="bold", slant="italic")
        self.geometry("400x400")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "white")
        self.controller = controller
        label = tk.Label(self, text="Spider Line 4", font=controller.title_font, bg = "white")
        label.pack(side="top", fill="x", pady=10)
        myFont = font.Font(family='Helvetica',size=100)

        button1 = tk.Button(self, text="Player vs Player",width=25,
                           height=5,command=lambda:fplays(),bg = "#FF6347")
        button1["font"]=myFont
        button1.pack()
        
        button2 = tk.Button(self, text="Player vs Computer",width=25,
                           height=5,command=lambda:fplay_bot(), bg= "#B0E2FF")
        button2["font"]=myFont
        button2.pack()
        button3 = tk.Button(self, text="Computer vs Computer",width=25,
                           height=5,command=lambda:fbot_bot(),bg = "#FF6347")
        button3["font"]=myFont
        button3.pack()
        
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
     
       
if __name__ == "__main__":
    #root = Tk()
    #app = SampleApp()
    #
    #root.mainloop()
    app = SampleApp()
    app.mainloop()
    app.geometry('700x400')