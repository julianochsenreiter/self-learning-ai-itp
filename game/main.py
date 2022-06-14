import gym
from stable_baselines3 import A2C, DQN, PPO
from AIManager import GatherData, Load
from gym.utils.play import play, PlayPlot

from email.mime import image
from tkinter.messagebox import YES
from tkinter import filedialog as fd
from tkinter import *
import tkinter as tk


root = tk.Tk()


def StartPlayer():
    _destroyMenu()
                    
    env = gym.make("gym_spaceship/Spaceship-v0")

    play(env, fps=240)

def StartAI():
    _destroyMenu()

    GatherData(A2C)
    GatherData(DQN)
    GatherData(PPO)

def LoadAI():
    filename = fd.askopenfilename(defaultextension="zip")

    bigname = filename.upper()
    if(bigname.find("A2C") != -1):
        Load(filename, A2C)
    elif(bigname.find("DQN") != -1):
        Load(filename, DQN)
    elif(bigname.find("PPO") != -1):
        Load(filename, PPO)
    else:
        return
    
    _destroyMenu()

def _destroyMenu():
    root.destroy()

root.resizable(False, False)

def Main():
    canvas = tk.Canvas(root, height=500, width=600, bg="black")
    canvas.pack()

    bg = tk.PhotoImage(file="menu/weltall.png")
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

    tk.Button(framebtt1, text='Start as player', bg='darkblue', fg="lightblue", height=2, width=35, font=('Raleway 16'), command=StartPlayer).pack()
    tk.Button(framebtt2, text='Start AI', bg='darkblue', fg="lightblue", height=2, width=35, font=('Raleway 16'), command=StartAI).pack()
    tk.Button(framebtt3, text='Load AI', bg='darkblue', fg="lightblue", height=2, width=35, font=('Raleway 16'), command=LoadAI).pack()

    root.mainloop()

if __name__ == "__main__":
    Main()