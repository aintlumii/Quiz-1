import tkinter as tk
import random

def nextTurn(row, column):
    global player
    
    if buttons[row][column]['text'] == " " and checkWin() is False:
       
        if player == players[0]:  
            buttons[row][column]['text'] = player

            if checkWin() is False:
                player = players[1]
                label.config(text=(players[1] + " TURN"))
            elif checkWin() is True:
                label.config(text=(players[0] + " WINS!"))
            elif checkWin() == "TIE":
                label.config(text="TIE!")

        else:  
            buttons[row][column]['text'] = player
            
            if checkWin() is False:
                player = players[0]
                label.config(text=(players[0] + " TURN"))
            elif checkWin() is True:
                label.config(text=(players[1] + " WINS!"))
            elif checkWin() == "TIE":
                label.config(text="TIE!")

def checkWin():
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != " ":
            buttons[row][0].config(bg="dark green")
            buttons[row][1].config(bg="dark green")
            buttons[row][2].config(bg="dark green")
            return True
        
    for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != " ":
                buttons[0][column].config(bg="dark green")
                buttons[1][column].config(bg="dark green")
                buttons[2][column].config(bg="dark green")
                return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != " ":
            buttons[0][0].config(bg="dark green")
            buttons[1][1].config(bg="dark green")
            buttons[2][2].config(bg="dark green")
            return True
        
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != " ":
            buttons[0][2].config(bg="dark green")
            buttons[1][1].config(bg="dark green")
            buttons[2][0].config(bg="dark green")
            return True
        
    elif emptySpaces() is False:
            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="dark orange")
            return "TIE"    
        
    else:
            return False

def emptySpaces():
    
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != " ":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def newGame():
    global player

    player = random.choice(players)
    label.config(text=player + " TURN")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text=" ",bg="dark gray")    

window = tk.Tk()
window.title("TIC TAC TOE")
window.geometry("500x380")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0], 
           [0,0,0], 
           [0,0,0]]

label = tk.Label(text = player + " " +"TURN" , font = ("Komika", 15))
label.pack(side = "top")

reset_button = tk.Button(text="restart", font = ("Komika", 15), 
                bg="gray", activebackground="dark gray",         
                command = newGame)
reset_button.pack(padx=10, pady=10, side = "bottom")

frame = frame = tk.Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = tk.Button(frame, text = " ", font = ("Komika", 20), width = 5, height = 2, 
                bg="gray", activebackground="dark gray",
                command = lambda r=row, c=column: nextTurn(r, c))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()  
