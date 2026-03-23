class Location3D:
   def __init__(self, x=0, y=0, z=0):
       self._x = x
       self._y = y
       self._z = z


# getters + setters for coords


   def get_x(self):
       return self._x


   def set_x(self, x):
       self._x = x


   def get_y(self):
       return self._y


   def set_y(self, y):
       self._y = y


   def get_z(self):
       return self._z


   def set_z(self, z):
       self._z = z


   def get_location(self):
       return (self._x, self._y, self._z)


   def set_location(self, x, y, z):
       self._x = x
       self._y = y
       self._z = z
