from geometry import isLength

def area(a, b): 
    ''' принимает стороны прямоугольника a и b, возвращает площадь прямоугольника со сторонами a и b'''
    assert (isLength(a) and isLength(b)), f"The rectangle sides should be nonegative numbers: {a=}, {b=}"
    
    return a * b 

def perimeter(a, b): 
    ''' принимает стороны прямоугольника a и b, возвращает периметр прямоугольника со сторонами a и b'''
    assert (isLength(a) and isLength(b)), f"The rectangle sides should be nonegative numbers: {a=}, {b=}"

    return 2 * (a + b) 
