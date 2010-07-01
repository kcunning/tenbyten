
"""
Rooms have the following structure:

Title
Description
Exits (dictionary)
"""


class Room:
    
    DIRECTIONS = {
        'north' :   'south',
        'south' :   'north',
        'east'  :   'west',
        'west'  :   'east',
        'up'    :   'down',
        'down'  :   'up',
    }
    
    def __init__(self, title='', description='', exits={}):
        self.title = title
        self.description = description
        self.exits = exits
        for d, r in exits.items():
            self.connect_rooms(d, r)
    
    def display(self):
        print self.title
        print self.description
        if self.exits.keys():
            print "Exits: "
            for i in self.exits.keys():
                print i
        else:
            print "No exits"
    
    def update_room(self, title='', description='', exits={}):
        if title:
            self.title = title
        if description:
            self.description = description
        if exits:
            for d, r in exits.items():
                self.connect_rooms(d,r)
    
    def connect_rooms(self, direction, room):
        room.exits[self.DIRECTIONS[direction]] = self