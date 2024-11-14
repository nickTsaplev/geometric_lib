from geometry import isLength

def area(a, h): 
    ''' принимает сторону треугольника a и высоту треугольника с основанием на этой стороне h, возвращает площадь такого треугольника'''

    assert (isLength(a) and isLength(h)), f"The triangle side and height should be nonegative numbers: {a=}, {h=}"
    
    
    return a * h / 2 

def perimeter(a, b, c): 
    ''' принимает стороны треугольника a, b и c, возвращает периметр треугольника со сторонами a, b и c'''
    assert (isLength(a) and isLength(b) and isLength(c)), f"The triangle sides should be nonegative numbers: {a=}, {b=}, {c=}"
        
    
    return a + b + c 
