import numpy as np
import copy as cp

def get_best_move(c4, player, evaluate, depth = 4):
    return minimax(c4, player, depth, -np.inf, np.inf, evaluate)[1]


def minimax(c4, player, depth, alpha, beta, evaluate):
    moves = c4.get_valid_moves_Karim2()

    best_move = -1

    if depth == 0 or len(moves) == 0 or c4.is_gameover(player):
        return [evaluate(c4), best_move]

    for move in moves:
        if c4.c[move[0],move[1]]==5:
            continue
        tmp=c4.c[move[0],move[1]]
        c4.c[move[0],move[1]]=4
        new_game = cp.deepcopy(c4)
        new_game.move(move[0], move[1], player)
        
        next_player = 2 if player == 1 else 1
        temp = minimax(new_game, next_player, depth - 1, alpha, beta, evaluate)[0]
        c4.c[move[0],move[1]]=tmp
        # player 1 -> MAX
        if player == 1:
            if temp > alpha:
                alpha = temp
                best_move = move
        # player 2 -> MIN
        else:
            if temp < beta:
                beta = temp
                best_move = move

        if alpha >= beta:
            break

    return [alpha if player == 1 else beta, best_move]

def fav1(c4):
    return c4.nlinhas4(1) - c4.nlinhas4(2)
def fav2(c4):
    return 100*fav1(c4) + c4.nlinhas3(1) - c4.nlinhas3(2)
def fav3(c4):
    return 100*fav1(c4) + c4.central(1) - c4.central(2)
def fav4(c4):
    return 5*fav2(c4) + fav3(c4)
