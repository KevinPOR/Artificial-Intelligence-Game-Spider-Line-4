
from spide4 import Connect4
from logic import get_best_move, fav4
from time import sleep
from tkinter import *




c4 = Connect4()
# 2

player = 1
depth = 4

def swap_player():
    global player
    player = 2 if player == 1 else 1

def print_win():
    print(c4)
    print("Player " + str(player) + " (" + ("X" if player == 1 else "O") + ") Won!\n")

def print_bot_error():
    print("Bot couldn't calculate best move!")

def PvsP():
    while(1):
        print(c4)
        if c4.move(int(input("COL: "))-1,int(input("ROW: "))-1, player):
            if c4.is_gameover(player):
                print_win()
                break
            swap_player()
    
def PvsB():
    while(1):
        # ----- PLAYER -----
        print(c4)
        col=int(input("COL: "))-1
        row=int(input("ROW: "))-1
        #if (c4.move(int(input("COL: "))-1,int(input("ROW: "))-1, player)) and player == 1:
        if (c4.move(col,row, player)) and player == 1:
            if c4.is_gameover(player):
                print_win()
                break
            c4.c[col,row]=5
            swap_player()
            
            # ----- BOT -----
            print(c4)
            col,row = get_best_move(c4, player, fav4)
            if (c4.move(col,row, player)) and player == 2:
                if c4.is_gameover(player):
                    print_win()
                    break
                c4.c[col,row]=5
                swap_player()
            else:
                print_bot_error()
                break

def BvsP():
    while(1):
        # ----- BOT -----
        print(c4)
        col,row = get_best_move(c4, player, fav4)
        if (c4.move(col,row, player)):
            if c4.is_gameover(player):
                print_win()
                break
            c4.c[col,row]=5
            swap_player()

            # ----- PLAYER -----
            while (player==2):
                print(c4)
                if (c4.move(int(input("COL: "))-1,int(input("ROW: "))-1, player)):
                    if c4.is_gameover(player):
                        print_win()
                        return 'ehehe'
                    c4.c[col,row]=5
                    swap_player()
                
        else:
           print_bot_error()
           break
    
def BvsB():
    counter=0
    while(1):
        print(c4)
        if(c4.is_gameover(player)):
                print_win()
                break
        if counter ==c4.COLS * c4.ROWS:
            print("It is a tie")
            break
        col,row = get_best_move(c4, player, fav4)
        if (c4.move(col,row, player)):
            if(c4.is_gameover(player)):
                print_win()
                break
            c4.c[col,row]=5
            counter+=1
            swap_player()
        # sleep(1)


print("|---------------------|")
print("|       Connect4      |")
print("|---------------------|")
print("  1- Player vs Player  ")
print("  2- Player vs Bot     ")
print("  3- Bot vs Player     ")
print("  4- Bot vs Bot        ")
print("                       ")
op = int(input("-> "))
print("\n")

if op == 1:
    PvsP()
elif op == 2:
    PvsB()
elif op == 3:
    BvsP()
elif op == 4:
    BvsB()