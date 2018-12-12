import pyautogui
import time
import tkinter
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class application(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.geometry('900x600')
        self.parent.title('Color Picker')
        self.parent.configure(bg ='white')

        self.path = 'spectrum.png'
        self.img = ImageTk.PhotoImage(Image.open(self.path))
        self.lblIm = tk.Label(image = self.img)
        self.lblIm.place(x = 250, y = 100)
        self.lblIm.bind('<Motion>', self.motion)
        self.lblIm.bind('<Button-1>', self.events)



        self.titlelbl = tk.Label(text = 'COLOR PICKER',font = ('Comic Sans MS', 40), bg = 'black', fg = 'blue', width = 20)

        self.titlelbl.place(x = 1, y = 0)
        self.display = tk.Entry(text='', font=("Comic Sans MS", 10), bg='white', width=10)
        self.display.place(x=1, y=1)

    def events(self, event):
        self.x, self.y = pyautogui.position()
        self.r, self.g, self.b = pyautogui.pixel(self.x, self.y)
        self.xx = '#%02x%02x%02x' % (self.r, self.g, self.b)
        self.parent.configure(bg=str(self.xx))
        self.display.delete(0, END)
        self.display.insert(0, self.xx)

    def motion(self, event):
        x, y = event.x, event.y
        self.x, self.y = pyautogui.position()
        self.r, self.g, self.b = pyautogui.pixel(self.x, self.y)

        self.xx = ('#%02x%02x%02x' % (self.r, self.g, self.b))
        self.parent.configure(bg = str(self.xx))
        self.titlelbl.configure(fg = self.xx)

if __name__ == '__main__':
    try:
        app = application(tk.Tk())
        app.mainloop()
    finally:
        print('\n Done')
