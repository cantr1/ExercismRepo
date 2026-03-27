def rotate(text, key):
    alphabet: list = list("abcdefghijklmnopqrstuvwxyz")
    new_text: list = []

    for char in text:
        if char.isalpha():
            starting_point: int = alphabet.index(char.lower())
            ending_point: int = starting_point + key
            if ending_point == 26:
                ending_point = 0
            elif ending_point > 26:
                ending_point = ending_point - 26
                
            new_char: str = alphabet[ending_point]
            if char.isupper():
                new_text.append(new_char.upper())
            else:
                new_text.append(new_char)
        else:
            new_text.append(char)

    return ''.join(new_text)

    
