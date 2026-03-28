def convert(number: int) -> str:

    full_string: str = ""

    if number % 3 == 0:
        full_string = full_string + "Pling"
        
    if number % 5 == 0:
        full_string = full_string + "Plang"
        
    if number % 7 == 0:
        full_string = full_string + "Plong"
        
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)

    return full_string
