import unittest


def encode(plaintext):
    if plaintext == '':
        return plaintext

    ciphertext = ''
    current_char = plaintext[0]
    series_count = 0

    for letter in plaintext:
        if letter == current_char:
            series_count += 1
        else:
            ciphertext += compress_series(current_char, series_count)
            current_char = letter
            series_count = 1

    ciphertext += compress_series(current_char, series_count)

    return ciphertext


def compress_series(character, quantity):
    if quantity == 1:
        return character
    else:
        return str(quantity) + character


def decode(ciphertext):
    quantity = ''
    plaintext = ''
    for letter in ciphertext:
        if letter.isdigit():
            quantity += letter
        else:
            if quantity == '':
                plaintext += letter
            else:
                plaintext += int(quantity) * letter
                quantity = ''

    return plaintext