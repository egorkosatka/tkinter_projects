# pip install speedtest-cli

import tkinter
import time
import speedtest
from tkinter import Label, Button
import speedtest


def run_test():
    text.config(text='Ожидайте!')
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    text.config(text=f'Download: {str(res["download"])[:2]} Мб\nUpload: {str(res["upload"])[:2]} Мб\nPing: {str(res["ping"]).split(".")[0]} М/с')


master = tkinter.Tk()       # создаю окно
master.title('speedtest')
master.geometry('220x210')
text = Label(text="Запустите!",
           font=("Comic Sans MS",
                 14, "bold"), bd=14)
text.pack()
run_but = Button(text='run', command=run_test, width=20, height=3, bg='#CCCCCC')
run_but.place(y = 100)
run_but.pack()
dop_indo = Label(text='PS. программа на некоторое время\nзависнет. Не бойтесь, так должно быть!').pack()
canvas = tkinter.Canvas(master, bg='white', height=30, width=300).pack()  # создаю холст
master.mainloop()   # mainloop
