def factors(value):
    my_list = []
    num = 2
    factoring = True
    while factoring:
        if value % num == 0:
            my_list.append(num)
            value = value / num
        else:
            num += 1
            
        if value == 1:
            factoring = False

    return my_list
