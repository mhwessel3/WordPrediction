import pygtrie as trie

class Trie:

    def __init__(self):
        self.trie = trie.CharTrie()

    def initTrie(self):
        with open("words.txt", "r") as f:
            for _, word in enumerate(f):
                self.trie[word[:-1].lower()] = True
        print("Trie has been initialized")

    def getTopSuggestions(self, prefix, num_sug=3):
        """
        if len(self.trie.keys()) == 0:
            print("Trie needs to be initialized")
            return []
        """
        suggestions = []

        try:
            suggestions = self.trie.keys(prefix)
        except:
            suggestions = []

        if len(suggestions) > num_sug:
            return suggestions[:num_sug]
        else:
            return suggestions

        """
        while True:
            text = raw_input()
            try:
                print(t.keys(text))
            except:
                print("That prefix don't exist fool")
        """