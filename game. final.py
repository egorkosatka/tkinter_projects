# Q - смена позиции выхода
# C - смена цвета фона


import tkinter
from tkinter import messagebox
import random
import time

colors = ['blue', 'white', 'red']
index = 0

def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])
    if canvas.coords(obj)[1] < 0:
        canvas.move(obj, move[0], step * N_X)
    
    if canvas.coords(obj)[0] < 0:
        canvas.move(obj, step * N_X, move[1])

    if canvas.coords(obj)[0] > 90:
        canvas.move(obj, -step * N_X, move[1])

    if canvas.coords(obj)[1] > 90:
        canvas.move(obj, move[0], -step * N_X)


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        canvas.quit()
        tkinter.messagebox.showwarning(title='Предупреждение!', message='Игра закончена!') 
    if canvas.coords(player) == canvas.coords(enemy):
        canvas.quit()
        tkinter.messagebox.showwarning(title='Предупреждение!', message='Вас убили!')
    if canvas.coords(enemy) == canvas.coords(exit):
        canvas.quit()
        tkinter.messagebox.showwarning(title='Предупреждение!', message='Враг сьел выход!')

def key_pressed(event):
    global index, colors
    if event.keysym == 'w':
        move_wrap(player, (0, -step))
    if event.keysym == 'a':
        move_wrap(player, (-step, 0))
    if event.keysym == 's':
        move_wrap(player, (0, step))
    if event.keysym == 'd':
        move_wrap(player, (step, 0))
    if event.keysym == 'q':
        canvas.move(exit, 10, 10)
        move_wrap(exit, (random.randint(0, 10) * step, random.randint(0, 10) * step))
    if event.keysym == 'c':
        index += 1 if index < 2 else 0
        canvas.config(bg=colors[index])
    if canvas.coords(enemy)[0] != canvas.coords(exit)[0]:
        if canvas.coords(enemy)[0] < canvas.coords(exit)[0]:
            move_wrap(enemy, (step, 0))
        if canvas.coords(enemy)[0] > canvas.coords(exit)[0]:
            move_wrap(enemy, (-step, 0))
    if canvas.coords(enemy)[1] != canvas.coords(exit)[1]:
        if canvas.coords(enemy)[1] < canvas.coords(exit)[1]:
            move_wrap(enemy, (0, step))
        if canvas.coords(enemy)[1] > canvas.coords(exit)[1]:
            move_wrap(enemy, (0, -step))
    check_move()


master = tkinter.Tk()
step = 10
N_X = 10
N_Y = 10

canvas = tkinter.Canvas(master, bg=colors[index],
                        width=step * N_X, height=step * N_Y)

p_pos = 10
e_pos = 10
en_pos = random.randint(0, 10) * step
while e_pos == p_pos:
    p_pos = random.randint(0, N_X - 1) * step
    e_pos = random.randint(0, N_X - 1) * step

player_pos = (p_pos, p_pos)
exit_pos = (e_pos, e_pos)
enemy_pos = (en_pos, 0)
player = canvas.create_oval((player_pos[0], player_pos[1]),
                            (player_pos[0] + step, player_pos[1] + step), 
                            fill='green')

exit = canvas.create_oval((exit_pos[0], exit_pos[1]),
                        (exit_pos[0] + step, exit_pos[1] + step), 
                        fill='yellow')

enemy = canvas.create_oval((enemy_pos[0], enemy_pos[1]), 
                        (enemy_pos[0] + step, enemy_pos[1] + step), 
                        fill='black')
label = tkinter.Label(master, text="найди выход!")
label.pack()
canvas.pack()
master.geometry("150x180")
master.bind("<KeyPress>", key_pressed)
master.mainloop()
