def yacht(combination):
    combination = set(combination)
    
    if len(combination) == 1:
        return 50
    else:
        return 0


def nums(combination, base):
    sum = 0
    
    for dice in combination:
        if dice == base:
            sum += dice

    return sum


def full_house(comb):
    quantity, base = most_common(comb)
    if len(set(comb)) == 2 and quantity == 3:
        return sum(comb)
    else:
        return 0
     


def four_of_a_kind(comb):
    quantity, base = most_common(comb)
    if quantity == 4 or quantity == 5:
        return base * 4
    else:
        return 0

def little_straight(comb):
    comb.sort()
    
    for i in range(5):
        if i+1 != comb[i]:
            return 0

    return 30
            
def big_straight(comb):
    comb.sort()

    for i in range(5):
        if i+2 != comb[i]:
            return 0

    return 30

def choice(comb):
   return sum(comb)


def most_common(seq):
    seq.sort()
    
    #max_quantity = [quantity, base]
    max_quantity = [0, 0]
    counter = [0, 0]
    
    for element in seq:
        if element != counter[1]:
            counter = [1, element]
        else:
            counter[0] += 1

        if counter[0] > max_quantity[0]:
            max_quantity = counter[:]


    return max_quantity# Score categories
# Change the values as you see fit
YACHT = yacht
ONES = lambda comb : nums(comb, 1)
TWOS = lambda comb : nums(comb, 2)
THREES = lambda comb : nums(comb, 3) 
FOURS = lambda comb : nums(comb, 4)
FIVES = lambda comb : nums(comb, 5)
SIXES = lambda comb : nums(comb, 6)
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = choice


def score(dice, category):
    return category(dice)


