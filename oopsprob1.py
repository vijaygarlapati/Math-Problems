#Problem 1
#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class line():
    
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def distance(self):
        from math import sqrt
        return sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)
    
    def slope(self):
        return (self.y2-self.y1)/(self.x2-self.x1)
      
