def is_valid(isbn):
    isbn_list = []
    isbn = isbn.replace('-', '')
    
    if len(isbn) != 10:
        return False

    if 'X' in isbn and isbn.index('X') != 9:
        return False
        
    for char in isbn:
        if char.isalpha():
            if char == 'X':
                isbn_list.append(10)
            else:
                return False
        else:
            isbn_list.append(int(char))

    return (isbn_list[0] * 10 + isbn_list[1] * 9 + isbn_list[2] * 8 + isbn_list[3] * 7 +
           isbn_list[4] * 6 + isbn_list[5] * 5 + isbn_list[6] * 4 + isbn_list[7] * 3 + 
           isbn_list[8] * 2 + isbn_list[9] * 1) % 11 == 0

