from location3D import Location3D


class Shape3D:
   def __init__(self, shape_type, color, x=0, y=0, z=0):
       self._type = shape_type #didnt name it type cause of the type funct
       self._color = color
       self._location = Location3D(x, y, z)


   def volume(self):
       return None


   def surface_area(self):
       return None


   def draw(self):
       pass


   def get_color(self):
       return self._color


   def set_color(self, shapeColor):
       self._color = shapeColor


   def get_type(self):
       return self._type


   def set_type(self, shape_type):
       self._type = shape_type
   #did the "create your own class to store coordinates extra credit option


   def get_location(self):
       return self._location


   def set_location(self, x, y, z):
       self._location.set_location(x, y, z)


