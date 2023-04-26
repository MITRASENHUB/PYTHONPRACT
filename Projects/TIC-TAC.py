import random

#Set the board

board=["-","-","-",
        "-","-","-",
        "-","-","-"]
current_player= "X"
winner=None
gameRunning=True

#Printing the board

def printBoard (board):
    print( board[0]  + " | " +  board[1]  +  " | "  + board[2] )
    print("----------")
    print( board[3]  + " | " +  board[4]  +  " | "  + board[5] )
    print("----------")
    print( board[6]  + " | " +  board[7]  +  " | "  + board[8] )        

#printBoard(board)

#Take player input
def playerInput(board):
    inp=int(input("Please put a number from 1-9 :>   "))
    if inp>=1 and inp<=9 and board [inp-1]=="-":
        board[inp-1]=current_player
    else:
        print("Oops player is already in that spot ! ")

#Check for win or tie
def checkHorizontal(Board):
    global winner
    if board[0]==board[1] and board[1]==board[2] and board [1] != "-" :
        winner=board[0]
        return True
    elif board[3]==board[4] and board==[5] and board [3] != "-" :
        winner=board[3]
        return True
    elif board[6]==board[7] and board==[8] and board [6] != "-" :
        winner=board[6]
        return True
    
def checkRow (Board):
    global winner
    if board[0]==board[3] and board==[6] and board [0] != "-" :
        winner=board[0]
        return True
    elif board[1]==board[4] and board==[7] and board [1] != "-" :
        winner=board[3]
        return True
    elif board[2]==board[5] and board==[8] and board [2] != "-" :
        winner=board[2]
        return True

def checkDiagonal (Board):
    global winner
    if board[0]==board[4] and board==[8] and board [0] != "-" :
        winner=board[0]
        return True
    elif board[2]==board[4] and board==[6] and board [1] != "-" :
        winner=board[2]
        return True

def checkTie (board) :
    global gameRunning
    if"-"not in board : 
        printBoard(board)
        print("it is a tie !")
        gameRunning=False

def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"the winner is {winner}")
        return True
    return False
     

#Switch the player
def SwitchPlayers():
    global current_player
    if current_player=="X":
        current_player="0"
    else:
        current_player="X"

def computer (board) : 
        while current_player=="0":
             position= random.randint(0,8)
             if board [position]=="-":
                board[position]="0"
                SwitchPlayers()


#Check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    if checkWin( ):
        break
    checkTie(board)
    SwitchPlayers()
    computer(board)
    if checkWin( ):
        break
    checkTie(board)
    