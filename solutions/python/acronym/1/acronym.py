import string

def abbreviate(words):
    words = words.replace('-', ' ')
    translator = str.maketrans('', '', string.punctuation)
    words = words.translate(translator)
    caps = words.title()
    acronym = ''.join([ch for ch in caps if ch.istitle()])

    return acronym