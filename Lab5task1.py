import math

class point:
    
    def __init__(self):
        self.x=0
        self.y=0

def distance_between_points(a,b):
    d1 = a.x - b.x
    d2 = a.y - b.y

    distance = math.sqrt(d1**2 + d2**2)
    return distance

x = point()   
y = point()         
print(x)
print(y)
print(x != y)

p0 = point()
p0.x = input("Enter value of point x1:")
p0.y = input("Enter value of point y1:")

p1 = point()
p1.x = input("Enter value of point x2:")
p1.y = input("Enter value of point y2:")
print('Distance is,')
print(distance_between_points(p1, p0))
