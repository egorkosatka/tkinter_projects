import tkinter      # импорты
import math
import tkinter.messagebox


master = tkinter.Tk()       # создаю окно
canvas = tkinter.Canvas(master, bg='white', height=300, width=300)  # создаю холст
canvas.pack()        # пакую всё это
radius = 100        # радиус


def insert():
    try:
        number = int(e1.get())    # вводим кол-во лучей так, чтобы потом работать с ними
    except ValueError:
        tkinter.messagebox.showerror(title='Ошибка', message='Вы ввели некорректное значение!\n\nЧисло концов: 5')
        number = 5
    canvas.delete("all") 
    for i in range(number):
        # вычисляем по формуле
        coord = (i + number / 2 - 1) % number if number % 2 == 0 else (i + (number - 1) / 2) % number
        cp = lambda x: (150 + radius * math.cos(2 * 3.14 * x / number), 150 + radius * math.sin(2 * 3.14 * x / number))
        canvas.create_line(cp(i), cp(coord), fill = 'red')     # отрисовываем линию


e1 = tkinter.Entry(width=50)
but = tkinter.Button(text="Сгенерировать", command=insert)
e1.pack()
but.pack()
master.mainloop()   # mainloop