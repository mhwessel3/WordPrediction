import sys
import curses
import os

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
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("- - - - ENTER YOUR TEXT BELOW, ONE CHARACTER AT A TIME - - - - ")
    print("- - - - - TO ESCAPE THE PROGRAM, TYPE \"CTRL C\" - - - - - - - ")

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
           win.addstr("word1 word2 word3\n")
           win.addstr(curr_str)
           
           if key == os.linesep:
              break
        except Exception as e:
           # No input
           pass
        count += 1    

curses.wrapper(main)