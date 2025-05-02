# MINESWEEPER ----------------------------------------------------------------------------------

# IMPORTING MODULES

import tkinter, random, os
from tkinter import *

#import winsound


# CREATING GAME WINDOW

window = tkinter.Tk()
window.geometry("640x520")
window["bg"]="#006D77"
window.title("MINESWEEPER")



row = 10
column = 10
mine = 20


new = True
gameover = False


#Insert image file location

flag_image= PhotoImage(file='/Users/shivani.dinesh/Desktop/Shivani/12th archive/CS_Project/assets/flag_final copy.png')

#Insert image file location

mine_image = PhotoImage(file='/Users/shivani.dinesh/Desktop/Shivani/12th archive/CS_Project/assets/mine1 copy.png')


bg1 = "#006D77"

fg1 = "#83C5BE"

bg2 = "#2F3C7E"

fg2 = "#FBEAEB"

bg3 = "#02343F"

fg3 = "#F0EDCC"

bg4 = "#201E20"

fg4 = "#DDC3A5"


# START PAGE

def home():
    global play, inst, score, setting
    
    
    play = tkinter.Button(window, text="PLAY", highlightbackground="#006D77", font=("Helvetica",17), command = gameWindow2, height=2, width=15)
    play.grid(row=5, column=5)
    play.place(relx=0.5, rely=0.4, anchor='center')
    
    inst = tkinter.Button(window, text="HOW TO PLAY?", highlightbackground="#006D77", font=("Helvetica",17), command = instructions, height=2, width=15)
    inst.grid(row=6, column=5)
    inst.place(relx=0.5, rely=0.5, anchor='center')
    
    score = tkinter.Button(window, text="SCOREBOARD", highlightbackground="#006D77", font=("Helvetica",17), command = score_display, height=2, width=15)
    score.grid(row=6, column=5)
    score.place(relx=0.5, rely=0.6, anchor='center')
    
    setting = tkinter.Button(window, text="SETTINGS", highlightbackground="#006D77", font=("Helvetica",17), command = settings, height=2, width=15)
    setting.grid(row=6, column=5)
    setting.place(relx=0.5, rely=0.7, anchor='center')
    
def settings():
     
    
    play.destroy()
    inst.destroy()
    score.destroy()
    setting.destroy()
    
    change_clr = tkinter.Button(window, text="Change Display Colour", highlightbackground="#006D77", font=("Helvetica",17), command = colour, height=2, width=15)
    change_clr.grid(row=6, column=5)
    change_clr.place(relx=0.5, rely=0.5, anchor='center')
    
    
def colour():
    
    c1 = tkinter.Button(window, text="COMBO-1", highlightbackground=fg1, font=("Helvetica",17), command = set1, height=2, width=15)
    c1.grid(row=6, column=5)
    c1.place(relx=0.5, rely=0.4, anchor='center')
    
    c2 = tkinter.Button(window, text="COMBO-2", highlightbackground=fg2, font=("Helvetica",17), command = set2, height=2, width=15)
    c2.grid(row=6, column=5)
    c2.place(relx=0.5, rely=0.5, anchor='center')
    
    c3 = tkinter.Button(window, text="COMBO-3", highlightbackground=fg3, font=("Helvetica",17), command = set3, height=2, width=15)
    c3.grid(row=6, column=5)
    c3.place(relx=0.5, rely=0.6, anchor='center')
    
    c4 = tkinter.Button(window, text="COMBO-4", highlightbackground=fg4, font=("Helvetica",17), command = set4, height=2, width=15)
    c4.grid(row=6, column=5)
    c4.place(relx=0.5, rely=0.7, anchor='center')
    
    play = tkinter.Button(window, text="PLAY", highlightbackground="#006D77", font=("Helvetica",17), command = gameWindow, height=2, width=15)
    play.grid(row=5, column=5)
    play.place(relx=0.5, rely=0.8, anchor='center')
    
    
    
