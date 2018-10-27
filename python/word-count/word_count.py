def word_count(phrase):
    phrase = ''.join([i for i in phrase if i.isalpha()])
    phrase = phrase.lower()
    words = phrase.split()
    words_frequency = dict()
    for word in words:
        if word in words_frequency.keys():
            words_frequency[word] += 1
        else:
            words_frequency[word] = 1


    return words_frequency
