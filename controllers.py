import curses
import sys

def display_init():
    stdscr = curses.initscr()
    curses.echo()
    stdscr.keypad(1)
    return stdscr

def quit(stdscr):
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()
    
def write(string):
    '''
    Writes a message to stdout, and appends a newline.\n
    Usage: write(string=string)
    '''
    sys.stdout.write(string+'\n')
    
    
def user_screen(screen, title="", subtitle="", main_text="",exits=[], inventory=[], prompt="> ", message=""):
    screen.erase()
    screen.addstr(0,0,title)
    screen.addstr(1,0, subtitle)
    screen.addstr(2,0,main_text)
    if exits:
        screen.addstr(4,0,"Exits:")
        for exit in exits:
            screen.addstr(4+exits.index(exit)+1, 0, exit)
    if inventory:
        screen.addstr(4,20, "You see:")        
        for item in inventory:
            screen.addstr(4+inventory.index(item)+1, 20, item.title)
    screen.addstr(16, 0, message)
    screen.addstr(15,0, prompt)
    c = screen.getstr(15,2)
    screen.refresh()
    return c
    
    
    