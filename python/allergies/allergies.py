possible_allergies = ['cats', 'pollen', 'chocolate', 'tomatoes', 'strawberries', 'shellfish', 'peanuts', 'eggs']
max_score = 255


class Allergies(object):
    def __init__(self, score):
        self.my_allergies = []

        if score > max_score:
            score %= max_score + 1

        # convert to binary without prefix  0b
        score = bin(score)[2:]

        if len(score) < len(possible_allergies):
            score = (len(possible_allergies) - len(score)) * '0' + score

        #every bit in binary number says if sb has allergy on sth or no
        self.my_allergies = [possible_allergies[i] for i in range(len(possible_allergies)) if score[i] == '1']

    def is_allergic_to(self, item):
        return True if item in self.my_allergies else False

    @property
    def lst(self):
        return self.my_allergies


if __name__ == '__main__':
    e = Allergies(1)
    print(e.my_allergies)
