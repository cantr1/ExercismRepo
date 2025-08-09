from collections import Counter

def find_anagrams(word, candidates):
    word_list = list(word.lower())
    anagram_words = []
    
    for item in candidates:
        if Counter(item.lower()) == Counter(word.lower()):
            is_anagram = True
            if len(item) != len(word):
                is_anagram = False
            elif item.lower() == word.lower():
                is_anagram = False
            else:
                track_list = []
                for char in item:
                    track_list.append(char)
                    if char.lower() not in word_list:
                        is_anagram = False
                        break
                    
                if is_anagram:
                    anagram_words.append(item)

    return anagram_words
            
                
            
