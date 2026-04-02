from baseShape import Shape3D
import math


class GabrielsHorn(Shape3D):
   def __init__(self, color, b,  x=0, y=0, z=0):
       super().__init__("Gabriel's Horn", color, x, y, z)
       #type is hardcoded here but only because every instance of the class will be a sphere
       #so its redundant to keep asking the user to type it when they create a sphere
       self._b = b
   #for gabe's horn, the volume when x = 1, and x = b will never be bigger than pi.
   #the volume approaches pi as 'b' approaches infinity.
   #technically, the voulme is taken by splitting the shape into a bunch of thin disks
   def get_b(self):
       return self._b

   def set_b(self, b):
       try:
           if b <= 1:
               print("b must be positive and greater than 1")
               return
           self._b = b
       except ValueError:
           print(f"Invalid value for b. Try again.")

   def volume(self):
       return math.pi * (1 - (1 / self._b))


   def surface_area(self):
       #this is the intresting part of this shape. Even though there is a finite volume,
       #the surface area will be infinite for ant finite 'b' value.
       # this is becasue the SA forumla uses a divergent intergal, so the area grows infinite as the
       #horn extends infinitley far.
       return float('inf')


   def draw(self):
            print(f"""
           |>
           | --->
           |  ------->
           |   ----------->
           |  ------->
           | --->
           |>
           Gabriel's Horn: 
           b = {self._b}
           Color: {self.get_color()}
           Volume ≈ {round(self.volume(), 4)} (approaches π ≈ 3.1416 as b → ∞)
           Surface Area = infinite!!
           Location: ({self.get_location().get_x()}, {self.get_location().get_y()}, {self.get_location().get_z()})
           """)
