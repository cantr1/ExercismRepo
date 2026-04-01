def find(search_list, value):
    search_list.sort()
    modified_list = search_list

    if value not in search_list:
        raise ValueError("value not in array")

    item_found = False
    while item_found == False:
        mid_index = len(modified_list) // 2
        mid_item = modified_list[mid_index]

        if mid_item == value:
            return search_list.index(value)
        elif mid_item > value:
            modified_list = modified_list[:mid_index]
        elif mid_item < value:
            modified_list = modified_list[mid_index + 1:]