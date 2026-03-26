from baseShape import Shape3D
import math


class Sphere(Shape3D):
   def __init__(self, color, radius,  x=0, y=0, z=0):
       super().__init__("Sphere", color, x, y, z)
       #type is hardcoded here but only because every instance of the class will be a sphere
       #so its redundant to keep asking the user to type it when they create a sphere
       self._radius = radius


   def get_radius(self):
       return self._radius

   def set_radius(self, sphere_radius):
       self._radius = sphere_radius
       try:
           if sphere_radius <= 0:
               print("Radius must be positive")
               return
           self._radius = sphere_radius
       except ValueError:
           print(f"Invalid value for radius. Try again.")

   def volume(self):
       return (4 / 3) * math.pi * self._radius ** 3


   def surface_area(self):
       return 4 * math.pi * self._radius ** 2


   def draw(self):
       print(f"""
        *****
      *       *
    *           *
   *             *
    *           *
      *       *
        ***** """)
