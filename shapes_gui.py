import tkinter as tk
from tkinter import *

#from NewWIndowClass import NewWindow
from tkinter import messagebox
#from PIL import Image, ImageTk
#citation: https://www.geeksforgeeks.org/python/open-a-new-window-with-a-button-in-python-tkinter/
def open_new_window():
    # Create the new Toplevel window
    new_window = tk.Toplevel(master)
    new_window.title("Sphere Calculator!")
    new_window.geometry("300x200") # Set the window size

    # Add a Label to the new window
    label = tk.Label(new_window, text="Enter the dimensions for your sphere!")
    label.pack(pady=10)

    # Add an Entry (input) widget to the new window
    instruction = tk.Label(new_window, text="Enter the radius of the sphere!")
    instruction.pack(pady=10)
    rad_entry = Entry(new_window)
    rad_entry.pack(pady=2)

    Label(new_window, text="Color", bg='#ffd6e7').pack(pady=5)
    # Create a Tkinter variable
    colorVar = StringVar(new_window)
    color_options = ['red', 'blue', 'green', 'pink', 'purple', 'orange', 'yellow']

    colorOptionMenu = OptionMenu(new_window, colorVar, *color_options)
    colorOptionMenu.config(width=30, bg="lightpink",
                          activebackground="blue",
                          fg="black",
                          activeforeground="pink")
    colorOptionMenu.pack(pady=5)

master = Tk()
master.title("SHAPE PROGRAM")
master.geometry('800x750')
master.configure(bg="#ffd6e7")  #bg color
Label(master, text="This is the main window").pack(pady=10)
Button(master, text="Create Sphere", width=15, command=open_new_window).pack(pady=10)
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