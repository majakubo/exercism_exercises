import string

# create mapping from normal alphabet to cipher
letters = list(string.ascii_lowercase)
key = letters[:]
key.reverse()

encode_map = dict(zip(letters, key))
decode_map = dict(zip(key, letters))


def encode(plain_text):
    plain_text = plain_text.lower()
    ciphered_text = ''
    for letter in plain_text:
        if letter.isalpha():
            ciphered_text += encode_map[letter]
        else:
            ciphered_text += letter

    ciphered_text = list(ciphered_text)
    ciphered_text.reverse()
    ciphered_text = ''.join(ciphered_text)
    return ciphered_text


def decode(ciphered_text):
    return encode(ciphered_text)