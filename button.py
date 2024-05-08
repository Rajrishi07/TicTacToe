
from tkinter import Button
BORDERWIDTH = 10
HEIGHT = 10
WIDTH = 20
class my_Button(Button):
        def __init__(self,x,y):
            super().__init__()
            self.config(height=HEIGHT, width=WIDTH,borderwidth=BORDERWIDTH,
                        bg='seaGreen3')
            self.grid(column=x, row=y)

