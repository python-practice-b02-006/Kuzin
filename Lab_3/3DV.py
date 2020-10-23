from random import randint, uniform
import math

class THREEDV():
    def __init__(self, X, Y, Z):
        self.x = X
        self.y = Y
        self.z = Z
        
    def __str__(self):
        return '<%s, %s, %s>' % (self.x, self.y, self.z)   
        
    def module(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)    
        
    def __copy(self):
        return THREEDV(self.x, self.y, self.z)    
    
    def __add__(self, inst):
        return THREEDV(self.x + inst.x , self.y + inst.y , self.z + inst.z)
        
    def __mul__(self, number):
        return THREEDV(self.x*number, self.y*number, self.z*number)
    
    def __matmul__(self, inst):
        return THREEDV(self.y*inst.z - self.z*inst.y, self.z*inst.x - self.x*inst.z, self.x*inst.y - self.y*inst.x)
    
    def __div__(self, number):
        return self.__copy() * (number**-1)
    
    def __and__(self, inst):
        return self.x*inst.x + self.y*inst.y + self.z*inst.z    
        
    def normal(self):
        return self.__copy() / self.module()  
        
V3D1 = THREEDV(1, 4, 2)
V3D2 = THREEDV(7, 1, 3)

A = V3D1 + V3D2

print(A.normal)
    
    