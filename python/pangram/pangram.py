def is_pangram(sentence):
    import string
    alphabet = set(string.ascii_lowercase)
    
    
    #make s.lower to avoid duplications
    sentence = sentence.lower() 

    letters = set()
   
    for letter in sentence:
       if not letter in letters:
           letters.add(letter)

    
    if alphabet.issubset(letters):
        return True
    else:
        return False

