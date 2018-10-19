def word_count(phrase):
    word_list = phrase.split()
    used_words = dict()
    
    for word in word_list:
        if word in used_words.keys():
            used_words[word] += 1
        else:
            used_words[word] = 1

    for word, occurences in used_words.items():
        print(word, ':   ', occurences)

    return used_words
