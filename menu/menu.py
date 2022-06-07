from cgitb import text
from distutils.util import execute
from email.mime import image
import runpy
import tkinter as tk
from tkinter.messagebox import YES
from turtle import pos, position


root = tk.Tk()

def StartPlayer():
    runpy.run_path("C:\\Users\\aim\\Documents\\GitHub\\self-learning-ai-itp\\game\\main.py")

def StartAI():
    runpy.run_path("C:\\Users\\aim\\Documents\\GitHub\\self-learning-ai-itp\\game\\main.py")

def LoadAI():
    runpy.run_path("C:\\Users\\aim\\Documents\\GitHub\\self-learning-ai-itp\\game\\main.py")


root.resizable(False, False)



canvas = tk.Canvas(root, height=500, width=600, bg="black")
canvas.pack()

bg = tk.PhotoImage(file="C:\\Users\\aim\\Documents\\GitHub\\self-learning-ai-itp\\menu\weltall.png")
l = tk.Label(root, image=bg)
l.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='darkblue')
frame.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.1)
label = tk.Label(frame, text='Artificial Intelligence Minigames', font=('Raleway 24'), pady=50, bg='darkblue', fg='lightblue').pack()

framebtt1 = tk.Frame(root, bg='darkblue')
framebtt1.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.4)

framebtt2 = tk.Frame(root, bg='darkblue')
framebtt2.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.6)

framebtt3 = tk.Frame(root, bg='darkblue')
framebtt3.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.8)

game_Player = tk.Button(framebtt1, text='Start as player', bg='darkblue', fg="lightblue", height=2, width=35, font=('Raleway 16'), command=StartPlayer).pack()
game_AI = tk.Button(framebtt2, text='Start AI', bg='darkblue', fg="lightblue", height=2, width=35, font=('Raleway 16'), command=StartAI).pack()
load_AI = tk.Button(framebtt3, text='Load AI', bg='darkblue', fg="lightblue", height=2, width=35, font=('Raleway 16'), command=LoadAI).pack()

root.mainloop()