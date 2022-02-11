#To find out the volume and surface area of cylinder

class Cylinder():
    def __init__(self,height=1,radious=1):
        self.height = height
        self.radious = radious
    def volume(self):
        pi = 3.14
        return pi*(self.radious**2)*self.height
    def surface_area(self):
        pi = 3.14
        return 2*pi*(self.radious)*(self.radious + self.height)
