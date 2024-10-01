import tkinter as tk
from tkinter import *


# UI Functions
def ui_generation():
    
    window = tk.Tk()
    window.title("Genetic Algorithm For  Flowers")
    window.geometry("300x200")
    button = Button(window, text="evolve new generations")
    button.grid(row=0, columnspan=8, pady=(5, 30))
    
    for i in range(1):
      for j in range(0,8):
        frame = tk.Frame(window, borderwidth = 2,  width=150, height=300, bg="white")
        frame.grid(row = 2 , column = j, padx=15)

    
    

    window.mainloop()


