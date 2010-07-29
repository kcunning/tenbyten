import sys
import logging
from views import *

# Ordinal directions and their opposites
DIRECTIONS = {
    'north' :   'south',
    'south' :   'north',
    'east'  :   'west',
    'west'  :   'east',
    'up'    :   'down',
    'down'  :   'up',
}

# All possible inputs for a direction, and their non-abbreviated counterpart
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

# All possible actions a user can take, and their non-abbreviated counterpart.                
ACTIONS = {'look': 'look',
           'take': 'take',
           'go': 'go',
           'i': 'print_inventory',
           'l': 'look',
           'inventory': 'print_inventory',
           'take': 'take',
           'drop': 'drop',
           'admin': 'admin',}
           

class Room:
    '''
    A room within a dungeon. It may contain objects, and can be connected to other rooms through ordinal directions.\n
    Usage: Room(title=string, description=string, inventory=list of items)
    '''
          
    def __init__(self, title='', description='', inventory=[]):
        '''
        Usage: Room(title=string, description=string, inventory=list of Item objects)
        '''
        self.title = title
        self.description = description
        self.inventory=inventory
        
    def connect_rooms(self, direction, r2):
        '''
        Sets exit to a room, and sets the inverse direction on the destination room.\n
        Usage: room1.connect_rooms(direction, room2)
        '''
        direction = DIR_CHOICES[direction]
        setattr(self, direction, r2)
        setattr(r2, DIRECTIONS[direction], self)

    def get_exits(self):
        '''
        Returns all exits for a room.\n
        Usage: room.get_exits()
        '''
        exits = []
        for dir in DIRECTIONS.keys():
            if hasattr(self, dir):
                exits.append(dir)
        return exits
            
    def edit(self, title=None, description=None):
        '''
        Edits the Room object. Allows for changes to the title or description.
        Usage: room.edit()
        '''
        if title:
            self.title = title
        if description:
            self.description = description
    
    def do_trigger(self):
        '''
        This is not implemented yet.
        '''
        pass
    
    def get_items(self):
        '''
        Returns a dictionary list of all the items in a room. Keys are synonmys, values are objects.\n
        Usage: room.get_items()
        '''
        items = {}
        for item in self.inventory:
            syn = item.title.split()
            syn = syn[syn.__len__()-1]
            items[syn] = item
        return items
            
class Dungeon:
    '''
    A dungeon is a collection of rooms.\n 
    Usage: Dungeon(title=string, description=string, rooms=list of rooms)
    '''
    
    def __init__(self, title='', description='', rooms = []):
        '''
        Usage: Dungeon(title=string, description=string, rooms=list of Rooms)
        '''
        self.title = title
        self.description = description
        self.rooms = rooms
        
    def edit(self, title=None, description=None, rooms=[]):
        '''
        Updates the dungeon. Only populated attributes are updated.\n
        Usage: dungeon.update(title=string, description=string, rooms=list of Rooms)
        '''
        if title:
            self.title = title
        if description:
            self.description = description
        if rooms:
            self.rooms = rooms
            
    def add_room(self, title=None, description=None):
        '''
        Adds a room to the dungeon.\n
        Usage: dungeon.add_room(title=string, description=string)
        '''
        room = Room(title=title, description=description)
        self.rooms.append(room)
        
    def delete_room(self, room):
        '''
        Deletes a room and all its connections from the dungeon.\n
        Usage: dungeon.delete_room(room=Room)
        '''
        for exit in room.get_exits():
            delattr(getattr(room, exit), DIRECTIONS[exit])
        self.rooms.pop(self.rooms.index(room))

            
        
class Mob:
    '''
    A mobile item in a dungeon.\n
    Usage: Mob(title=string, description=string, location=room, dungeon=dungeon)
    '''
    
    def __init__(self, location=Room(), dungeon = Dungeon(), title="", description=""):
        '''
        Usage: Mob(title=string, description=string, location=room, dungeon=dungeon)
        '''
        self.location=location
        self.dungeon=dungeon
        self.title=title
        self.description=description
        
    
