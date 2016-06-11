#Rewrite the distance function from chapter 5 so that it takes two Points as parameters instead of four numbers.

class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

def distance(a,b):
    return ((a.x-b.x)**2 + (a.y-b.y)**2)**0.5
