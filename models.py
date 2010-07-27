import sys
import logging
from views import *

DIRECTIONS = {
    'north' :   'south',
    'south' :   'north',
    'east'  :   'west',
    'west'  :   'east',
    'up'    :   'down',
    'down'  :   'up',
}

DIR_CHOICES = { 'north': 'north',
                'south': 'south',
                'east': 'east',
                'west': 'west',
                'up':'up',
                'down':'down',
                'n': 'north',
                'e': 'east',
                'w': 'west',
                's': 'south',
                'u': 'up',
                'd': 'down'}
                
ACTIONS = {'look': 'look',
           'take': 'take',
           'go': 'go',
           'i': 'inventory',
           'l': 'look',
           'inventory': 'inventory',
           'take': 'take'}
           

class Room:
    title = ""
    description = ""
    content = []
    trigger = {}

      
    def __init__(self, title='', description='', inventory=[]):
        self.title = title
        self.description = description
        self.inventory=inventory
        
    def connect_rooms(self, direction, r2):
        setattr(self, direction, r2)
        setattr(r2, DIRECTIONS[direction], self)

    def get_exits(self):
        exits = []
        for dir in DIRECTIONS.keys():
            if hasattr(self, dir):
                exits.append(dir)
        return exits
    
    def set_exit(self, direction, room2):
        setattr(self, direction, room2)
        setattr(room2, DIRECTIONS[direction], self)
            
    def edit(self):
        title = input("New title (blank for no change): ")
        description = input("New description (blank for no change): ")
    
    def do_trigger(self):
        pass
    
    def get_items(self):
        items = {}
        for i in self.inventory:
            items[i.title] = i
        return items
            
class Dungeon:
    title = ""
    description = ""
    rooms = []
    
    def __init__(self, title='', description='', rooms = []):
        self.title = title
        self.description = description
        self.rooms = rooms
    

            
    def admin_menu(self):
        while 1==1:
            write("What would you like to do?")
            write("Edit [d]ungeon | Edit a [r]oom | D[i]splay dungeon | Add a [c]onnection | [q]uit")
            c = input()[0]
            if c.lower() == 'd':
                self.update()
            if c.lower() == 'r':
                self.rooms_menu()
            if c.lower() == 'i':
                self.display()
            if c.lower() == 'c':
                self.connect_rooms()
            if c.lower() == 'q':
                break
            
    def update(self):
        title = input("New title (blank for no change): ")
        description = input("New description (blank for no change): ")
        if title:
            self.title = title
        if description:
            self.description = description
        
    def rooms_menu(self):
        while 1==1:
            c = input("Create a [n]ew room | [E]dit a room | [D]elete a room | Go [b]ack ")[0]
            if c.lower() == 'n':
                self.new_room()
            if c.lower() == 'e':
                self.edit_room()
            if c.lower() == 'd':
                pass
            if c.lower() == 'b':
                break
            
    def new_room(self):
        """
        Adds a new room, and connects it to other rooms if needed
        """
        title = input("Title: ")
        description = input("Description: ")
        while 1==1:
            c = input("Do you want to add an exit? [y/n] ")[0]
            exits = {}
            if c.lower() == 'y':
                while c.lower() == 'y':
                    dir = input("Direction: [north/south/east/west/up/down] ")
                    write("Which room?")
                    for r in self.rooms:
                        write(self.rooms.index(r) + r.title)
                    e = input("Room #: ")
                    exits[dir] = self.rooms[int(e)]
                    c = input("Would you like to add another exit? [y/n] ")
                break 
            if c.lower() == 'n':
                break
        new_room = Room(title=title, description=description, exits=exits)
        self.rooms.append(new_room)
            
    def edit_room(self):
        self.list_rooms()
        c = input("Which room? [#] ")
        
class Mob:
    location = None
    dungeon = None
    title = None
    description = None
    
    def __init__(self, location=Room(), dungeon = Dungeon(), title="", description=""):
        self.location=location
        self.dungeon=dungeon
        self.title=title
        self.description=description
        
    
class User(Mob):
    inventory = []
    
    def __init__(self, location=Room(), dungeon=Dungeon(), title="", description="", inventory=[]):
        Mob.__init__(self, location=location, title=title, description=description, dungeon=dungeon)
        self.inventory = inventory
    
    def move(self, direction):
        exits = self.location.get_exits()
        if direction in exits:
            self.location = self.location.exits[direction]
        else:
            write("That's not a valid exit.")
        self.location.display_room()
        
    def action(self, action):
        if action[0].lower() == 'go':
            action.pop(action.index('go'))
            dir = None
            for i in action:
                if i in DIR_CHOICES.keys():
                    dir = i
            if dir:
                self.move(DIR_CHOICES[dir.lower()])
            else:
                write("You need to give me a direction if you want to go somewhere.")
                self.location.display_room()
        if ACTIONS[action[0].lower()] == 'inventory':
            self.show_inventory()
        if action[0].lower() == 'take':
            self.add_to_inventory(action)
            

    def add_to_inventory(self, action):
        print 'Trying to take something.'
        items = self.location.get_items()

        
    def parse_action(self, action):
        action = action.split()
        if action[0].lower() in ACTIONS.keys():
            self.action(action)
            return
        if action[0].lower() in DIR_CHOICES.keys():
            self.move(DIR_CHOICES[action[0].lower()])
            return
        
    def dungeon_walk(self):
        write("Welcome to" +  self.dungeon.title + "!")
        display_room(self.location)
        while 1==1:
            c = input("> ")
            if c.__len__() != 0: 
                self.parse_action(c)
               
                if c.lower()[0] == 'q':
                    write("Goodbye!")
                    break

    def show_inventory(self):
        if not self.inventory:
            write('You have nothing in your inventory.')
        else:
            for i in self.inventory:
                write(i.title)
 
class Item:
    title = None
    description = None
    synonyms = []
    
    
    def __init__(self, title='', description='', synonyms=[]):
        # Todo -- have it also grab other synonyms from the item's initial name.
        self.title = title
        self.description = description
        self.synonyms = synonyms
        t = title.split()
        t = t[t.__len__()-1]
        if not t in self.synonyms:
            self.synonyms.append(t)     
    
    def display(self):
        write(self.title + ' - ' + self.description)
    
    def edit(self, title='', description='', location=None):
        # TODO -- Add location and synonyms
        if not title:
            t = input("New title (return to keep the same): ")
            self.title = t
        if not description:
            d = input("New description (return to keep the same):")
            self.description = d
        
            
        