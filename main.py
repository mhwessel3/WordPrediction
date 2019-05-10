import sys
import curses
import os

from trie import Trie

def getSuggestions():
    """
    Returns the top three word suggestions that the user may want to type
    """
    return "word1 word2 word3\n"


def start_program(win):

    win.nodelay(True)
    key=""
    win.clear()
    win.addstr("word1 word2 word3\n")
    win.addstr("")

    curr_str = ""
    while True:
        try:
            key = win.getkey()
            if key != "KEY_UP" or key != "KEY_DOWN" or key != "KEY_RIGHT" or key != "KEY_LEFT":
                if key not in ('KEY_BACKSPACE', '\b', '\x7f'):
                    curr_str += key
                else:
                    # backspace
                    if len(curr_str) > 0:
                        curr_str = curr_str[:-1]
            win.clear()

            # call helper function here
            suggestions = getSuggestions()
            win.addstr(suggestions)
            win.addstr(curr_str)
           
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
                                  ,"  ## |   O O. 
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
    #raw_input()
    t = Trie()
    t.initTrie()
    while True:
        prefix = raw_input()
        suggestions = t.getTopSuggestions(prefix)
        print(suggestions)
    #curses.wrapper(trie.initTrie())
    #curses.wrapper(start_program)

if __name__ == "__main__":
    main("heh")