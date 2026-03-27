def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == 0 and b == 0 and c == 0:
        return False
    
    if c > a + b:
        return False
        
    if a > c + b:
        return False
        
    if b > c + a:
        return False
    
    if a == b and b == c:
        return True
    else:
        return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if c > a + b:
        return False
        
    if a > c + b:
        return False
        
    if b > c + a:
        return False

    if a == b or a == c or b == c:
        return True
    else:
        return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if c > a + b:
        return False
        
    if a > c + b:
        return False
        
    if b > c + a:
        return False
    

    if a != b and b != c and a != c:
        return True
    else:
        return False