class User(Mob):
    '''
    The user's object in a dungeon.\n
    Usage: User(title=string, description=string, inventory=list of items, location=Room, dungeon=Dungeon)
    '''
    
    def __init__(self, location=None, dungeon=None, title="", description="", inventory=[]):
        '''
        Usage: User(title=string, description=string, inventory=list of items, location=Room, dungeon=Dungeon)
        '''
        Mob.__init__(self, location=location, title=title, description=description, dungeon=dungeon)
        self.inventory = inventory
    
    def move(self, direction):
        '''
        Allows user to move throughout the dungeon.\n
        Usage: user.move(direction)
        '''
        exits = self.location.get_exits()
        if direction in exits:
            self.location = getattr(self.location, direction)
        else:
            write("That's not a valid exit.")
        display_room(self.location)
        
    def action(self, action):
        '''
        Parses an action from an action statement. If the user has typed 'go', the user is moved. Otherwise, another action is performed.\n
        Assumption: the first word in the action list is a valid action. Valid actions are the keys of ACTIONS.\n
        Assumption: the value of the action in the ACTIONS dictionary is a valid function on the User object.\n
        Usage: this function should be used with parse_action, as that checks to make sure the action is valid.\n
        user.parse_action(action=string)
        '''
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
        else:
            getattr(self, ACTIONS[action[0]])(action)      
            

    def take(self, action):
        '''
        Moves an object from the current room to the user's inventory. The inventory of the room is checked against the rest of the action, minus the word 'take'\n
        Usage: user.take(action=list of strings)
        '''
        action.pop(action.index('take'))
        items = self.location.get_items()
        for item in action:
            if item in items.keys():
                self.inventory.append(items[item])
                self.location.inventory.pop(self.location.inventory.index(items[item]))
                write("Took " + items[item].title.lower())
                
    def look(self, action):
        '''
        Displays the current location.\n
        Usage: user.look()
        '''
        display_room(self.location)
                
    def get_items(self):
        '''
        Returns a dictionary of items in the user's inventory, with their synonyms as the keys, and the objects as the values.\n
        Usage: user.get_items()
        '''
        items = {}
        for item in self.inventory:
            syn = item.title.split()
            syn = syn[syn.__len__()-1]
            items[syn] = item
        return items
                
    def drop(self, action):
        '''
        Removes an item from the user's inventory and places it in the room's inventory.
        Usage: user.drop(action=list of strings)
        '''
        action.pop(action.index('drop'))
        items = self.get_items()
        for item in action:
            if item in items.keys():
                self.inventory.pop(self.inventory.index(items[item]))
                self.location.inventory.append(items[item])
                write("Dropped " + items[item].title.lower())
        
    def parse_action(self, action):
        '''
        Accepts an action from the user and parses it, determining its validity, then sending it off to either move the user, or have the user perform an action.
        Usage: user.parse_action(action=string)
        '''
        action = action.split()
        if action[0].lower() in ACTIONS.keys():
            self.action(action)
            return
        if action[0].lower() in DIR_CHOICES.keys():
            self.move(DIR_CHOICES[action[0].lower()])
            return
            
    def admin(self, action):
        '''
        Initiates the admin function for the dungeon.\n
        TODO: protect this function\n
        Usage: user.admin(action=anything)
        '''
        menu_edit_dungeon(self.dungeon)
        
    def dungeon_walk(self):
        '''
        Initiates the user's walking through the dungeon. Continues until the user quits.\n
        Usage: user.dungeon_walk()
        '''
        write("Welcome to " +  self.dungeon.title + "!")
        display_room(self.location)
        while 1==1:
            c = input("> ")
            if c.__len__() != 0: 
                self.parse_action(c)
               
                if c.lower()[0] == 'q':
                    write("Goodbye!")
                    break

    def print_inventory(self, action):
        '''
        Displays the users inventory./n
        NOTE: this is the one exception to the user.action method, due to inventory already being a list within the user object./n
        Usage: user.print_inventory(action=list of string)
        '''
        if not self.inventory:
            write('You have nothing in your inventory.')
        else:
            for i in self.inventory:
                write(i.title)
 
class Item:
    '''
    A non-mobile object within a dungeon. \n
    Usage: Item(title=string, description=string, synonmys=list)
    '''    
    
    def __init__(self, title='', description='', synonyms=[]):
        '''
        Usage: Item(title=string, description=string, synonyms=list)
        '''
        # Todo -- have it also grab other synonyms from the item's initial name.
        self.title = title
        self.description = description
        self.synonyms = synonyms    
    
    def display(self):
        '''
        Displays the item's title and description.\n
        Usage: item.display()
        '''
        write(self.title + ' - ' + self.description)
    
    def edit(self, title='', description='', location=None):
        '''
        Edits the attributes of an item. Blank values are not updated.\n
        Usage: item.edit(title=string, description=string, location=Room)
        TODO: not interactive
        '''
        # TODO -- Add location and synonyms
        if not title:
            t = input("New title (return to keep the same): ")
            self.title = t
        if not description:
            d = input("New description (return to keep the same):")
            self.description = d
        
            
        