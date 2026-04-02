import tkinter as tk
from tkinter import *
from tkinter import messagebox
from sphere import Sphere
from gabriels_horn import GabrielsHorn


#from PIL import Image, ImageTk


def load_gif(file):
   frames = []
   i = 0
   while True:
       try:
           frame = tk.PhotoImage(file=file, format=f"gif -index {i}")
           frames.append(frame)
           i += 1
       except:
           break
   return frames

# citation: https://devhubcommunity.hashnode.dev/displaying-gifs-in-tkinter-python
def animate_gif(label, frames, index=0):
   frame = frames[index]
   label.config(image=frame)
   label.image = frame
   index = (index + 1) % len(frames)
   label.after(100, lambda: animate_gif(label, frames, index))




#citation: https://www.geeksforgeeks.org/python/open-a-new-window-with-a-button-in-python-tkinter/
def open_sphere_window():
   # Create the new Toplevel window
   new_window = tk.Toplevel(master)
   new_window.title("Sphere Calculator!")
   new_window.geometry("300x400")
   tk.Label(new_window, text="Enter the dimensions for your sphere!", font=("Helvetica", 14, "bold"), bg="#ffe4e1").grid(row=0, column=0, columnspan=2, pady=10)




   # Add an Entry (input) widget to the new window
   tk.Label(new_window, text="Radius:", bg="#ffe4e1").grid(row=1, column=0, sticky="e")
   rad_entry = Entry(new_window)
   rad_entry.grid(row=1, column=1)


   #color
   tk.Label(new_window, text="Color:", bg="#ffe4e1").grid(row=2, column=0, sticky="e")
   colorVar = StringVar(new_window)
   colorVar.set("red")
   colors = ['red', 'blue', 'green', 'pink', 'purple', 'orange', 'yellow']
   tk.OptionMenu(new_window, colorVar, *colors).grid(row=2, column=1)


   #coords
   tk.Label(new_window, text="X:", bg="#ffe4e1").grid(row=3, column=0, sticky="e")
   x_entry = Entry(new_window)
   x_entry.grid(row=3, column=1)


   tk.Label(new_window, text="Y:", bg="#ffe4e1").grid(row=4, column=0, sticky="e")
   y_entry = Entry(new_window)
   y_entry.grid(row=4, column=1)


   tk.Label(new_window, text="Z:", bg="#ffe4e1").grid(row=5, column=0, sticky="e")
   z_entry = Entry(new_window)
   z_entry.grid(row=5, column=1)


   result_label = tk.Label(new_window, text="", font=("Courier", 11, "bold"), bg="#fffacd", justify="left", bd=2, relief="solid", padx=10, pady=5)
   result_label.grid(row=7, column=0, columnspan=2, pady=10, sticky="ew")


   ## gif setup

   sphere_gif_file = "sphere.gif"


   frames = load_gif(sphere_gif_file)


   gif_label = tk.Label(new_window, bg="#ffe4e1")
   gif_label.grid(row=8, column=0, columnspan=2, pady=10)




   def calculate():
       try:
           r = float(rad_entry.get())
           x = float(x_entry.get())
           y = float(y_entry.get())
           z = float(z_entry.get())
           color = colorVar.get()


           s = Sphere(color, r, x, y, z)


           result_label.config(text=
                               f"Type: {s.get_type()}\n"
                               f"Color: {s.get_color()}\n"
                               f"Location: ({x}, {y}, {z})\n"
                               f"Volume: {round(s.volume(), 2)} units cubed\n"
                               f"Surface Area: {round(s.surface_area(), 2)} units squared"
                               #f"{s.draw()}"
                               )
           animate_gif(gif_label, frames)
           s.draw()


       except ValueError:
           messagebox.showerror("Error", "Invalid input!")


   Button(new_window, text="Calculate", command=calculate).grid(row=6, column=0, columnspan=2, pady=10)


def open_horn_window():
   # Create the new Toplevel window
   new_window = tk.Toplevel(master)
   new_window.title("Gabriel's Horn Calculator!")
   new_window.geometry("500x500")
   new_window.configure(bg="#e0ffff")  # light cyan


   tk.Label(new_window, text="Enter Gabriel's Horn Details", font=("Helvetica", 14, "bold"), bg="#e0ffff").grid(row=0, column=0, columnspan=2, pady=10)


   # Add an Entry (input) widget to the new window
   tk.Label(new_window, text="B value (>1):", bg="#e0ffff").grid(row=1, column=0, sticky="e")
   b_entry = tk.Entry(new_window)
   b_entry.grid(row=1, column=1)


   #color
   tk.Label(new_window, text="Color:", bg="#e0ffff").grid(row=2, column=0, sticky="e")
   hornColorVar = StringVar(new_window)
   hornColorVar.set("red")
   color_options = ['red', 'blue', 'green', 'pink', 'purple', 'orange', 'yellow']
   OptionMenu(new_window, hornColorVar, *color_options).grid(row=2, column=1)


   #coords
   tk.Label(new_window, text="X:", bg="#e0ffff").grid(row=3, column=0, sticky="e")
   x_entry = tk.Entry(new_window)
   x_entry.grid(row=3, column=1)


   tk.Label(new_window, text="Y:", bg="#e0ffff").grid(row=4, column=0, sticky="e")
   y_entry = tk.Entry(new_window)
   y_entry.grid(row=4, column=1)


   tk.Label(new_window, text="Z:", bg="#e0ffff").grid(row=5, column=0, sticky="e")
   z_entry = tk.Entry(new_window)
   z_entry.grid(row=5, column=1)


   result_label = tk.Label(new_window, text="", font=("Courier", 11, "bold"), bg="#f0e68c", justify="left", bd=2, relief="solid", padx=10, pady=5)
   result_label.grid(row=7, column=0, columnspan=2, pady=10, sticky="ew")


   horn_gif_file = "gabrielsHorn.gif"
   frames = load_gif(horn_gif_file)
   gif_label = tk.Label(new_window, bg="#e0ffff")
   gif_label.grid(row=8, column=0, columnspan=2, pady=10)


   def calculate():
       try:
           b = float(b_entry.get())
           if b <= 1:
               messagebox.showerror("Error", "B must be greater than 1!")
               return
           x = float(x_entry.get())
           y = float(y_entry.get())
           z = float(z_entry.get())
           color = hornColorVar.get()


           g = GabrielsHorn(color, b, x, y, z)


           result_label.config(text=
                               f"Type: {g.get_type()}\n"
                               f"Color: {g.get_color()}\n"
                               f"Location: ({x}, {y}, {z})\n"
                               f"Volume: {round(g.volume(), 4)} units cubed\n"
                               f"Surface Area: infinite\n"
                               #f"{g.draw()}"
                               )
           animate_gif(gif_label, frames)
           g.draw()
       except ValueError:
           messagebox.showerror("Error", "Invalid input!")


   tk.Button(new_window, text="Calculate", command=calculate, bg="#20b2aa", fg="white",
                 font=("Helvetica", 12, "bold")).grid(row=6, column=0, columnspan=2, pady=10)




master = Tk()
master.title("SHAPE PROGRAM")
master.geometry('400x400')
master.configure(bg="#ffd6e7")  #bg color
Label(master, text="This is the main window").grid(row=0, column=6, columnspan=2, pady=10)
Button(master, text="Create Sphere", width=15, command=open_sphere_window).grid(row=1, column=4, columnspan=2, pady=10)
Button(master, text="Create Horn", width=15, command=open_horn_window).grid(row=2, column=4, columnspan=2, pady=10)



master.mainloop()
