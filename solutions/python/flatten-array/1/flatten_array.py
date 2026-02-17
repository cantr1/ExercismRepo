def flatten(iterable):
    processed_list = []
    for item in iterable:
        if item is None:
            continue
        elif isinstance(item, list):
            processed_list.extend(flatten(item)) 
        else:
            processed_list.append(item)

    return processed_list
