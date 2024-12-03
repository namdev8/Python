from graphics import circle,rectangle
r=int(input("Enter radius of the circle: "))
circle.areac(r)
circle.peric(r)
l=int(input("Enter length of the rectangle: "))
b=int(input("Enter breadth of the rectangle: "))
rectangle.arear(l,b)
rectangle.perir(l,b)

from graphics.drgraphics import cuboid,sphere

l1=int(input("\n enter the lenght of cuboid:"))
b1=int(input("\n enter the breadth of cuboid:"))
h1=int(input("\n enter the height of cuboid:"))
cuboid.areacub(l1,b1,h1)
cuboid.pericub(l1,b1,h1)

r1=int(input("\n enter the radius of sphere:"))
sphere.area(r1)
sphere.peris(r1)