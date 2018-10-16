def is_isogram(string):
    string = string.lower()
    used_letters = set()
    special_letters = {' ', '-'}
    
    for letter in string:
        if letter in used_letters and not letter in special_letters:
               return False
        else:
            used_letters.add(letter)

    return True
