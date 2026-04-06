from baseShape import Shape3D
import math


class Sphere(Shape3D):
   def __init__(self, color, radius,  x=0, y=0, z=0):
       super().__init__("Sphere", color, x, y, z)
       #type is hardcoded here but only because every instance of the class will be a sphere
       #so its redundant to keep asking the user to type it when they create a sphere
       if radius <= 0:
           raise ValueError("Invalid radius. Try again.")
       self._radius = radius
# the radius error handling is here too incase someone just calls the constructor rather than the setter
   # and uses an invalid radius there

   def get_radius(self):
       return self._radius


   def set_radius(self, sphere_radius):
       if sphere_radius <= 0:
           raise ValueError("Invalid value for radius. Try again.")
       self._radius = sphere_radius



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
        ***** 
        Sphere: 
           Radius = {self._radius}
           Color: {self.get_color()}
           Volume = {round(self.volume(), 4)}
           Surface Area = {round(self.surface_area(), 4)}
           Location: ({self.get_location().get_x()}, {self.get_location().get_y()}, {self.get_location().get_z()})
              
              
              
              
              
              
             """ )
