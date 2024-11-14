import math
from geometry import isLength

def area(r):
    ''' принимает радиус круга r, возвращает площадь круга радиуса r'''
    
    assert (isLength(r)), f"The circle radius should be a nonegative number: {r=}"
    
    return math.pi * r * r

def perimeter(r):
    ''' принимает радиус окружности r, возвращает периметр окружности радиуса r'''

    assert (isLength(r)), f"The circle radius should be a nonegative number: {r=}"
    
    return 2 * math.pi * r

