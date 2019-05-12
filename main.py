import sys
import curses
import os

from Trie import Trie
from BigramTrainer import BigramTrainer

def start_program(win):
    #t = Trie()
    #t.initTrie()
    d = BigramTrainer()
    d.initBigram()

    win.nodelay(True)
    key=""
    win.clear()
    win.addstr("word1 word2 word3\n")
    win.addstr("")

    sentence_str = ""
    curr_str = ""
    suggestions = ""
    left = middle = right = False
    while True:
        try:
            key = win.getkey()
            if key == "KEY_UP" or key == "KEY_DOWN":
                # user has selected the middle word
                middle = True
            elif key == "KEY_RIGHT":
                # user has selected the right word
                right = True
            elif key == "KEY_LEFT":
                # user has selected the left word
                left = True
            elif key in ('KEY_BACKSPACE', '\b', '\x7f'):
                if len(sentence_str) > 0:
                    sentence_str = sentence_str[:-1]
                if len(curr_str) > 0:
                    curr_str = curr_str[:-1]
            elif key == " ":
                d.last_word = curr_str.lower()
                curr_str = ""
                sentence_str += key
            elif key == "." or  key == "!" or  key == "?":
                d.last_word = ""
                curr_str = ""
                sentence_str +=key
            else:
                curr_str += key
                sentence_str += key
            win.clear()

            # get words here
            if (left or middle or right):
                l, m, r = suggestions[:-1].split(" ")
                while(len(sentence_str) > 0 and sentence_str[len(sentence_str)-1] != " "):
                    sentence_str = sentence_str[:-1]
                if left:
                    sentence_str += l
                    d.last_word = l
                elif right:
                    sentence_str += r
                    d.last_word = r
                else:
                    sentence_str += m
                    d.last_word = m
                left = right = middle = False
                sentence_str += " "
                curr_str = ""
            
            suggestions = d.getTopSuggestions(curr_str.lower())
            if suggestions == "":
                """suggestions = t.getTopSuggestions(curr_str.lower())
            if suggestions == "":
                print("oof")"""
                suggestions = curr_str+"\n"
            win.addstr(suggestions)
            win.addstr(sentence_str)
           
            if key == os.linesep:
                curses.endwin()
                break
        except Exception as e:
            # No input
            pass

def main(win):
    """
    Main method. Decodes command-line arguments, and starts the Word Prediction Trainer and/or Tester.
    """
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("- - - - - - - - - - - - WORD PREDICTOR - - - - - - - - - - - - ")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("""\
                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## | --D-D. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /
                    """)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("- - - AS YOU ENTER KEYS, POTENTIAL WORDS WILL POPULATE - - - - ")
    print("- - - - - TO ESCAPE THE PROGRAM, TYPE \"CTRL C\" - - - - - - - ")
    print("- - - - - - - - - PRESS <enter> TO BEGIN - - - - - - - - - - - ")
    
    # START THE PROGRAM
    # t = Trie()
    # t.initTrie()
    # while True:
    #     prefix = raw_input()
    #     suggestions = t.getTopSuggestions(prefix)
    #     print(suggestions)
    #curses.wrapper(trie.initTrie())
    raw_input()
    curses.wrapper(start_program)
    #curses.wrapper(d.getTopSuggestions())

if __name__ == "__main__":
    main("heh")