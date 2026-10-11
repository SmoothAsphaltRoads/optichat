import random
from collections import defaultdict

class markov:
    def __init__(self, order):
        self.order = order
        self.chain = defaultdict(list)
    def train(self, text):
        words = text.split()
        if len(words)<= self.order:
            return
        for i in range (len(words)-self.order):
            key = tuple(words[i:i+self.order])
            next_word = words[i+self.order]
            self.chain[key].append(next_word)
    def generate(self, length=20, seed=None):
        if not self.chain:
            return ""
        if seed:
            seed_words = tuple(seed.split()[:self.order])
            if seed_words in self.chain:
                current = seed_words
            else:
                current = random.choice (list(self.chain.keys()))
        else:
            current = random.choice(list(self.chain.keys()))
        result = list(current)

        for i in range (length-self.order):
            if current not in self.chain:
                break
            next_word = random.choice(self.chain[current])
            result.append(next_word)
            current = tuple(result[-self.order:])

        return " ".join(result)