from cgitb import text
from distutils.util import execute
import tkinter as tk
from turtle import pos, position

root = tk.Tk()

def StartPlayer():
    execute('game\main.py')

def StartAI():
    execute('game\main.py')

def LoadAI():
    execute('game\main.py')

root.resizable(False, False)

canvas = tk.Canvas(root, height=500, width=600, bg='black')
canvas.pack()

frame = tk.Frame(root, bg='black')
frame.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.1)
label = tk.Label(frame, text='Artificial Intelligence Minigames', font=('Raleway 24'), pady=50, bg='black', fg='yellow').pack()


framebtt1 = tk.Frame(root, bg='black')
framebtt1.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.4)

framebtt2 = tk.Frame(root, bg='black')
framebtt2.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.6)

framebtt3 = tk.Frame(root, bg='black')
framebtt3.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.8)

game_Player = tk.Button(framebtt1, text='Start as player', bg='yellow', height=2, width=35, font=('Raleway 16'), command=StartPlayer).pack()
game_AI = tk.Button(framebtt2, text='Start AI', bg='yellow', height=2, width=35, font=('Raleway 16'), command=StartAI).pack()
load_AI = tk.Button(framebtt3, text='Load AI', bg='yellow', height=2, width=35, font=('Raleway 16'), command=LoadAI).pack()

root.mainloop()