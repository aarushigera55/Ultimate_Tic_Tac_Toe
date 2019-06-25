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

WORKING OF OUR PROGRAM:

Our code executes AlphaBeta Algorithm to solve this 9 grid Tic Tac Toe.
For each move, the main function calls parse whice decodes the action to be taken.
If the action is next_move, call the play() function. In the play function, we are calculating the number of moves as variable move and deepcopy the board as boards_copy. We check if the move is less than 10.
If it is, we call the move_before_10 function passing boards_copy and corners_new variable having the corners as parameters. In the move_before_10() function, we make a list of indices where no player has played yet. After this, we check for each element in these indices, if there is a winning move, if there is, we go for it and win the game.
If not, we check if there is a winning move for the human player X, if there is, we play there to hinder him from winning.
If not this, we also check for each move, if there is a winning condition for X in the next to be current board, if there is, we remove that index from the list if indices so we dont play there and X doesnt win on the next move. Next we check if the length of indices is 9, if it is, means the whole board is empty, so we randomly pick any corner as playing in the corner will open maximum number of branches for the human player. If the length of indices available is not equal to 9, we remove from the corner_new list, the corners that have been played and are not empty. If after this, the length of corner_list is 1, we randomly pick any element from the list of avaiable indices, otherwise, we randomly pick from the list of corner_new.
 If move is greater than 10, our play() function calls minimax() function. This function checks which player's actual is it and in turn assigns, player_ variable the value of the other player. Now, it checks for the available indices in the current board where the computer can play. It next checks, if the current board is empty, if it is, it checks for each position on the board, if there is a winning position for X in the next to be current board, if there is, it removes that position from the list of available indices  and the list of corners and randomly returns any corners. If the current board ain't empty, for each element in the available indices, it checks for the winning position of O, if there is, it returns to win the game, else it checks for the winning position for X, if there is, it returns that position to prevent X from winning next time, else, it checks, if there a winning position for X in next to be current board and removes it from the list of available indices if there is. It then calls the alpha_beta function to work on alphabeta algorithm. The alphabeta function first checks if the game is won by either X or O already or if the board has completed cells and has been drawn or if the depth of the branches has reached a zero point, if either of this case is true, it calculates the value of winning cases of
 X in the current board, the value of winning cases of O in the current board by calling the check_val() function for both and finally subtracting the value of winnings of X from winnings of O to get the score and returns the score.
 If the neither of the above conditions are satisfied, it checks for the indices where no player has played and calculates player_ just like in minimax() function. Now for all the available positions in the indices_new list, one by one, it marks the board with the player value .
 Now it checks if the minmax variable value if "max" or "min" as passed to the alphabeta function(). If the minmax value if "max", it checks for "min" next or if it is "min", it checks for "max"-  what will happen next by recursively calling alphabeta function. The recursive call to the alpha_beta() function traverses the MINMAX tree to get the values of alpha and beta for the algorithm. Finally, when the base case is reached and score is returned, for the minmax = "max", the alpha value will be changed as the maximum of score and the previous alpha value. It checks the pruning condition, i.e. if the alpha value becomes greater than the beta value, it prunes by returning the alpha value. If the minmax value at the time of calling was "min", it will change the beta value to minimum of previous beta value. It again checks for the pruning condition being, if alpha value is greater than beta, it prunes by returning the alpha value.
 Finally, if it was not pruned, it returns the alpha value if the player was 1 or beta value if the player was 2. Finally, after all the recursions, the final value is returned back to the minimax function in the dictionary value for each available index.
 Finally, after all the indices have their values from alpha_beta() function, we find the index value for which this alpha_beta score was maximum and return this index value to the play function which stores it in variable n. Finally, the play function after calling either move_before_10() or minimax() functions, returns the value of n as the best possible next move of the Computer O.


# Ultimate_Tic_Tac_Toe
Ultimate Tic-Tac-Toe is a board game composed of nine tic-tac-toe boards arranged in a 3-by-3 grid. In the game implemented here, players take turns playing in the smaller tic-tac-toe boards until one of them wins in the either of the smaller boards.

Introduction

In this project I wrote an agent to play the game of Nine-Board Tic-Tac-Toe.

This game is played on a 3 x 3 array of 3 x 3 Tic-Tac-Toe boards. The first move is made by placing an X in a randomly chosen cell of a randomly chosen board. After that, the two players take turns placing an O or X alternately into an empty cell of the board corresponding to the cell of the previous move. (For example, if the previous move was into the upper right corner of a board, the next move must be made into the upper right board.)

The game is won by getting three-in-a row either horizontally, vertically or diagonally in one of the nine boards. If a player is unable to make their move (because the relevant board is already full) the game ends in a draw.


Getting Started

Download and store all the files to src folder

Then type in terminal:

cd src
make all

./servt -x -o

You should then see something like this:


 . . . | . . . | . . .
 
 . . . | . . . | . . .
 
 . . . | . . . | . . .
 ----+---+----
 . . . | . . . | . . .
 . . . | . . . | . . .
 . . . | . . x | . . .
 ----+---+----
 . . . | . . . | . . .
 . . . | . . . | . . .
 . . . | . . . | . . .
 
 

next move for O ? 
You can now play Nine-Board Tic-Tac-Toe against yourself, by typing a number for each move. 
The cells in each board are numbered 1, 2, 3, 4, 5, 6, 7, 8, 9 as follows:
+-----+
|1 2 3|
|4 5 6|
|7 8 9|
+-----+

To play against a computer player, you need to open another terminal window (and cd to the src directory).

Type this into the first window:

./servt -p 12345 -x
This tells the server to use port 12345 for communication, and that the moves for X will be chosen by you, the human, typing at the keyboard. (If port 12345 is busy, choose another 5-digit number.)
You should then type this into the second window (using the same port number):

./randt -p 12345
The program randt simply chooses each move randomly among the available legal moves.


lookt is a slightly more sophisticated player which was given in the question to compare results.
You can play against lookt by typing this into the second window:

./lookt -p 12345

(If you are using a Mac, type ./lookt.mac instead of ./lookt)
To play two computer programs against each other, you may need to open three windows. For example, to play agent against lookt using port 54321, type as follows:

window 1:	./servt -p 54321
window 2:	./agent -p 54321
window 3:	./lookt -p 54321

(Whichever program connects first will play X; the other program will play O.)
Alternatively, you can launch all three programs from a single window by typing

./servt -p 54321 &
./agent -p 54321 &
./lookt -p 54321

Writing a Player

My task was to write a program to play the game of nine-board tic-tac-toe as well as I can.
My program receives commands from the server (init, start(), second_move(), third_move(), last_move(), win(), loss(), draw(), end()) and sends back a single digit specifying the chosen move.
