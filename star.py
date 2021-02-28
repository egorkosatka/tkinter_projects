import tkinter
from tkinter import messagebox, Button, Label
import math

def insert():
    try:
        number = int(e1.get())    # вводим кол-во лучей так, чтобы потом работать с ними
    except ValueError:
        messagebox.showerror(title='Ошибка', message='Вы ввели некорректное значение!\n\nЧисло концов: 5')
        number = 5
    canvas.delete("all") 
    for i in range(number):
        # вычисляем по формуле
        coord = (i + number / 2 - 1) % number if number % 2 == 0 else (i + (number - 1) / 2) % number
        cp = lambda x: (100 + radius * math.cos(2 * 3.14 * x / number), 100 + radius * math.sin(2 * 3.14 * x / number))
        canvas.create_line(cp(i), cp(coord), fill = 'red')     # отрисовываем линию


def question():
    messagebox.showinfo(title='question', message='Программа рисует звезду с определённым\
        количеством концов.\n\n\nВведите число в строку и нажмите "сгенерировать"')


master = tkinter.Tk()       # создаю окно
master.title('star')
master.geometry('210x300')
question_button = tkinter.Button(text='?', command=question, width=50).pack()
canvas = tkinter.Canvas(master, bg='white', height=220, width=200)  # создаю холст
canvas.pack()        # пакую всё это
radius = 100        # радиус
e1 = tkinter.Entry(width=50)
but = tkinter.Button(text="Сгенерировать", command=insert, width=50)
e1.pack()
but.pack()
master.mainloop()   # mainloop
