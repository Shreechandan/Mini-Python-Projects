import random

board = ["_", "_", "_",
       "_", "_","_",
       "_","_","_"]
currentplayer ="x"
winner = None
gameRunning = True



def printboard(board):
    print(board[0] + " | " + board[1] + " | " +board[2])
    print("----------")
    print(board[0] + " | " + board[4] + " | " +board[5])
    print("----------")
    print(board[0] + " | " + board[7] + " | " +board[8])
printboard(board)   

def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "_":
        board[inp - 1] = currentplayer
    else:
        print("Oops! The spot is already taken.")

        
def CheckHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] !="-":
        winner = board[0]
        return True   
    elif board[3] == board[4] == board[5] and board[3] !="-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] !="-":
        winner = board[6]
        return True
    
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] !="-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] !="-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] !="-":
        winner = board[2]
        return True 
    
    
def checkDiag(board):
    global winner       
    if board[0] == board[4] == board[8] and board[0] !="-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] !="-":
        winner = board[2]
        return True 
    
    
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printboard(board)
        print("It is a tie!")
        gameRunning = False 


def checkWin():
    if checkDiag(board) or CheckHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")
        
        
        
        
        
def switchPlayer():
    global currentplayer
    if currentplayer == "x":
        currentplayer = "o"
    else:
        currentplayer = "x" 
        
def computer(board):
    while currentplayer == "o":
        position= random.randint(0, 8)
        if board[position] =="_":
           board[position] =="o"
           switchPlayer()      
        
        
        
        
while gameRunning:
    printboard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()           
                          
        
        
              
