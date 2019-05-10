import pygtrie as trie


t = trie.CharTrie()

with open("words.txt", "r") as f:
    for _, word in enumerate(f):
        t[word[:-1].lower()] = True

print("Please enter a prefix!")
while True:
    text = raw_input()
    try:
        print(t.keys(text))
    except:
        print("That prefix don't exist fool")



"""print("Hello")

import sys
import time
counter = 0
while True:
    counter +=1
    print("Counter is " + str(counter))
    
    time.sleep(0.5)
    text = input()
    print(text)
    sys.stdout.write("\033[K" * 3) # Cursor up one line"""