class Fraction:
    def __init__(self,x ,y):
        self.x = x 
        self.y = y
    def __str__(self):
        return str(f"{self.x}/{self.y}")

    def __add__(self, other):
        num = self.x * other.y + self.y * other.x
        den = self.y * other.y
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.x * other.y - self.y * other.x
        den = self.y * other.y
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.x*other.x
        dem = self.y*other.y
        return Fraction(num,dem)

    def __truediv__(self, other):
        num = self.x*other.y
        dem = self.y*other.x
        return Fraction(num, dem)

    def __eq__(self, other):
        return self.x*other.y == self.y*other.x

      

a=Fraction(3,6)
b= Fraction(4,7)
print(str(a))
c =a+b
d=a-b
e=a*b
f=a/b
print(c)
print(d)
print(e)
print(f)
print(a==b)

        
