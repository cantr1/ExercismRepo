def square_root(number: int):
    if number == 1:
        return number
    for num in range(1, number):
        if num * num == number:
            return num
    