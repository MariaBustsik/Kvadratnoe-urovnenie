from tkinter import *
from math import *


def calculation(event):
    a1 = int(str(a.get()))
    b1 = int(str(b.get()))
    c1 = int(str(c.get()))
    d = b1**2 - 4 * a1 * c1
    if d > 0:
        x1 = (-b1 + sqrt(d)) / (2 * a1)
        x2 = (-b1 - sqrt(d)) / (2 * a1)
        #x3 = "x1 = " + x1 + "x2 = " + x2
        lbl.configure(text=f"x1 = {x1} + x2 = {x2}")
    if d == 0:
        x1 = -b1 / (2 * a1)
        #x3 = "x = " + x1
        lbl.configure(text=f"x1 = {x1}")
    if d < 0:
        lbl.configure(text=f"Нет решения D = {d}")

win=Tk()
win.title("Название окна")
win.geometry("500x500")

btn=Button(win,text="Нажми \n на меня",fg="red",bg="lightblue",font="Arial 40",width=15)
lbl=Label(win,text="0",height=3)
a=Entry(win,text="Введите значение а: ",fg="red",bg="lightblue",font="Arial 15",width=3)
b=Entry(win,text="Введите значение b: ",fg="red",bg="lightblue",font="Arial 15",width=3)
c=Entry(win,text="Введите значение c: ",fg="red",bg="lightblue",font="Arial 15",width=3)

a.pack()
b.pack()
c.pack()
btn.pack()
btn.bind("<Button-1>",calculation)
lbl.pack(padx=20,pady=20)

win.mainloop()
