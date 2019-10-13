from tkinter import *
from tkinter import messagebox
import db.db


class Customer:

    def __init__(self):
        self.win = Tk()
        self.win.geometry("600x400")
        self.win.title("Data Option Menu")

    def add_frame(self):
        self.frame = Frame(self.win, width=400, height=300)
        self.frame.place(x=0,y=0)

        self.label = Label(self.frame, text='Name')
        self.label.place(x=10, y=10)

        # Drop down menu
        OPTIONS = []
        for i in db.db.show_options():
            OPTIONS.append(i[1])

        self.variable = StringVar(self.win)
        self.variable.set(OPTIONS[0])

        self.name = OptionMenu(self.frame, self.variable, *OPTIONS, command=self.dropdown)
        self.name.place(x=80, y=10)

        self.win.mainloop()


    def dropdown(self, value, *args):
        print(self.variable.get())


if __name__ == "__main__":
    x = Customer()
    x.add_frame()