class Rectangle:
    def __init__(self, lenght, breadht):
        self.lenght = lenght
        self.breadht = breadht
    def area(self):
        return self.lenght * self.breadht
    def perimeter(self):
        return 2 * (self.lenght + 2 * self.breadht)

    def display(self):
        print("area of rectangle is ", self.area())
        print("perimeter of rectangle is ", self.perimeter())

    def compare_area(self, other):
            if self.area()==other.area():
                print("\n rectangle is equal in area.")
            elif self.area()>other.area():
                print("\n rectangle 1 is greater in area than rectangle 2.")
            else:
                print("\n rectangle 2 is greater in area than rectangle 1.")

print("enter the diamentions of first rectangle:")
lenght1 = int(input("enter lenght1:"))
breadht1 = int(input("enter breadht1:"))
rect1 = Rectangle(lenght1, breadht1)
rect1.display()

print("enter the diamentions of second rectangle:")
lenght2 = int(input("enter lenght2:"))
breadht2 = int(input("enter breadht2:"))
rect2 = Rectangle(lenght2, breadht2)
rect2.display()

rect1.compare_area(rect2)
