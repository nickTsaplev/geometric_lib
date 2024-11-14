from geometry import isLength

def area(a):
        ''' принимает сторону квадрата a, возвращает площадь квадрата со стороной a'''
        assert (isLength(a)), f"The square side should be a nonegative number: {a=}"
    
        return a * a

def perimeter(a):
        ''' принимает сторону квадрата a, возвращает периметр квадрата со стороной a'''
        assert (isLength(a)), f"The square side should be a nonegative number: {a=}"
        
        return 4 * a
