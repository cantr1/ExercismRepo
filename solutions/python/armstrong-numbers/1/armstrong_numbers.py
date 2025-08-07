def is_armstrong_number(number):
    total = 0
    length = len(str(number))
    
    for char in str(number):
        total += int(char) ** length
        
    if total == number:
        return True
    else:
        return False
