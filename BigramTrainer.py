from collections import defaultdict
import string


class BigramTrainer:

    def __init__(self):
        self.bigram_freqs = defaultdict(dict)
        self.unigram_freqs = defaultdict(int)
        self.last_word = ""

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
        suggestions = []
        if self.last_word == "":
            top_freqs = sorted(self.unigram_freqs, key=self.unigram_freqs.get, reverse=True)
            
            return " ".join(top_freqs[:num_sug])+"\n"
        if self.last_word not in self.bigram_freqs:
            top_freqs = sorted(self.unigram_freqs, key=self.unigram_freqs.get)
            suggestions = [word for word in possible_words if word.startswith(prefix)]
            if len(suggestions) == 0:
                return ""
            return " ".join(suggestions[:num_sug])+"\n"
        possible_words = sorted(self.bigram_freqs[self.last_word], key=self.bigram_freqs[self.last_word].get, reverse=True)
        suggestions = [word for word in possible_words if word.startswith(prefix)]
        if len(suggestions) == 0:
            return ""
        return " ".join(suggestions[:num_sug])+"\n"



"""
def main():
"""
    #Creates a weighted bigram dictionary to be used when predicting the most likely word
"""
    filepath = '/Users/mhwessel3/Desktop/WordPrediction/data/w2_.txt'  
    d = defaultdict(dict)
    with open(filepath) as fp:
        for _, line in enumerate(fp):
            freq, prior, curr = line.rstrip().split('\t')
            if prior not in d:
                d[prior] = defaultdict(int)
            d[prior][curr] = freq

    while True:
        print("Prev Word?")
        prev = raw_input()
        if prev not in d:
            print("Try again, word not in dictionary")
            continue
        print("Second Word?")
        curr = raw_input()
        if curr not in d[prev]:
            print("Try again, word not in dictionary")
            continue
        print(prev, curr, d[prev][curr])
            
            

if __name__ == '__main__':
    main()
"""