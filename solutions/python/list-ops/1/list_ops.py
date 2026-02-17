def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    my_list = []
    for list in lists:
        my_list.extend(list)
    return my_list


def filter(function, list):
    my_list = []
    for item in list:
        if function(item):
            my_list.append(item)
    return my_list


def length(list):
    return len(list)


def map(function, list):
    my_list = [function(item) for item in list]
    return my_list


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in reversed(list):
        initial = function(initial, item)
    return initial


def reverse(list):
    return list[::-1]
