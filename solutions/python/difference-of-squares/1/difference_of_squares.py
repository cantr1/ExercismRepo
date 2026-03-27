def square_of_sum(number):
    my_list = []
    if number == 1:
        return number
        
    for _ in range(1, number + 1):
        my_list.append(_)

    return sum(my_list)**2


def sum_of_squares(number):
    my_list = []
    for _ in range(1, number + 1):
        my_list.append(_**2)

    return sum(my_list)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
