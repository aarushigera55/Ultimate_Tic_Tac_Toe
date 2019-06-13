#!/usr/bin/python3




'''
ALPHABETA PRUNING ALGORITHM:

Alpha-Beta pruning is adversarial search algorithm, an optimization technique for minimax algorithm. It is called Alpha-Beta
pruning because it passes 2 extra parameters in the minimax function, namely alpha and beta. The Min and Max nodes are there
because we want to maximise the score of our move and minimize the score of the opponent's move. Alphabeta reduces the computation time
by a huge factor. This allows us to search much faster and even go into deeper levels in the game tree. While traversing the alphabeta
algorithm, it changes the value of alpha if returning node is a max node and changes the value of beta while returning to a min node. It
cuts off branches in the game tree which need not be searched because there already exists a better move available. A better move is
defined when value of alpha becomes greater than value of beta. It stops evaluating a move when at least one possibility has been found
that proves the move to be worse than a previously examined move.


ALPHA-BETA PRUNING FUNCTIONING:
1.	Initialize alpha = -infinity and beta = infinity as the worst possible cases. The condition to prune a node is when alpha becomes
greater than or equal to beta.
2.	Starts with assigning the initial values of alpha and beta to root and since alpha is less than beta we don’t prune it.
3.	Carry these values of alpha and beta to the child node on the left till we reach the leftmost terminal node. We calculate the
utility value of the terminal node and return this to it's parent. If the parent is a max node, we change the value of alpha as maximum
of previous value of alpha and the value of the child (alpha= MAX(alpha, returned_val)). If the parent is a min node, we change the
value of beta as minimum of the previous value of beta and the returned value of the child (beta = MIN(beta, returned_val)).
4. Now we check if the value of alpha is greater than or equal to the value of beta, if this is so, we prune the right child and return
alpha if the current node was a Max node or beta if the current node was Min node.
5. If the value of alpha is less than value of beta, we copy these new values of alpha and beta to the child node and recursively call
the alpha-beta algorithm to work on this again.
6. Doing this recursively, we finally get the value for root node. We usually start root node as MAX node because we want to maximise our
value, hence finally, alpha will be the true value of root node, which is returned from the algorithm as the final value


ANSWER TO THE QUESTION: WORKING OF OUR PROGRAM

Our code executes AlphaBeta Algorithm to solve this 9 grid Tic Tac Toe.
For each move, the main function calls parse whice decodes the action to be taken.
If the action is next_move, call the play() function. In the play function, we are calculating the number of moves as variable move
and deepcopy the board as boards_copy. We check if the move is less than 10.

If it is, we call the move_before_10 function passing boards_copy
and corners_new variable having the corners as parameters. In the move_before_10() function, we make a list of indices where no player has
played yet. After this, we check for each element in these indices, if there is a winning move, if there is, we go for it and win the game.
If not, we check if there is a winning move for the human player X, if there is, we play there to hinder him from winning.
If not this, we also check for each move, if there is a winning condition for X in the next to be current board, if there is, we
remove that index from the list if indices so we dont play there and X doesnt win on the next move. Next we check if the length of indices
is 9, if it is, means the whole board is empty, so we randomly pick any corner as playing in the corner will open maximum number of branches
for the human player. If the length of indices available is not equal to 9, we remove from the corner_new list, the corners that have been
played and are not empty. If after this, the length of corner_list is 1, we randomly pick any element from the list of avaiable indices,
otherwise, we randomly pick from the list of corner_new.

 If move is greater than 10, our play() function calls minimax() function. This function checks which player's actual is it and in turn
 assigns, player_ variable the value of the other player. Now, it checks for the available indices in the current board where the computer
 can play. It next checks, if the current board is empty, if it is, it checks for each position on the board, if there is a winning position
 for X in the next to be current board, if there is, it removes that position from the list of available indices  and the list of corners
 and randomly returns any corners. If the current board ain't empty, for each element in the available indices, it checks for the winning
 position of O, if there is, it returns to win the game, else it checks for the winning position for X, if there is, it returns that position
 to prevent X from winning next time, else, it checks, if there a winning position for X in next to be current board and removes it from the
 list of available indices if there is. It then calls the alpha_beta function to work on alphabeta algorithm.

 The alphabeta function first checks if the game is won by either X or O already or if the board has completed cells and has been drawn or
 if the depth of the branches has reached a zero point, if either of this case is true, it calculates the value of winning cases of
 X in the current board, the value of winning cases of O in the current board by calling the check_val() function for both and finally
 subtracting the value of winnings of X from winnings of O to get the score and returns the score.
 If the neither of the above conditions are satisfied, it checks for the indices where no player has played and calculates player_ just like
 in minimax() function. Now for all the available positions in the indices_new list, one by one, it marks the board with the player value .
 Now it checks if the minmax variable value if "max" or "min" as passed to the alphabeta function(). If the minmax value if "max", it
 checks for "min" next or if it is "min", it checks for "max"-  what will happen next by recursively calling alphabeta function. The
 recursive call to the alpha_beta() function traverses the MINMAX tree to get the values of alpha and beta for the algorithm. Finally,
 when the base case is reached and score is returned, for the minmax = "max", the alpha value will be changed as the maximum of score and
 the previous alpha value. It checks the pruning condition, i.e. if the alpha value becomes greater than the beta value, it prunes
 by returning the alpha value. If the minmax value at the time of calling was "min", it will change the beta value to minimum of previous
 beta value. It again checks for the pruning condition being, if alpha value is greater than beta, it prunes by returning the alpha value.
 Finally, if it was not pruned, it returns the alpha value if the player was 1 or beta value if the player was 2. Finally, after all the
 recursions, the final value is returned back to the minimax function in the dictionary value for each available index.

 Finally, after all the indices have their values from alpha_beta() function, we find the index value for which this alpha_beta score was
 maximum and return this index value to the play function which stores it in variable n. Finally, the play function after calling either
 move_before_10() or minimax() functions, returns the value of n as the best possible next move of the Computer O.

'''




