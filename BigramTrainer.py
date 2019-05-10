from collections import defaultdict

def main():
    """
    Creates a weighted bigram dictionary to be used when predicting the most likely word
    """
    filepath = '/Users/mhwessel3/Desktop/WordPrediction/data/w2_.txt'  
    d = defaultdict(lambda: defaultdict(int))
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