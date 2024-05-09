from tkinter import *
from button import my_Button

User = {
    1: "X",
    0: "O"
}
BORDERWIDTH = 10
HEIGHT = 10
WIDTH = 20
Result = [[None, None, None],
          [None, None, None],
          [None, None, None]]

chance = 1
used = 0


def onclick(x, y, btn):
    global chance, used
    Result[x][y] = chance
    used = used + 1
    find_winner(x, y, chance)
    chance = (chance + 1) % 2
    btn.config(state=DISABLED, image=ChanceDict[chance], height=HEIGHT + 145, width=WIDTH + 125)


def find_winner(x, y, key):
    global used
    # vertical wins
    if Result[0][y] == Result[1][y] == Result[2][y] is not None:
        declare_winner(key)
    # Horizontal wins
    elif Result[x][0] == Result[x][1] == Result[x][2] is not None:
        declare_winner(key)
    # Diagonal Wins
    elif (Result[0][0] == Result[1][1] == Result[2][2] is not None or
          Result[0][2] == Result[1][1] == Result[2][0] is not None):
        declare_winner(key)
    elif used == 9:
        state_draw()


def declare_winner(key):
    winner.config(text=f"{User[key]} Won", font=("Times", 30, "bold"), bg='#EED5B7')
    screen.after(2000, exit, 1)


def state_draw():
    winner.config(text="Game Tied NO winner", font=("Times", 30, "bold"), bg='#EED5B7')
    screen.after(2000, exit, 1)


screen = Tk()
screen.geometry("500x600")

ximg = PhotoImage(file="x.png")
oimg = PhotoImage(file="o.png")
ChanceDict = {0: ximg,
              1: oimg
              }

# Creating Buttons
Buttons = []
count = 0
for i in range(0, 3):
    for j in range(0, 3):
        btn = my_Button(i, j)
        Buttons.append(btn)
        Buttons[count].config(command=lambda x=j, y=i, btn=Buttons[count]: onclick(x, y, btn))
        count = count + 1

winner = Label(text="GAME IS ON", width=20, pady=10, padx=10, font=("Times", 30, "bold"), bg='#3D9140')
winner.grid(row=3, columnspan=3)

screen.mainloop()
