def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    my_list = []
    
    for num in range(1, number - 1):
        if number % num == 0:
            my_list.append(num)

    sum_list = sum(my_list)

    if sum_list == number:
        return "perfect"
    elif sum_list < number:
        return "deficient"
    else:
        return "abundant"
