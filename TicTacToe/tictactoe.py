#TicTacToe game with computer agents

size = 10
board = [' ' for x in range(size)] #Create a board of a specific size.
 
def displayBoard():
    print("\n*********")
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("*********\n")
 
def winState(brd, gp): #Check each row, column, and diagonal on the board for three game pieces in a row.
    return ((brd[1] == gp) and (brd[2] == gp) and (brd[3] == gp) or 
            (brd[4] == gp) and (brd[5] == gp) and (brd[6] == gp) or 
            (brd[7] == gp) and (brd[8] == gp) and (brd[9] == gp) or 
            (brd[1] == gp) and (brd[4] == gp) and (brd[7] == gp) or 
            (brd[2] == gp) and (brd[5] == gp) and (brd[8] == gp) or 
            (brd[3] == gp) and (brd[6] == gp) and (brd[9] == gp) or 
            (brd[1] == gp) and (brd[5] == gp) and (brd[9] == gp) or 
            (brd[3] == gp) and (brd[5] == gp) and (brd[7] == gp))
  
def emptySpace(pos):
    return board[pos] == ' '

def claimSpace(gamePiece, pos):
    board[pos] = gamePiece

def noMoves(board):
    if board.count(' ') == 0:
        return True
    else:
        return False

def playerTurn(player):
    valid = True
    while valid:
        move = input("Please enter a number to claim a space (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if emptySpace(move):
                    valid = False
                    claimSpace(player, move)
                else:
                    print("A player has already claimed that space. Please choose another.")
            else:
                print("Please enter a number between 1 and 9.")
        except:
            print("Please enter an integer.")
        
def game():
    #Main game loop
    player = 'X'
    cpu = 'O'
    playerWin = 0
    cpuWin = 0
    ties = 0

    # print("X's always go first.")
    # initiative = input("Would You like to play as X's or O's? (X/O)")

    # if initiative == 'X':
    #     player = 'X'
    #     cpu = 'O'
    # else:
    #     cpu = 'X'
    #     player = 'O'

    displayBoard()
 
    while not(noMoves(board)):
        if not(winState(board, cpu)):
            playerTurn(player)
            displayBoard()
        else:
            cpuWin+=1
            print("Computer won!")
            break
       
        if not(winState(board, player)):
            move = cpuTurn()
            if move == 0:
                ties+=1
                print("Tie game, there are no remaining spaces.")
            else:
                claimSpace(cpu, move)
                print("Computer placed", cpu, "in space ", move)
                displayBoard()
        else:
            playerWin+=1
            print("You won!")
            break
 
    print("Player wins:", playerWin)
    print("Computer wins:", cpuWin)
    print("Ties:", ties)

def main():

    game()

main()