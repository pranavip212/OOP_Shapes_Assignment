import tkinter as tk
from tkinter import *
from tkinter.ttk import *
#from NewWIndowClass import NewWindow
from tkinter import messagebox
#from PIL import Image, ImageTk
#citation: https://www.geeksforgeeks.org/python/open-a-new-window-with-a-button-in-python-tkinter/
def open_new_window():
    # Create the new Toplevel window
    new_window = tk.Toplevel(master)
    new_window.title("New Window with Widgets")
    new_window.geometry("300x200") # Set the window size

    # Add a Label to the new window
    label = tk.Label(new_window, text="This is the new window!")
    label.pack(pady=10)

    # Add an Entry (input) widget to the new window
    entry = tk.Entry(new_window, width=20)
    entry.pack(pady=5)

master = Tk()
master.title("SHAPE PROGRAM")
master.geometry('800x750')
master.configure(bg="#ffd6e7")  #bg color
Label(master, text="This is the main window").pack(pady=10)
Button(master, text="Add Gloss", width=15, command=open_new_window).pack(pady=10)
"""
btn = Button(master, text="Open Sphere Window ")
btn.bind("<Button>", lambda e: NewWindow(master))  # Bind the event

btn.pack(pady=10)

btn = Button(master, text="Open Gabriel's Horn Window ")
btn.bind("<Button>", lambda e: NewWindow(master))  # Bind the event

btn.pack(pady=10)
"""


# Run the Tkinter event loop
master.mainloop()