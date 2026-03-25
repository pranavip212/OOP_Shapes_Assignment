from tkinter import *
from tkinter.ttk import *
# pretty cool feature! used a lambda function and created a small class
#to make the code to open a new window more reusable
class Sphere(Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.title("SPHERES")
        self.geometry("250x150")

        Label(self, text="This is a new window").pack(pady=20)



        # deffirantie between shapes and stop it from creatin
        #more than one window if you press the button more than once

class GabrielsHorn(Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.title("SPHERES")
        self.geometry("250x150")