# Sample starter bot by Zac Partridge
# Sample used by Aarushi and Shamine

import socket
import sys
import numpy as np
import copy
import math
import random

# a board cell can hold:
#   0 - Empty
#   1 - I played here
#   2 - They played here

# the boards are of size 10 because index 0 isn't used
boards = np.zeros((10, 10), dtype="int8")
s = [".","X","O"]
curr = 0 # this is the current board to play in
move = 2
win = 0
move = 2
pos = 0
depth = 0
corner= [1, 3, 9, 7]


# print a row
# This is just ported from game.c
def print_board_row(board, a, b, c, i, j, k):
    print(" "+s[board[a][i]]+" "+s[board[a][j]]+" "+s[board[a][k]]+" | " \
             +s[board[b][i]]+" "+s[board[b][j]]+" "+s[board[b][k]]+" | " \
             +s[board[c][i]]+" "+s[board[c][j]]+" "+s[board[c][k]])

# Print the entire board
# This is just ported from game.c
def print_board(board):
    print_board_row(board, 1,2,3,1,2,3)
    print_board_row(board, 1,2,3,4,5,6)
    print_board_row(board, 1,2,3,7,8,9)
    print(" ------+-------+------")
    print_board_row(board, 4,5,6,1,2,3)
    print_board_row(board, 4,5,6,4,5,6)
    print_board_row(board, 4,5,6,7,8,9)
    print(" ------+-------+------")
    print_board_row(board, 7,8,9,1,2,3)
    print_board_row(board, 7,8,9,4,5,6)
    print_board_row(board, 7,8,9,7,8,9)
    print()

def check_horizontal_complete(board_line): #Base Case when the game is won by either player in Horizontal side
    global win
    for i in range(1,10,3):
        if board_line[i] ==1 and board_line[i+1]==1 and board_line[i+2] ==1:
            win = 1
            return win


    for i in range(1,10,3):
        if board_line[i] ==2 and board_line[i+1]==2 and board_line[i+2] ==2:
            win = 2
            return win
    return win


def check_vertical_complete(board_line): #Base Case when the game is won by either player in Vertical side
    global win
    for i in range(1,10):
        if(i+6 > 9):
            break
        else:
            if board_line[i] ==1 and board_line[i+3]==1 and board_line[i+6] ==1:
                win = 1
                return win


    for i in range(1,10):
        if(i+6 > 9):
            break
        else:
            if board_line[i] ==2 and board_line[i+3]==2 and board_line[i+6] ==2:
                win = 2
                return win

    return win


