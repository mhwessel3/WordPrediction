import sys
import curses
import os

from Trie import Trie
from BigramTrainer import BigramTrainer
from TrigramTrainer import TrigramTrainer

def arrow_key(key):
    """
    Returns an integer that represents what key was hit
    -1 = no arrow key was hit
    0 = left
    1 = middle (up or down)
    2 = right
    """
    if key == "KEY_UP" or key == "KEY_DOWN":
        return 1
    elif key == "KEY_RIGHT":
        return 2
    elif key == "KEY_LEFT": 
        return 0
    else:
        return -1

def start_program(win):

    #tr = Trie()
    #tr.initTrie()

    d = BigramTrainer()
    d.initBigram()

    t = TrigramTrainer()
    t.initTrigram()


    win.nodelay(True)
    win.clear()
    win.addstr(d.getTopSuggestions(""))

    arrow_val = -1
    sentence_str = curr_str = suggestions = key = ""
    sentence_stack = []
    while True:
        try:
            key = win.getkey()
            arrow_val = arrow_key(str(key))
            if (arrow_val == -1):
                """
                No arrow key has been hit
                """
                if key in ('KEY_BACKSPACE', '\b', '\x7f'):
                    if len(sentence_str) > 0:
                        sentence_str = sentence_str[:-1]
                    if len(curr_str) > 0:
                        curr_str = curr_str[:-1]
                    else:
                        if len(sentence_stack) > 0:
                            curr_str = sentence_stack.pop()
                            t.second_to_last = "" if len(sentence_stack) < 2 else sentence_stack[-2]
                            t.last_word = "" if not sentence_stack else sentence_stack[-1]
                            d.last_word = "" if not sentence_stack else sentence_stack[-1]

                elif key == " ":
                    sentence_stack.append(curr_str)
                    d.learn(curr_str)
                    t.learn(curr_str)
                    t.second_to_last = d.last_word
                    t.last_word = curr_str.lower()
                    d.last_word = curr_str.lower()
                    curr_str = ""
                    sentence_str += key
                elif key == "." or  key == "!" or  key == "?":
                    sentence_stack.append(curr_str)
                    d.learn(curr_str)
                    t.learn(curr_str)
                    t.second_to_last = d.last_word
                    t.last_word = ""
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
                sug_arr = suggestions[:-1].split(" ")
                if len(sug_arr) > arrow_val:
                    while(len(sentence_str) > 0 and sentence_str[len(sentence_str)-1] != " "):
                        sentence_str = sentence_str[:-1]
                    sentence_str += sug_arr[arrow_val]
                    t.second_to_last = d.last_word
                    t.last_word = sug_arr[arrow_val]
                    d.last_word = sug_arr[arrow_val]
                    sentence_stack.append(sug_arr[arrow_val])
                    t.learn(sug_arr[arrow_val])
                    d.learn(sug_arr[arrow_val])
                    sentence_str += " "
                    curr_str = ""
            
            win.clear()
            
            suggestions = t.getTopSuggestions(curr_str.lower())
            if suggestions == "":
                suggestions = d.getTopSuggestions(curr_str.lower())
            if suggestions == "":
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
    
   
    raw_input()
    curses.wrapper(start_program)

if __name__ == "__main__":
    main("")