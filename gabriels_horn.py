from baseShape import Shape3D
import math


class GabrielsHorn(Shape3D):
   def __init__(self, color, b,  x=0, y=0, z=0):
       super().__init__("Gabriel's Horn", color, x, y, z)
       #type is hardcoded here but only because every instance of the class will be a sphere
       #so its redundant to keep asking the user to type it when they create a sphere
       if b <= 1:
           raise ValueError("Invalid value for b")
       self._b = b
   #for gabe's horn, the volume when x = 1, and x = b will never be bigger than pi.
   #the volume approaches pi as 'b' approaches infinity.
   #technically, the vol is taken by splitting the shape into a bunch of thin disks

   def get_b(self):
       return self._b

   def set_b(self, b):
       if b <= 1:
           raise ValueError("Invalid value for b")
       self._b = b

   def volume(self):
       return math.pi * (1 - (1 / self._b))


   def surface_area(self):
       #this is the interesting part of this shape. Even though there is a finite volume,
       #the surface area will be infinite for any finite 'b' value.
       # this is because the SA formula uses a divergent intergral, so the area grows infinite as the
       #horn extends infinitely far.
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
           Volume = {round(self.volume(), 4)} (approaches π ≈ 3.1416 as b approaches ∞)
           Surface Area = infinite!!
           Location: ({self.get_location().get_x()}, {self.get_location().get_y()}, {self.get_location().get_z()})
           """)
