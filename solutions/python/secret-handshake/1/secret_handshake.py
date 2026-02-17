def commands(binary_str):
    my_list = []

    if binary_str[len(binary_str) - 1] == '1':
        my_list.append("wink")
    if binary_str[len(binary_str) - 2] == '1':
        my_list.append("double blink")
    if binary_str[len(binary_str) - 3] == '1':
        my_list.append("close your eyes")
    if binary_str[len(binary_str) - 4] == '1':
        my_list.append("jump")

    if len(binary_str) == 5:
        if binary_str[0] == '1':
            return my_list[::-1]
    return my_list