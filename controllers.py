import curses

def display_init():
    stdscr = curses.initscr()
    curses.echo()
    stdscr.keypad(1)
    return stdscr

def quit(stdscr):
    curses.nocbreak(); stdscr.keypad(0); curses.echo()
    curses.endwin()
    
def write(string):
    '''
    Writes a message to stdout, and appends a newline.\n
    Usage: write(string=string)
    '''
    sys.stdout.write(string+'\n')
    
def user_screen(screen, title="", main_text="", prompt="> "):
    screen.erase()
    screen.addstr(0,0,title)
    screen.addstr(2,0,main_text)
    screen.addstr(7,0,prompt)
    c = screen.getstr(7,3)
    screen.refresh()
    
    
    