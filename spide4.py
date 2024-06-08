import numpy as np
#from datetime import datetime


class Connect4:
    ROWS = 5
    COLS = 5
    
    def __init__(self):
        self.board = np.zeros((self.ROWS, self.COLS), dtype=int)
        self.c = np.array([[3,3,3,3,3],
                    [3,0,0,0,3],
                    [3,0,0,0,3],
                    [3,0,0,0,3],
                    [3,3,3,3,3]])

    def __str__(self):
        ret = ""
        for row in reversed(self.board):
            for cell in row:
                ret += " X " if cell == 1 else " O " if cell == 2 else " * "
            ret += "\n"
        return ret
    


    def move(self, col,row, player):

        if col >= self.COLS or col < 0 :
            return False
        
        if row >= self.ROWS or row < 0 :
            return False

        #swapaxes facilitates the iteration through a column
        tempBoard = np.swapaxes(self.board, 0, 1)
        

        if tempBoard[col, row] == 0:
            if self.possible_pos (col, row):
                tempBoard[col, row] = player
                self.board = np.swapaxes(tempBoard, 0, 1)
                return True
            else: return False
                

        return False


    def possible_pos (self, col, row):
        tempBoard = np.swapaxes(self.board, 0, 1)
        
        if col==0 or col == self.COLS-1 or row == 0 or row== self.ROWS -1:
            #print(self.board)
            if tempBoard[col, row] == 0:
                return True
            else:
                
                return False
        

        if not np.any((tempBoard[col,row+1:self.ROWS] == 0)):
            
            return True
        
        elif not np.any((tempBoard[col,0:row] == 0)):
            
            return True
            
    
        elif not np.any((tempBoard[0:col,row] == 0)):
            
            return True
        
        
        elif not np.any((self.board[row,col+1:self.COLS] == 0)):
            
            return True
        
        else: return False

    def is_gameover(self, player):
        return self.nlinhas4(player) >= 1
   

    def get_valid_moves(self):
        
        tempBoard = np.swapaxes(self.board, 0, 1)

        ret = []
        for col in range(self.COLS+1):
            for row in range (self.ROWS+1):
                if(col < self.COLS and row < self.ROWS):
                    if tempBoard[col, row] == 0:

                        if col==0 or col == self.COLS-1 or row == 0 or row== self.ROWS -1:
                                ret.append([col,row])
                                continue

                        if(row>self.ROWS):
                            up = tempBoard[col, row+1]
                            if up !=0:
                               if not np.any((tempBoard[col,row+1:self.ROWS] == 0)):
                                    ret.append([col,row])
                                    continue
                        if(row>0):  
                            down = tempBoard[col, row-1]
                            if down !=0:
                               if not np.any((tempBoard[col,0:row] == 0)):
                                   ret.append([col,row])
                                   continue
                        if(col>0):
                            left = tempBoard[col-1, row]
                            if left !=0:
                               if not np.any((tempBoard[0:col,row] == 0)):
                                   ret.append([col,row])
                                   continue

                        if(col>self.COLS):
                            right = tempBoard[col+1, row]
                            if right !=0:
                                if not np.any((self.board[row,col+1:self.COLS] == 0)):
                                    ret.append([col,row])
                                    continue                                    
        return ret

 

    def get_valid_moves_Karim2(self):
        tempBoard = np.swapaxes(self.board, 0, 1)
        
        ret = []
        for col in range(self.COLS):
            for row in range (self.ROWS):
                if self.c[row,col]==4:
                    continue
                if tempBoard[col, row] == 0:
                    if col==0 or col == self.COLS-1 or row == 0 or row== self.ROWS -1:
                            ret.append([col,row])
                            continue
 
                    elif self.possible_pos (col, row):
                        ret.append([col,row])

        return ret

    def nlinhas4(self, player):
        return self.nlinhas(player, exact=True)

    def nlinhas3(self, player):
        return self.nlinhas(player, exact=False)

    def central(self, player):
        tempBoard = np.swapaxes(self.board, 0, 1)
        return 2 * np.count_nonzero(tempBoard[3] == player) \
            + np.count_nonzero(tempBoard[2] == player) \
            + np.count_nonzero(tempBoard[4] == player)


    def nlinhas(self, player, exact):
        ret = 0
        # dx = [0, 0, 1,-1, 1, 1,-1,-1]
        # dy = [1,-1, 0, 0, 1,-1, 1,-1]
        dx = [0, 1, 1, 1]
        dy = [1, 0, 1,-1]
        for x in range(self.ROWS):
            for y in range(self.COLS):
                cell = self.board[x, y]
                if not cell or cell != player:
                    continue
                for i in range(len(dx)):
                    xTemp = x + dx[i]
                    yTemp = y + dy[i]
                    if xTemp not in range(self.ROWS) or yTemp not in range(self.COLS):
                        continue

                    newCell = self.board[xTemp, yTemp]

                    if cell == newCell or (not exact and newCell == 0):
                        if self.checkLine(x, y, dx[i], dy[i], player, exact):
                            ret += 1
                            
        return ret

    def checkLine(self, x, y, dx, dy, player, exact):
        counter = 0
        for i in range(4):
            newX = x + dx*i
            newY = y + dy*i
            if newX not in range(self.ROWS) or newY not in range(self.COLS):
                return False
            cell = self.board[newX, newY]
            if cell == player:
                continue
            elif not exact and cell == 0:
                counter += 1
                if counter > 1:
                    return False
            else:
                return False
        
        if not exact:
            return counter == 1
        else:
            return True