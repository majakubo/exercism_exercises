class HighScores(object):
    def __init__(self, scores):
        self.scores = scores[:]
        self.sorted_scores = scores[:]
        self.sorted_scores.sort()
        self.sorted_scores.reverse()

    def latest(self):
        return self.scores[-1]

    def top(self):
        return self.sorted_scores[:3]

    def highest(self):
        return self.sorted_scores[0]

    def report(self):
        last = self.scores[-1]
        best = self.sorted_scores[0]
        if last == best:
            return "Your latest score was {}. That's your personal best!".format(best)
        else:
            return "Your latest score was {}. That's {} short of your personal best!".format(last, (best - last))






