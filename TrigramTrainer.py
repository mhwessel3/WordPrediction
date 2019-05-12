from collections import defaultdict
import string

class TrigramTrainer:
    def __init__(self):
        self.trigram_freqs = defaultdict(dict)
        self.second_to_last = ""
        self.last_word = ""
        self.USER_MULTIPLER = 50

    def initTrigram(self):
        filepath = 'data/w3_.txt'
        with open(filepath) as fp:
            for _, line in enumerate(fp):
                freq, prior, recent_prior, curr = line.rstrip().split('\t')
                freq = int(freq)
                if prior not in self.trigram_freqs:
                    self.trigram_freqs[prior] = defaultdict(dict)
                if recent_prior not in self.trigram_freqs[prior]:
                    self.trigram_freqs[prior][recent_prior] = defaultdict(int)
                self.trigram_freqs[prior][recent_prior][curr] = freq
    
    def getTopSuggestions(self, prefix, num_sug=3):
        if self.second_to_last == "" or self.last_word == "" or self.second_to_last not in self.trigram_freqs or self.last_word not in self.trigram_freqs[self.second_to_last]:
            return ""
        possible_words = sorted(self.trigram_freqs[self.second_to_last][self.last_word], key=self.trigram_freqs[self.second_to_last][self.last_word].get, reverse=True)
        suggestions = [word for word in possible_words if word.startswith(prefix)]
        if len(suggestions) == 0:
            return ""
        return " ".join(suggestions[:num_sug])+"\n"

    def learn(self, word):
        if self.second_to_last != "" and self.last_word != "":
            if self.second_to_last not in self.trigram_freqs:
                self.trigram_freqs[self.second_to_last] = defaultdict(dict)
            if self.last_word not in self.trigram_freqs[self.second_to_last]:
                self.trigram_freqs[self.second_to_last][self.last_word] = defaultdict(int)
            if word not in self.trigram_freqs[self.second_to_last][self.last_word]:
                self.trigram_freqs[self.second_to_last][self.last_word][word] = self.USER_MULTIPLER
            else:
                self.trigram_freqs[self.second_to_last][self.last_word][word] += self.USER_MULTIPLER