def check_going_right_diagonal_complete(board_line): #Base Case when the game is won by either player in diagonal side going down on the right
    global win
    for i in range(1,10):
        if i+8 > 9:
            break
        else:
            if board_line[i] ==1 and board_line[i+4]==1 and board_line[i+8] ==1:
                win = 1
                return win
        i += 4

    for i in range(1,10):
        if i+8 > 9:
            break
        else:
            if board_line[i] ==2 and board_line[i+4]==2 and board_line[i+8] ==2:
                win = 2
                return  win
        i += 4
    return win


def check_going_left_diagonal_complete(board_line): #Base Case when the game is won by either player in diagonal side going down on the left
    global win
    for i in range(3,10):
        if i+4 > 9:
            break
        else:
            if board_line[i] ==1 and board_line[i+2]==1 and board_line[i+4] ==1:
                win = 1
                break
        i += 4
    return win

def check_board_complete(board_line): #Base case to check draw condition
    if 0 not in board_line[1:]:
        return 1
    return 0


# To know the winning move in either horizontal, vertical or diagonal
def get_winning_position(boards_line, p):

    #horizontal condition
    for i in range(1,len(boards_line),3):
        if i+2 > 9:
            break
        if boards_line[i] == p and boards_line[i + 1] == p and boards_line[i + 2] == 0:
            return i+2
        if boards_line[i] == p and boards_line[i + 1] == 0 and boards_line[i + 2] == p:
            return i+1
        if boards_line[i] == 0 and boards_line[i + 1] == p and boards_line[i + 2] == p:
            return i


    # vertical condition
    for i in range(1,len(boards_line)):
        if i+6 > 9:
            break
        if boards_line[i] == p and boards_line[i+3] == p and boards_line[i+6] == 0:
            return i+6
        if boards_line[i] == p and boards_line[i+3] == 0 and boards_line[i+6] == p:
            return i+3
        if boards_line[i] == 0 and boards_line[i+3] == p and boards_line[i+6] == p:
            return i


    # diagonal condition LtR
    for i in range(1,len(boards_line),2):
        if i+8 > 9:
            break
        if boards_line[i] == p and boards_line[i+4] == p and boards_line[i+8] == 0:
            return i+8
        if boards_line[i] == p and boards_line[i+4] == 0 and boards_line[i+8] == p:
            return i+4
        if boards_line[i] == 0 and boards_line[i+4] == p and boards_line[i+8] == p:
            return i



    # diagonal conditions RtL
    for i in range(1, len(boards_line), 3):
        if i+6 > 9:
            break
        if boards_line[i + 2] == p and boards_line[i + 4] == p and boards_line[i + 6] == 0:
            return i+6
        if boards_line[i + 2] == p and boards_line[i + 4] == 0 and boards_line[i + 6] == p:
            return i+4
        if boards_line[i + 2] == 0 and boards_line[i + 4] == p and boards_line[i + 6] == p:
            return i

    return 0

