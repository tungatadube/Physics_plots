from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Ball Animate")
canvas.pack()

ball = canvas.create_oval(10, 10, 60, 60, fill = 'green')
xspeed = 4
yspeed = 2

while True:
    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball)
    if pos[3] >= HEIGHT or pos[1] <= 0:
        yspeed = -yspeed
        canvas.create_oval(pos[0], pos[1], pos[2], pos[3], fill = 'red')
    if pos[2] >= WIDTH or pos[0] <=0:
        xspeed = -xspeed
        canvas.create_oval(pos[0], pos[1], pos[2], pos[3], fill = 'yellow')
    tk.update()
    time.sleep(0.01)

tk.mainloop()