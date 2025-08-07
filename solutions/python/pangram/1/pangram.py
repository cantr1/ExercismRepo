import string
def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)

    for letter in sentence.lower():
        if letter in alphabet:
            alphabet.remove(letter)

    return not alphabet