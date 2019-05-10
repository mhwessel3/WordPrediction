import sys
import curses
import os

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
           curr_str += key
           win.clear()

           # call helper function here
           suggestions = getSuggestions()
           win.addstr(suggestions)
           win.addstr(curr_str)
           
           if key == os.linesep:
              break
        except Exception as e:
           # No input
           pass
    


def getSuggestions():
    """
    Returns the top three word suggestions that the user may want to type
    """
    return "word1 word2 word3\n"

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
                                  ,"  ## |   ಠ ಠ. 
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
    input()
    curses.wrapper(start_program)

if __name__ == "__main__":
    main("heh")