def set1():
    global fg, bg
    
    window["bg"]="#006D77"
    bg=bg1
    fg=fg1
    
    gameWindow()
    
def set2():
    global fg, bg
    
    window["bg"]="#2F3C7E"
    bg=bg2
    fg=fg2
    
    gameWindow()
    
def set3():
    global fg, bg
    
    window["bg"]="#02343F"
    fg=fg3
    bg=bg3
    
    gameWindow()
    
def set4():
    global fg, bg
    
    window["bg"]="#201E20"
    fg=fg4
    bg=bg4
    
    gameWindow()
    
def instructions():
    global play, inst, score
    global steps, header, back_btn
    
    play.destroy()
    inst.destroy()
    score.destroy()
    
    header = tkinter.Label(window, text="HOW TO PLAY?", width=15, font=("Helvetica", 15))
    header.grid(row=5, column=5)
    header.place(relx=0.5, rely=0.1, anchor='center')
    
    steps = Text(window, height=25, width=70, font=("Helvetica",13))
    steps.grid(row=6, column=5)
    steps.place(relx=0.5, rely=0.5, anchor='center')
    
    content = """Here are the instructions on how to play MINESWEEPER:
        
        
        1. Each Minesweeper game starts out with a grid of unmarked squares.
        
        2. The objective of the game is to clear the board without clicking on
           the boxes with mine.
           
        3. To start the game, first click on any box at random.
        
        4. Now, one of the three things happen:
            
            a. You see a single number on the screen which replaced the box
               you clicked on.
               
            b. You see a number of boxes that have opened, and some numbers
               surround a few empty boxes.
               
            c. You clicked on a mine and a 'Game Over' message appears...
               Better luck next time!
               
        5. The numbers that you see are the clues that tell you how many mines
           surround the box with the number.
           
        6. Based on these clues you must proceed opening remaining boxes
          (which do not contain mines)
          
        7. When you feel that a certain box does contain a mine, you may right
           click over it to flag it. 
           This step is completely optional as it is only so that you do not
           have to memorize all the locations.
           
           """
    steps.insert(tkinter.END, content)
    
    back_btn = tkinter.Button(window, text="Back", highlightbackground="#006D77", font=("Helvetica",13), command = back, height=2, width=15)
    back_btn.grid(row=5, column=5)
    back_btn.place(relx=0.5, rely=0.95, anchor='center')
    
def back():
    global steps, header, back_btn
    
    steps.destroy()
    header.destroy()
    back_btn.destroy()
    
    home()



# ADDING BUTTONS

def gameWindow2():
    global buttons, play, score
    
    play.destroy()
    inst.destroy()
    score.destroy()
    
    
    rstrt = tkinter.Button(window, text="Restart", highlightbackground=bg1, command = restartGame, width = 5)
    rstrt.grid(row=10, column=11, sticky=tkinter.N+tkinter.W+tkinter.S+tkinter.E)
    
    window["bg"]="#006D77"
    
    
    buttons = []
    for r in range(0, row):
        buttons.append([])
        for c in range(0, column):
            
            
            box = tkinter.Button(window,  highlightbackground=fg1, text=" ", relief="raised", font=("Helvetica",17, "bold"), width=2, height=2, command=lambda r=r,c=c: leftClicked(r,c))
            
            
            
            box.bind("<Button-2>", lambda e, r=r, c=c:rightClicked(r,c))
            box.bind("<Button-3>", lambda e, r=r, c=c:rightClicked(r,c))
            box.grid(row=r+1, column=c, sticky=tkinter.N+tkinter.W+tkinter.S+tkinter.E)
            
            buttons[r].append(box)
            
    newGame()

