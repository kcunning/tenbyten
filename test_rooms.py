from models import *
from views import *
from controllers import *
import time

def create_rooms(items):
    r1 = Room(title='Northerly room', description='A cold room!', inventory=items)
    r2 = Room('Southerly room', 'It\'s hot here!')
    r3 = Room('Westerly room', 'This room has a picture window.')
    r1.connect_rooms('south', r2)
    r2.connect_rooms('west', r3)
    return([r1,r2,r3])
    
def create_items():
    i1 = Item(title='A lamp', description='Bright and shiny!', synonyms=['lamp'])
    i2 = Item(title='A bracelet', description='It has a green jewel on it.', synonyms=['bracelet'])
    return [i1, i2]

if __name__ == "__main__":
    items = create_items()
    rooms = create_rooms([items[0]])
    dungeon = Dungeon('Test dungeon', 'A very simple test dungeon', rooms)
    user = User(title='Hero', description='A dashing hero: you!', location=dungeon.rooms[0], dungeon=dungeon, inventory=[items[1]])
    stdscr = display_init()
    message = ""
    while 1:
        title = dungeon.title
        subtitle, description, inventory, exits =  display_room(user.location)
        c = user_screen(title=title, main_text=description, inventory=inventory, exits=exits, message=message, screen=stdscr)
        if c == 'q':
            break
        if c == 'admin':
            admin_screen(dungeon=dungeon, screen=stdscr)
        else:
            message = user.parse_action(c)
    quit(stdscr)
    
    
    
