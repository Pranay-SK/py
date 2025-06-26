import math
class sphere:
    def __init__(self,radius):
        self.radius=radius

    def dia(self):
        return 2*self.radius
    def circu(self):
        return 2*math.pi*self.radius
    def volume(self):
        return (4/3)*math.pi*self.radius**3
    
radius=float(input("Enter radius of sphere:"))
s=sphere(radius)
print("diameter is:",s.dia())
print("circumference is:",s.circu())
print("volume is:",s.volume())
