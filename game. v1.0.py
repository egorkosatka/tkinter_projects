import tkinter
from tkinter import messagebox
import random
import time

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


def key_pressed(event):
    if event.keysym == 'w':
        move_wrap(player, (0, -step))
    if event.keysym == 'a':
        move_wrap(player, (-step, 0))
    if event.keysym == 's':
        move_wrap(player, (0, step))
    if event.keysym == 'd':
        move_wrap(player, (step, 0))
    check_move()


master = tkinter.Tk()
step = 10
N_X = 10
N_Y = 10


canvas = tkinter.Canvas(master, bg='blue',
                        width=step * N_X, height=step * N_Y)

p_pos = 10
e_pos = 10

while e_pos == p_pos:
    p_pos = random.randint(0, N_X - 1) * step
    e_pos = random.randint(0, N_X - 1) * step

player_pos = (p_pos, e_pos)
exit_pos = (e_pos, e_pos)

player = canvas.create_oval((player_pos[0], player_pos[1]),
                            (player_pos[0] + step, player_pos[1] + step), 
                            fill='green')

exit = canvas.create_oval((exit_pos[0], exit_pos[1]),
                        (exit_pos[0] + step, exit_pos[1] + step), 
                        fill='yellow')

label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