def gameWindow():
    global buttons, play, score
    
    play.destroy()
    inst.destroy()
    score.destroy()
    
    
    rstrt = tkinter.Button(window, text="Restart", highlightbackground=bg, command = restartGame2, width = 5)
    rstrt.grid(row=10, column=11, sticky=tkinter.N+tkinter.W+tkinter.S+tkinter.E)
    

    
    
    buttons = []
    for r in range(0, row):
        buttons.append([])
        for c in range(0, column):
            
            
            box = tkinter.Button(window,  highlightbackground=fg, text=" ", relief="raised", font=("Helvetica",17, "bold"), width=2, height=2, command=lambda r=r,c=c: leftClicked(r,c))
            
            
            
            box.bind("<Button-2>", lambda e, r=r, c=c:rightClicked(r,c))
            box.bind("<Button-3>", lambda e, r=r, c=c:rightClicked(r,c))
            box.grid(row=r+1, column=c, sticky=tkinter.N+tkinter.W+tkinter.S+tkinter.E)
            
            buttons[r].append(box)
            
    newGame()
    
# CREATING ROWS & COLUMNS

def newGame():
    global board
    
    board = []                      
    for r in range(0, row):           
        board.append([])            
        for c in range(0, column):
            board[r].append(0)      
                                    
# ADDING MINES 

    for m in range (0, mine):
        r = random.randint(0,row-1)
        c = random.randint(0,column-1)    
        
        
        while board[r][c] == -1:
            r = random.randint(0,row-1)
            c = random.randint(0,column-1)
        board[r][c] = -1
        
# ADDING CLUES

        if r != 0:                 
            if c !=0:              
                if board[r-1][c-1] != -1:
                    board[r-1][c-1] = int(board[r-1][c-1]) + 1      
            
            if board[r-1][c] != -1:
                board[r-1][c] = int(board[r-1][c]) + 1              
            
            if c != column-1:           
                if board[r-1][c+1] != -1:                           
                    board[r-1][c+1] = int(board[r-1][c+1]) + 1      
        
        if c != 0:                 
            if board[r][c-1] != -1:                                 
                board[r][c-1] = int(board[r][c-1]) + 1              
        
        if c != column-1:               
            if board[r][c+1] != -1:
                board[r][c+1] = int(board[r][c+1]) + 1             
        
        if r != row-1:               
            if c != 0:             
                if board[r+1][c-1] != -1:
                    board[r+1][c-1] = int(board[r+1][c-1]) + 1      
            if board[r+1][c] != -1:
                board[r+1][c] = int(board[r+1][c]) + 1              
            if c != column-1:           
                if board[r+1][c+1] != -1:
                    board[r+1][c+1] = int(board[r+1][c+1]) + 1
                    
# GAME OVER 
   
def leftClicked(r,c):
    global gameover
    if gameover:
        return
    buttons[r][c]["text"] = str(board[r][c])
    
    if board[r][c] == -1:
        buttons[r][c]["image"] = mine_image                                                  
        buttons[r][c].config(highlightbackground='red')
        gameover = True
       
        for r in range(0, row):
            for c in range(0, column):
                if board[r][c] == -1:
                    buttons[r][c]["image"] = mine_image                                   
                    buttons[r][c]["state"] = "disabled"
        tkinter.messagebox.showinfo("Game Over", "You have lost.")
        
        for r in range(0, row):
            for c in range(0, column):
                    buttons[r][c].config(state = "disabled", relief="sunken")

# GAME CONTINUE

    else:
        if buttons[r][c]["text"] == "1":
            buttons[r][c].config(disabledforeground="#1E88E5")
        if buttons[r][c]["text"] == "2":
            buttons[r][c].config(disabledforeground="#388E3C")
        if buttons[r][c]["text"] == "3":
            buttons[r][c].config(disabledforeground="#F57F17")
        if buttons[r][c]["text"] == "4":
            buttons[r][c].config(disabledforeground="#F44336")
        if buttons[r][c]["text"] == "5":
            buttons[r][c].config(disabledforeground="#B71C1C")
        if buttons[r][c]["text"] == "6":
            buttons[r][c].config(disabledforeground="#C2185B")
        if buttons[r][c]["text"] == "7":
            buttons[r][c].config(disabledforeground="#9C27B0")
        if buttons[r][c]["text"] == "8":
            buttons[r][c].config(disabledforeground="#4A148C")
            
    if board[r][c] == 0:
        buttons[r][c]["text"] = " "
        openNearby(r,c)
        
    buttons[r][c]['state'] = 'disabled'
    gameWon()
    
