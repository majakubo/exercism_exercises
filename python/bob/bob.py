import re
def hey(phrase):
    #phrase = clear_str(phrase)
    isQuestion = is_it_question(phrase)
    isYelling = is_it_yelling(phrase)
    isSentence = does_it_says_sth(phrase)
    
    if isQuestion and isYelling:
        return "Calm down, I know what I'm doing!"
    elif isQuestion and not isYelling:
        return "Sure."
    elif not isQuestion and not isYelling:
        return "Whatever."
    elif not isQuestion and isYelling:
        return "Whoa, chill out!"
    if not isSentence:
        return "Fine. Be that way!"




def is_it_yelling(phrase):
    if phrase.upper() == phrase:
        return True
    else:
        return False

def is_it_question(phrase):
    if len(phrase) == 0:
        return False

    if phrase[-1] == '?':
        return True
    else:
        return False

def does_it_says_sth(phrase):
    return re.search('[a-zA-Z]', phrase) 

def clear_str(phrase):
    phrase = [letter for letter in phrase if letter.isalpha()]
    return ''.join(phrase) 
