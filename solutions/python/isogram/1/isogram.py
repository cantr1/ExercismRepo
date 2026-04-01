def is_isogram(string: str) -> bool:
    iso: bool = True
    collected_letters: list = []
    converted_string = string.strip(' -').lower()

    for char in converted_string:
        if char in collected_letters:
            iso = False
        elif char not in collected_letters:
            if char.isalnum():
                collected_letters.append(char)

    print(collected_letters)

    return iso
