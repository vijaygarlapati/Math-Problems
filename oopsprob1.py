#Problem 1
#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line():
    
    def __init__(self,cord1,cord2):
        self.cord1 = cord1
        self.cord2 = cord2
        
    def distance(self):
        from math import sqrt
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return sqrt((x2-x1)**2 + (y2-y1)**2)
    
    def slope(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return (y2-y1)/(x2-x1)
      
