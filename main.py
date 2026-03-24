from sphere import Sphere
from gabriels_horn import GabrielsHorn

s = Sphere("red", 5, 1, 2, 3)

print(s.get_type())         # Sphere
print(s.get_color())        # red
print(s.get_radius())       # 5
print(s.volume())           # 523.598...
print(s.surface_area())     # 314.159...
s.draw()


s.set_radius(10)
print(s.get_radius())       # 10


g = GabrielsHorn("gold", 1000)
print(g.volume())       # very close to pi
print(g.surface_area()) # inf
g.draw()


"""s = Shape3D("Generic", "red", 1, 2, 3)


print(s.get_type())                 # Generic
print(s.get_color())                # red
print(s.get_location().get_x())     # 1
print(s.get_location().get_y())     # 2
print(s.get_location().get_z())     # 3


s.set_location(4, 5, 6)
print(s.get_location().get_x())     # 4
print(s.get_location().get_y())     # 5
print(s.get_location().get_z())     # 6


s.set_color("blue")
s.set_type("Updated")
print(s.get_color())                # blue
print(s.get_type())                 # Updated


print(s.volume())                   # None
print(s.surface_area())          """  # None