# Open adjacent empty boxes 
        
def openNearby(r,c):
   
    if buttons[r][c]["state"] == "disabled":
        return
    if board[r][c] != 0:
        buttons[r][c]["text"] = str(board[r][c])
        
        
    else:
        buttons[r][c]["text"] = " "
    if buttons[r][c]["text"] == "1":
        buttons[r][c].config(disabledforeground="#1E88E5")
    if buttons[r][c]["text"] == "2":
        buttons[r][c].config(disabledforeground="#388E3C")
    if buttons[r][c]["text"] == "3":
        buttons[r][c].config(disabledforeground="#F57F17")
    if buttons[r][c]["text"] == "4":
        buttons[r][c].config(disabledforeground="#F44336")
    if buttons[r][c]["text"] == "5":
        buttons[r][c].config(disabledforeground="#B71C1C")
    if buttons[r][c]["text"] == "6":
        buttons[r][c].config(disabledforeground="#C2185B")
    if buttons[r][c]["text"] == "7":
        buttons[r][c].config(disabledforeground="#9C27B0")
    if buttons[r][c]["text"] == "8":
        buttons[r][c].config(disabledforeground="#4A148C")
    buttons[r][c]['state'] = 'disabled'
    if board[r][c] == 0:
        if r != 0 and c != 0:                         
            openNearby(r-1,c-1)
        if r != 0:                                    
            openNearby(r-1,c)
        if r != 0 and c != column-1:                  
            openNearby(r-1,c+1)
        if c != 0:                                    
            openNearby(r,c-1)
        if c != column-1:                             
            openNearby(r,c+1)
        if r != row-1 and c != 0:                     
            openNearby(r+1,c-1)
        if r != row-1:                                
            openNearby(r+1,c)
        if r != row-1 and c != column-1:              
            openNearby(r+1,c+1)

# FLAG 

def rightClicked(r,c):
    
    if gameover:
        return
    if buttons[r][c]["text"] == " ":
        if buttons[r][c]["state"] == "normal":
            buttons[r][c]["text"] = ">"
            buttons[r][c]["state"] = "disabled"
            buttons[r][c]["image"] = flag_image
            
    elif buttons[r][c]["text"] == ">":
        buttons[r][c]["text"] = " "
        buttons[r][c]["state"] = "normal"
        buttons[r][c].config(image="")
        
#scores declaration

    
# RESTART 

def restartGame():
    global gameover
    
    gameover = False        
          
    for r in window.winfo_children(): 
        r.destroy()
    gameWindow2()
    newGame()
    
def restartGame2():
    global gameover
    
    gameover = False        
          
    for r in window.winfo_children(): 
        r.destroy()
    gameWindow()
    newGame()

# SCORES

def score_display(): 
    
    #displays the score updated in the file after the last win
    
       file=open("scores.txt","r")
       a=file.read()
       sc="your score till now :"
       tkinter.messagebox.showinfo("your score is ",sc+a)
       file.close()
    

#declaring scr for further updates

# GAME WON
def gameWon():
     

    win = True
    for r in range(0, row):
        for c in range(0, column):
            if board[r][c] != -1:
                if buttons[r][c]["state"] == "normal":
                    win = False
                
#defining if win
                    
    if win == True:
        file= open("scores.txt",'r+')
        if gameover == False:
            
            #updating the score for each win
            scr=0 
            scr+=1
            a=file.read()
            
            #taking the score saved after previous games in form of integer
            pre_sc=int(a)
            
            #adding the score after winning the game and update in the file
            scr1=str(scr+pre_sc)
            file.write(scr1)
            file.close()
            
            #showing message for game won
            tkinter.messagebox.showinfo("Congratulations","You have won the game!!!")
            
            
home()                    

window.mainloop()