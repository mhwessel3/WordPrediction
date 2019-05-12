import pygtrie as trie

class Trie:

    def __init__(self):
        self.trie = trie.CharTrie()

    def initTrie(self):
        with open("data/words.txt", "r") as f:
            for _, word in enumerate(f):
                self.trie[word[:-1].lower()] = True
        print("Trie has been initialized")

    def getTopSuggestions(self, prefix, num_sug=3):
    
        if len(prefix) == 0:
            return " \n"
        suggestions = []

        try:
            suggestions = self.trie.keys(prefix)
        except:
            suggestions = []

        if len(suggestions) > num_sug:
            return " ".join(suggestions[:num_sug])+"\n"
        else:
            return " ".join(suggestions)+"\n"

        return ""