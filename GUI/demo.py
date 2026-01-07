# from tkinter import *

# root=Tk()

# root.geometry("500x500")
# btn=Button(root,text="submit").pack(side=LEFT)
# btn=Button(root,text="username").pack(side=RIGHT)
# btn=Button(root,text="parth").pack(side=TOP)
# btn=Button(root,text="resubmit").pack(side=BOTTOM)


# l1=Label(root,text="username").grid(row=1,column=1)
# l2=Label(root,text="Email").grid(row=2,column=1)
# e1=Entry()
# e2=Entry()
# e1.grid(row=1,column=2)
# e2.grid(row=2,column=2)
# btn=Button(root,text="submit").grid(row=3,column=2)

# l1=Label(root,text="username").place(x=100,y=100)
# l2=Label(root,text="email").place(x=100,y=150)

# e1=Entry()
# e2=Entry()

# e1.place(x=200,y=100)
# e2.place(x=200,y=150)
# btn=Button(root,text="sumbmit",width=15).Place(x=200,y=200)

# root.mainloop()

import math
import time

board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print()

def check_winner(player):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in wins)

def is_draw():
    return " " not in board

def minimax(is_max, player, opponent):
    if check_winner(player):
        return 1
    if check_winner(opponent):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                score = minimax(False, player, opponent)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = opponent
                score = minimax(True, player, opponent)
                board[i] = " "
                best = min(best, score)
        return best

def thinker_move(player, opponent):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            score = minimax(False, player, opponent)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = player

# Auto Play
current = "X"
opponent = "O"

print("🤖 THINKER vs THINKER TIC TAC TOE\n")
print_board()

while True:
    time.sleep(1)
    thinker_move(current, opponent)
    print(f"Thinker {current} move:")
    print_board()

    if check_winner(current):
        print(f"🏆 Thinker {current} wins!")
        break

    if is_draw():
        print("🤝 Draw! Perfect play.")
        break

    current, opponent = opponent, current
