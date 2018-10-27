def find_anagrams(word, candidates):
    anagrams = []
    word_list = list(word.lower())
    word_list.sort()

    for candidate in candidates:
        candidate_list = list(candidate.lower())
        candidate_list.sort()

        if candidate_list == word_list and candidate.lower() != word.lower():
            anagrams.append(candidate)

    return anagrams