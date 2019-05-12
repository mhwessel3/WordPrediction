import sys
import curses
import os

from Trie import Trie
from BigramTrainer import BigramTrainer

def arrow_key(key):
    if key == "KEY_UP" or key == "KEY_DOWN":
        return (False, True, False)
    elif key == "KEY_RIGHT":
        return (False, False, True)
    elif key == "KEY_LEFT": 
        return (True, False, False)
    else:
        return (False, False, False)

def start_program(win):
    #t = Trie()
    #t.initTrie()
    d = BigramTrainer()
    d.initBigram()

    win.nodelay(True)
    win.clear()
    win.addstr("word1 word2 word3\n")
    win.addstr("")

    sentence_str = curr_str = suggestions = key = ""
    left = middle = right = False
    while True:
        try:
            key = win.getkey()
            left, middle, right = arrow_key(key)
            if (not right and not left and not middle):
                """
                No words have been selected using the arrow keys
                """
                if key in ('KEY_BACKSPACE', '\b', '\x7f'):
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
            else:
                """
                A word has been selected using the arrow keys
                """
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
            win.clear()
            
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
    Main method. Prints directions and triggers the word prediction program.
    """
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("                          WORD PREDICTOR                         ")
    print("                          --------------                         ")
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
    print("        AS YOU ENTER KEYS, POTENTIAL WORDS WILL POPULATE         ")
    print("        THREE WORD SUGGESTIONS WILL APPEAR                       ")
    print("        TO SELECT THE LEFT WORD, HIT THE LEFT ARROW              ")
    print("        TO SELECT THE MIDDLE WORD, HIT THE UP ARROW              ")
    print("        TO SELECT THE RIGHT WORD, HIT THE RIGHT ARROW            ")
    print("        TO ESCAPE/BEGIN, PRESS <enter>                           ")
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    
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
    main("")