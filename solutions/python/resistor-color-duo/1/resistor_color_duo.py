def value(colors):
    color_dict = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }
    total = ""
    for color in colors:
        total = total + str(color_dict[color])

    return int(total[:2])
