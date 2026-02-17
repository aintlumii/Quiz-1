board = [" "] * 9
player = "X"
mainGame = True


def printBoard():
    print("| " + board[0] + " | " + board[1] + " | " + board[2]+" |")
    print('-------------')
    print("| " + board[3] + " | " + board[4] + " | " + board[5]+" |")
    print('-------------')
    print("| " + board[6] + " | " + board[7] + " | " + board[8]+" |")

def moveInput():
    global player
    try:
        inp = int(input(f"Player {player}, select spot 1-9: ")) - 1
        if 0 <= inp <= 8 and board[inp] == " ":
            board[inp] = player
            return True
        else:
            print("SPOT ALREADY TAKEN OR INVALID!")
            return False
    except ValueError:
        print("ENTER A VALID NUMBER!")
        return False

def checkWin():
    winConditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    
    for condition in winConditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]]
    return None

def checkTie():
    return " " not in board

while mainGame:
    printBoard()
    
    if not moveInput():
        continue 
    
    winner = checkWin()
    if winner:
        printBoard()
        print(f"NICE G, Player {winner}!")
        mainGame = False
    elif checkTie():
        printBoard()
        print("NICE G, TIE LNG!")
        mainGame = False
    else:
        if player == "X":
            player = "O"
        else:
            player = "X"