# To help calculate the score
def check_val(boards_line,p):
    val = 0
    #horizontal win conditions
    for i in range(1,len(boards_line),3):
        if i+2 > 9:
            break
        if boards_line[i] == p and boards_line[i+1] == p and boards_line[i+2] == p :
            val += 1
        if boards_line[i] == p and boards_line[i+1] == p and boards_line[i+2] == 0:
            val += 1
        if boards_line[i] == p and boards_line[i+1] == 0 and boards_line[i+2] == p:
            val += 1
        if boards_line[i] == 0 and boards_line[i+1] == p and boards_line[i+2] == p:
            val += 1
        if boards_line[i] == p and boards_line[i+1] == 0 and boards_line[i+2] == 0:
            val += 1
        if boards_line[i] == 0 and boards_line[i+1] == p and boards_line[i+2] == 0:
            val += 1
        if boards_line[i] == 0 and boards_line[i+1] == 0 and boards_line[i+2] == p:
            val += 1

    #vertical win conditions
    for i in range(1,len(boards_line)):
        if i+6 > 9:
            break
        if boards_line[i] == p and boards_line[i+3] == p and boards_line[i+6] == p :
            val += 1
        if boards_line[i] == p and boards_line[i+3] == p and boards_line[i+6] == 0:
            val += 1
        if boards_line[i] == p and boards_line[i+3] == 0 and boards_line[i+6] == p:
            val += 1
        if boards_line[i] == 0 and boards_line[i+3] == p and boards_line[i+6] == p:
            val += 1
        if boards_line[i] == p and boards_line[i+3] == 0 and boards_line[i+6] == 0:
            val += 1
        if boards_line[i] == 0 and boards_line[i+3] == p and boards_line[i+6] == 0:
            val += 1
        if boards_line[i] == 0 and boards_line[i+3] == 0 and boards_line[i+6] == p:
            val += 1

    #diagonal_1 win conditions
    for i in range(1,len(boards_line),2):
        if i+8 > 9:
            break
        if boards_line[i] == p and boards_line[i+4] == p and boards_line[i+8] == p :
            val += 1
        if boards_line[i] == p and boards_line[i+4] == p and boards_line[i+8] == 0:
            val += 1
        if boards_line[i] == p and boards_line[i+4] == 0 and boards_line[i+8] == p:
            val += 1
        if boards_line[i] == 0 and boards_line[i+4] == p and boards_line[i+8] == p:
            val += 1
        if boards_line[i] == p and boards_line[i+4] == 0 and boards_line[i+8] == 0:
            val += 1
        if boards_line[i] == 0 and boards_line[i+4] == p and boards_line[i+8] == 0:
            val += 1
        if boards_line[i] == 0 and boards_line[i+4] == 0 and boards_line[i+8] == p:
            val += 1

    #diagonal_2 win conditions
    for i in range(1,len(boards_line),3):
        if i+6 > 9:
            break
        if boards_line[i+2] == p and boards_line[i+4] == p and boards_line[i+6] == p :
            val += 1
        if boards_line[i+2] == p and boards_line[i+4] == p and boards_line[i+6] == 0:
            val += 1
        if boards_line[i+2] == p and boards_line[i+4] == 0 and boards_line[i+6] == p:
            val += 1
        if boards_line[i+2] == 0 and boards_line[i+4] == p and boards_line[i+6] == p:
            val += 1
        if boards_line[i+2] == p and boards_line[i+4] == 0 and boards_line[i+6] == 0:
            val += 1
        if boards_line[i+2] == 0 and boards_line[i+4] == p and boards_line[i+6] == 0:
            val += 1
        if boards_line[i+2] == 0 and boards_line[i+4] == 0 and boards_line[i+6] == p:
            val += 1

    return val

def alpha_beta(boards_copy, depth, player, alpha, beta, minmax): #alpha_beta function that returns the best score for alpha to minimax algo
    global curr
    if depth == 0 or check_board_complete(boards_copy[curr]) or check_horizontal_complete(
            boards_copy[curr]) or check_vertical_complete(boards_copy[curr]) or check_going_right_diagonal_complete(
        boards_copy[curr]) or check_going_left_diagonal_complete(boards_copy[curr]): #if depth = 0 or match draw or winning condition,
        # calculate and return score
        val_X = check_val(boards_copy[curr], 2)
        val_O = check_val(boards_copy[curr], 1)
        score = val_O - val_X
        return score


    indices_new = []
    for i in range(1, len(boards_copy[curr])):
        if boards_copy[curr][i] == 0:
            indices_new.append(i)

    player_ = 0
    score = 0

    if player == 1:
        player_ = 2
    elif player == 2:
        player_ = 1

    for e in indices_new:
        boards_copy[curr][e] = player
        curr = e
        if minmax == 'max':
            score_val = alpha_beta(boards_copy, depth - 1, player_, alpha, beta, minmax = 'min')
            alpha = max(score_val, alpha)
            if alpha >= beta:
                return alpha
        elif minmax == 'min':
            score_val = alpha_beta(boards_copy, depth - 1, player_, alpha, beta, minmax='max')
            beta = min(score_val, beta)
            if alpha >= beta:
                return beta

    if player == 1:
        return alpha
    elif player == 2:
        return beta

