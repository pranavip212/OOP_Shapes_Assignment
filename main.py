from sphere import Sphere
from gabriels_horn import GabrielsHorn

s = Sphere("red", 5, 1, 2, 3)

print(s.get_type())         # Sphere
print(s.get_color())        # red
print(s.get_radius())       # 5
print(s.volume())           # 523.598
print(s.surface_area())     # 314.159
s.draw()


s.set_radius(10)
print(s.get_radius())       # 10


g = GabrielsHorn("gold", 1000)
print(g.volume())       # very close to pi
print(g.surface_area()) # inf
g.draw()

shapes = [s, g]

for shape in shapes:
    print(f"{shape.get_type()} Volume: {round(shape.volume(), 4)}")
    print(f"{shape.get_type()} Surface Area: {round(shape.surface_area(), 4)}")
    print('\n')
    shape.draw()



#proof of initial testing
"""s = Shape3D("Generic", "red", 1, 2, 3)
print(s.get_type())
print(s.get_color())                
print(s.get_location().get_x())     
print(s.get_location().get_y())     
print(s.get_location().get_z())     


s.set_location(4, 5, 6)
print(s.get_location().get_x())
print(s.get_location().get_y()) 
print(s.get_location().get_z())


s.set_color("blue")
s.set_type("Updated")
print(s.get_color())
print(s.get_type())


print(s.volume())                   
print(s.surface_area())          """
