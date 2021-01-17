from tkinter import *
from math import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def calculation(event):
    if not a.get() or not b.get() or not c.get():
        lbl.configure(text="Заполните ячейки цифрами!")
    else:
        a1 = int(str(a.get()))
        a.delete(0, END)
        b1 = int(str(b.get()))
        b.delete(0, END)
        c1 = int(str(c.get()))
        c.delete(0, END)
        d = b1**2 - 4 * a1 * c1
        x = np.arange(-1000, 1000, 0.1)
        y = (a1)*(x**2)+(b1)*x+(c1)

        if a1==0:
            lbl.configure(text="Неверное значение параметра: а")

        else:
            if d > 0:
                x1 = (-b1 + sqrt(d)) / (2 * a1)
                x2 = (-b1 - sqrt(d)) / (2 * a1)
                #x3 = "x1 = " + x1 + "x2 = " + x2
       
                lbl.configure(text=f"Результат: x1 = {x1}  x2 = {x2}")
            if d == 0:
                x1 = -b1 / (2 * a1)
                #x3 = "x = " + x1
                lbl.configure(text=f"x1 = {x1}")
            if d < 0:
                lbl.configure(text=f"Нет решения D = {d}")
            plt.subplots()
            plt.grid(True)# Отображение сетки на координатной плоскости
            plt.plot(x,y,'-r',linewidth=1)
            plt.show()  # Вывод изображения на экран

win=Tk()
win.title("Решение квадратного уравнения")
win.geometry("500x500")

def only_numbers(char):
    return char.isdigit()

validation=win.register(only_numbers)

img=PhotoImage(file="pilt.png")
btn_image=Label(win,image=img)

lbl1=Label(win,text="Введите значения a, b, c: ",font="Arial 15")

btn=Button(win,text="Решить",fg="red",bg="lightgrey",font="Arial 10",width=7)
lbl=Label(win,text="0",fg="purple", font="Arial 11", height=3)
a=Entry(win,text="Введите значение а: ",fg="red",bg="lightblue",font="Arial 15",width=3, validate="key", validatecommand=(validation, "%S"))
b=Entry(win,text="Введите значение b: ",fg="red",bg="lightblue",font="Arial 15",width=3, validate="key", validatecommand=(validation, "%S"))
c=Entry(win,text="Введите значение c: ",fg="red",bg="lightblue",font="Arial 15",width=3, validate="key", validatecommand=(validation, "%S"))

btn_image.pack()
lbl1.pack()
a.pack()
b.pack()
c.pack()
btn.pack()
btn.bind("<Button-1>",calculation)
lbl.pack(padx=20,pady=20)


win.mainloop()