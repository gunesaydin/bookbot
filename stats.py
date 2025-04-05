def count_words(content):
    num_words = len(content.split())
    return num_words

def count_letters(content):
    characters = {}

    content = content.lower()

    for char in content:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

def sort_dict(letter_dict):
    sorted_dict = dict(sorted(letter_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict