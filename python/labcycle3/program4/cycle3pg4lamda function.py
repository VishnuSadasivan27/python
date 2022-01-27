print("Write lambda functions to find area of square, rectangle and triangle.")
print("Area of Square")
l = float(input("Enter the length of a side of a square : "))
area_sqr = lambda a: a ** 2
print(f'Area of a square with side length={l} is {area_sqr(l)} sqm')
print("\n")

print("Area of Rectangle")
length = float(input("Enter the length : "))
breadth = float(input("Enter the breadth : "))
area_rec = lambda a, b: a * b
print(f'Area of a rectangle with side length={length} & breadth={breadth} is {area_rec(length, breadth)} sqm')
print("\n")

print("Area of triangle.")
length = float(input("Enter the length : "))
breadth = float(input("Enter the height : "))
area_tri = lambda a, b: 0.5 * a * b
print(f'Area of a triangle with side length={length} & breadth={breadth} is {area_tri(length, breadth)} sqm')
print("\n")
