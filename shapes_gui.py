from tkinter import *
from tkinter.ttk import *
from NewWIndowClass import NewWindow
from tkinter import messagebox
#from PIL import Image, ImageTk
#citation: https://www.geeksforgeeks.org/python/open-a-new-window-with-a-button-in-python-tkinter/

master = Tk()
master.title("SHAPE PROGRAM")
master.geometry('800x750')
master.configure(bg="#ffd6e7")  #bg color
Label(master, text="This is the main window").pack(pady=10)

btn = Button(master, text="Open Sphere Window ")
btn.bind("<Button>", lambda e: NewWindow(master))  # Bind the event

btn.pack(pady=10)

btn = Button(master, text="Open Gabriel's Horn Window ")
btn.bind("<Button>", lambda e: NewWindow(master))  # Bind the event

btn.pack(pady=10)

# Run the Tkinter event loop
master.mainloop()