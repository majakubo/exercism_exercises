def rotate(text, key):
    text = list(text)
    for i in range(len(text)):
        if text[i].isalpha():
            character = text[i]
            text[i] = shift(character, key)

    return ''.join(text)


def shift(character, key):
    code = ord(character) + key

    if character.islower():
        if code < ord('a'):
            code = ord('z') - (ord('a') - code)
        elif code > ord('z'):
            code = ord('a') + (code - ord('z')) - 1
    else:
        if code < ord('A'):
            code = ord('Z') - (ord('A') - code)
        elif code > ord('Z'):
            code = ord('A') + (code - ord('Z')) - 1

    return chr(code)



