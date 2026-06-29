class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.dem = d

    def __str__(self):
        return "{}/{}".format(self.num, self.dem)

    def __add__(self, other):
        temp_num = (self.num * other.dem) + (self.dem * other.num)
        temp_dem = self.dem * other.dem
        return "{}/{}".format(temp_num, temp_dem)
    
    def __sub__(self, other):
        temp_num = (self.num * other.dem) - (self.dem * other.num)
        temp_dem = self.dem * other.dem
        return "{}/{}".format(temp_num, temp_dem)
    
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_dem = self.dem * other.dem
        return "{}/{}".format(temp_num, temp_dem)
    
    def __truediv__(self, other):
        temp_num = self.num * other.dem
        temp_dem = self.dem * other.num
        return "{}/{}".format(temp_num, temp_dem)


x = Fraction(3, 7)
y = Fraction(5, 8)

print(x + y)
print(x-y)
print(x*y)
print(x/y)





##  goal(1) is to make the coordinate system by using magic method
##  goal(2) is to make teh martix operation using magic method