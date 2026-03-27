def square(number):
    total_grain = 1
    if number > 64 or number <= 0:
        raise ValueError("square must be between 1 and 64")
    for num in range (1, number):
        total_grain *= 2
    return total_grain


def total():
    return 2**64 - 1