# minimax algo returns the computer's move after 10th count move
def minimax(boards_copy, depth, player, alpha, beta, minmax):
    if player == 1:
        player_ = 2
    elif player == 2:
        player_ = 1

    indices = []
    for i in range(1, len(boards_copy[curr])):
        if boards_copy[curr][i] == 0:
            indices.append(i)

    if all([boards_copy[curr][i] ==0 for i in range(len(boards_copy[curr]))]):
        for e in corner:
            pos_next = get_winning_position(boards_copy[e], 2)
            if pos_next > 0:  # There is a winning condition for X in the next to be current board
                indices.remove(e)
                corner.remove(e)
        n = random.choice(corner)
        return n

    index_dict = {}

    for e in indices:
        pos_next = get_winning_position(boards_copy[e], player_)
        pos = get_winning_position(boards_copy[curr], player)
        pos_ = get_winning_position(boards_copy[curr], player_)

        if pos_next > 0:  # There is a winning condition for X in the next to be current board
            indices.remove(e)

        if pos > 0: #There is a winning condition for O in the current board
            return pos

        elif pos_ > 0: #There is a winning condition for X in the current board hence we should play there first
            return pos_


        index_dict[e] = alpha_beta(boards_copy, depth, player, alpha , beta, minmax)

    key_max = max(index_dict.keys(), key=(lambda k: index_dict[k]))
    return key_max


#move_before_10 function to return computer's move before the 10th move
def move_before_10(boards_copy, corner_new):
    indices_before_10 = []
    for i in range(1, len(boards_copy[curr])):
        if boards_copy[curr][i] == 0:
            indices_before_10.append(i)

    # Create a list of empty spaces - possible moves
    for e in indices_before_10:
        pos_next = get_winning_position(boards_copy[e], 2)
        pos = get_winning_position(boards_copy[curr], 1)
        pos_ = get_winning_position(boards_copy[curr], 2)

        if pos_next > 0:  # There is a winning condition for X in the next to be current board
            indices_before_10.remove(e)
            if e in corner_new:
                corner_new.remove(e)

        if pos > 0:  # There is a winning condition for O in the current board
            return pos
        elif pos_ > 0:  # There is a winning condition for X in the current board hence we should play there first
            return pos_

    if len(indices_before_10)==9:
        n = random.choice(corner_new)
        return n

    else:
        for e in corner_new:
            if boards_copy[curr][e] != 0:
                corner_new.remove(e)

        if len(corner_new) == 1:
            n = random.choice(indices_before_10)
            return n

        else:
            n = random.choice(corner_new)
            return n

def play():
    global move
    move += 1
    boards_copy = copy.deepcopy(boards)

    if move > 10: # >10 means move = 11 that has already happened-----was by X---> hence we call minimax for the 12th move by Computer
        n = minimax(boards_copy, depth = 6, player = 1, alpha = -math.inf, beta = math.inf, minmax = 'max')

    else: # move is less than or equal to the 10th move hence it calls the move_before_10 function to reduce time complexity otherwise calling
                                #minimax directly will increase the number of branches and hence the complexity.
        corner_new = [1, 3, 9, 7]
        n = move_before_10(boards_copy, corner_new)

    place(curr, n, 1)
    return n # finally the move to be taken by the computer returned




# place a move in the global boards
def place(board, num, player):
    global curr #current board
    curr = num
    boards[board][num] = player



# read what the server sent us and
# only parses the strings that are necessary
def parse(string):
    if "(" in string:
        command, args = string.split("(")
        args = args.split(")")[0]
        args = args.split(",")
    else:
        command, args = string, []

    if command == "second_move":
        place(int(args[0]), int(args[1]), 2)
        return play()
    elif command == "third_move":
        # place the move that was generated for us
        place(int(args[0]), int(args[1]), 1)
        # place their last move
        place(curr, int(args[2]), 2)
        return play()
    elif command == "next_move":
        place(curr, int(args[0]), 2)
        return play()
    elif command == "win":
        return -1
    elif command == "loss":
        return -1
    return 0

# connect to socket
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(sys.argv[2]) # Usage: ./agent.py -p (port)
    s.connect(('localhost', port))
    while True:
        text = s.recv(1024).decode()
        if not text:
            continue
        for line in text.split("\n"):
            response = parse(line)
            if response == -1:
                s.close()
                return
            elif response > 0:
                s.sendall((str(response) + "\n").encode())
if __name__ == "__main__":
    main()


#cmd= ./servt -p 12345 -x

#-p "12345"  - config