from tkinter import *
from time import sleep
User = {
    1 : "X",
    0 : "O"
}
BORDERWIDTH = 10
HEIGHT = 10
WIDTH = 20
Result = [[None, None, None],
          [None, None, None],
          [None, None, None]]

chance = 1
used=0

def onclick(x, y, btn):
    global chance, used
    Result[x][y] = chance
    used = used+1
    find_winner(x, y, chance)
    chance = (chance + 1) % 2
    print(ChanceDict[chance])
    btn.config(state=DISABLED, image=ChanceDict[chance],height=HEIGHT+145, width=WIDTH+125)


def find_winner(x, y, key):
    global used
    #vertical wins
    if Result[0][y]==Result[1][y]==Result[2][y]!=None:
        declare_winner(key)
    #Horizontal wins
    elif Result[x][0]==Result[x][1]==Result[x][2]!=None:
        declare_winner(key)
    #Diagonal Wins
    elif Result[0][0]==Result[1][1]==Result[2][2]!=None or Result[0][2]==Result[1][1]==Result[2][0]!=None:
        declare_winner(key)
    elif used==9:
        print("Draw")

def declare_winner(key):
    winner.config(text=f"{User[key]} Won", font=("Times",30,"bold"),bg='#EED5B7')



screen = Tk()
screen.geometry("500x600")

ximg=PhotoImage(file="x.png")
oimg=PhotoImage(file="o.png")
ChanceDict = { 0 : ximg,
           1: oimg
           }
button11 = Button(screen, borderwidth=BORDERWIDTH, height=HEIGHT, width=WIDTH, bg='seaGreen3',
                  command=lambda: onclick(0, 0, button11))
button11.grid(column=0, row=0)

button12 = Button(screen, borderwidth=BORDERWIDTH, height=HEIGHT, width=WIDTH, bg='seaGreen3',
                  command=lambda: onclick(0, 1, button12))
button12.grid(column=1, row=0)

button13 = Button(borderwidth=BORDERWIDTH, height=HEIGHT, width=WIDTH, bg='seaGreen3',
                  command=lambda: onclick(0, 2, button13))
button13.grid(column=2, row=0)

button21 = Button(borderwidth=BORDERWIDTH, height=HEIGHT, width=WIDTH, bg='seaGreen3',
                  command=lambda: onclick(1, 0, button21))
button21.grid(column=0, row=1)

button22 = Button(borderwidth=BORDERWIDTH, height=HEIGHT, width=WIDTH, bg='seaGreen3',
                  command=lambda: onclick(1, 1, button22))
button22.grid(column=1, row=1)

button23 = Button(borderwidth=BORDERWIDTH, height=HEIGHT, width=WIDTH, bg='seaGreen3',
                  command=lambda: onclick(1, 2, button23))
button23.grid(column=2, row=1)

button31 = Button(borderwidth=BORDERWIDTH, height=HEIGHT, width=WIDTH, bg='seaGreen3',
                  command=lambda: onclick(2, 0, button31))
button31.grid(column=0, row=2)

button32 = Button(borderwidth=BORDERWIDTH, height=HEIGHT, width=WIDTH, bg='seaGreen3',
                  command=lambda: onclick(2, 1, button32))
button32.grid(column=1, row=2)

button33 = Button(borderwidth=BORDERWIDTH, height=HEIGHT, width=WIDTH, bg='seaGreen3',
                  command=lambda: onclick(2, 2, button33))
button33.grid(column=2, row=2)

winner=Label(text="GAME IS ON",width=20,pady=10, padx=10, font=("Times",30,"bold"),bg='#3D9140')
winner.grid(row=3, columnspan=3)

screen.mainloop()
