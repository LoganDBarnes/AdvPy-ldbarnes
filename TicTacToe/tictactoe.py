#TicTacToe game with computer agents
#Based on code presented in YouTube video Python TIC TAC TOE Tutorial | Beginner Friendly Tutorial by Code Coach
#Source code availiable at https://github.com/watsojar/tictactoe/blob/main/tictactoePart1Finished.py

#Not finished - see README

import random
#from board import Board

player = 'X'
cpu = 'O'
currTurn = 'X'
winner = None
isRunning = True
playerWin = 0
cpuWin = 0
ties = 0

size = 10
board : int = [' ' for x in range(size)] #Create a board of a specific size.

def displayBoard(board):
    print("\n*********")
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("*********\n")

def playerTurn(board):
    move = int(input("Please enter a number to claim a space (1-9): "))
    if board[move] == " ":
        board[move] = currTurn
    else:
        print("A player has already claimed that space. Please choose another.")
        switchPlayer()

# def noMoves(board):
#     if ' ' not in board:
#         return True
#     else:
#         return False

def winState(board): #Check each row, column, and diagonal on the board for three game pieces in a row.
    brd = board
    global winner

    if brd[1] == brd[2] == brd[3] and brd[2] != ' ': #rows
        winner = brd[2]
        return True
    elif brd[4] == brd[5] == brd[6]and brd[5] != ' ':
        winner = brd[5]
        return True
    elif brd[7] == brd[8] == brd[9]and brd[8] != ' ':
        winner = brd[8]
        return True
    elif brd[1] == brd[4] == brd[7]and brd[4] != ' ': #columns
        winner = brd[4]
        return True
    elif brd[2] == brd[5] == brd[8]and brd[5] != ' ':
        winner = brd[5]
        return True
    elif brd[3] == brd[6] == brd[9]and brd[6] != ' ':
        winner = brd[6]
        return True
    elif brd[1] == brd[5] == brd[9]and brd[5] != ' ': #diagonals
        winner = brd[5]
        return True 
    elif brd[3] == brd[5] == brd[7]and brd[5] != ' ':
        winner = brd[5]
        return True

def checkIfWinOrTie(board):
    global isRunning
    global playerWin
    global cpuWin
    global ties

    if winState(board):
        displayBoard(board)
        print(f"The winner is {winner}!")
        isRunning = False

    elif ' ' not in board:
        displayBoard(board)
        ties+=1
        print("Tie Game!")
        isRunning = False

def switchPlayer():
    global currTurn
    if currTurn == "X":
        currTurn = "O"
    else:
        currTurn = "X"

def cpuRand(board):
    while currTurn == "O" and isRunning:
        position = random.randint(1, 9)
        if board[position] == " ":
            board[position] = "O"
            switchPlayer()

#def cpuHard(board):

def main():

    global isRunning
    global playerWin
    global cpuWin
    global ties
    
    while isRunning:
        displayBoard(board)
        playerTurn(board)
        checkIfWinOrTie(board)
        switchPlayer()
        cpuRand(board)
        checkIfWinOrTie(board)

        if winner == player:
            playerWin+=1
            print("You won!")
        elif winner == cpu:
            cpuWin+=1
            print("Computer won!")

        print("Player wins: ", playerWin)
        print("Computer wins: ", cpuWin)
        print("Ties: ", ties)

main()