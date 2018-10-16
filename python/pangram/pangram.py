def is_pangram(sentence):
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'w', 'x', 'y', 'z'}

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

