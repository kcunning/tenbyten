from globals import *
from controllers import *

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
        if inventory:
            self.inventory=inventory

        
    def connect_rooms(self, direction, r2):
        '''
        Sets exit to a room, and sets the inverse direction on the destination room.\n
        Usage: room1.connect_rooms(direction, room2)
        '''
        direction = DIR_CHOICES[direction]
        setattr(self, direction, r2)
        setattr(r2, DIRECTIONS[direction], self)
        
    def disconnect_rooms(self, direction):
        '''
        Removes the connection from two rooms.\n
        Usage: room1.disconnect_rooms(self, direction, r2)
        '''
        direction = DIR_CHOICES[direction]
        delattr(getattr(self, direction), DIRECTIONS[direction])
        delattr(self, direction)
        
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
        if self.inventory:
            for item in self.inventory:
                syn = item.title.split()
                syn = syn[syn.__len__()-1]
                items[syn] = item
        return items
    
    def add_item(self, item):
        '''
        Adds an item to the inventory of the room.\n
        Usage: room.add_item(item=Item)
        '''
        if hasattr(self, 'inventory'):
            self.inventory.append(item)
        else:
            self.inventory = [item]