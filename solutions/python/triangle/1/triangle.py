def is_triangle(a, b, c):
    if a + b >= c and b + c >= a and a + c >= b and min(a,b,c) > 0:
        return True
    return False

def equilateral(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    return is_triangle(a, b, c) and a == b == c

def isosceles(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if is_triangle(a, b, c): 
        return (a == b) or (a == c) or (b == c)
    else:
        return False

def scalene(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if is_triangle(a, b, c):
        return a != b and b !=c and a != c
    else:
        return False
    
