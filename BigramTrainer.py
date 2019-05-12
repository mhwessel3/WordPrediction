from collections import defaultdict
import string


class BigramTrainer:

    

    def __init__(self):
        self.bigram_freqs = defaultdict(dict)
        self.unigram_freqs = defaultdict(int)
        self.last_word = ""
        self.USER_MULTIPLER = 50

    def initBigram(self):
        filepath = 'data/w2_.txt'
        with open(filepath) as fp:
            for _, line in enumerate(fp):
                freq, prior, curr = line.rstrip().split('\t')
                freq = int(freq)
                if prior not in self.bigram_freqs:
                    self.bigram_freqs[prior] = defaultdict(int)
                if prior not in self.unigram_freqs:
                    self.unigram_freqs[prior] = freq
                self.unigram_freqs[prior] += freq
                self.bigram_freqs[prior][curr] = freq

    def testBigramDict(self):
        while True:
            print("Prev Word?")
            prev = raw_input()
            if prev not in self.bigram_freqs:
                print("Try again, word not in dictionary")
                continue
            print("Second Word?")
            curr = raw_input()
            if curr not in self.bigram_freqs[prev]:
                print("Try again, word not in dictionary")
                continue
            print(prev, curr, self.bigram_freqs[prev][curr])
    
    def getTopSuggestions(self, prefix, num_sug=3):
        if self.last_word == "" or self.last_word not in self.bigram_freqs:
            top_freqs = sorted(self.unigram_freqs, key=self.unigram_freqs.get, reverse=True)
            suggestions = [word for word in top_freqs if word.startswith(prefix)]
            if len(suggestions) == 0:
                return ""
            return " ".join(suggestions[:num_sug])+"\n"
        possible_words = sorted(self.bigram_freqs[self.last_word], key=self.bigram_freqs[self.last_word].get, reverse=True)
        suggestions = [word for word in possible_words if word.startswith(prefix)]
        if len(suggestions) == 0:
            return ""
        return " ".join(suggestions[:num_sug])+"\n"

    def learn(self, word):
        if word not in self.unigram_freqs:
            self.unigram_freqs[word] = self.USER_MULTIPLER
        else:
            self.unigram_freqs[word] += self.USER_MULTIPLER
        if self.last_word != "":
            if self.last_word not in self.bigram_freqs:
                self.bigram_freqs[self.last_word] = defaultdict(int)
            if word not in self.bigram_freqs[self.last_word]:
                self.bigram_freqs[self.last_word][word] = self.USER_MULTIPLER
            else:
                self.bigram_freqs[self.last_word][word] += self.USER_MULTIPLER
