
"""
Rooms have the following structure:

Title
Description
Exits (dictionary)
"""

"""
TODO: Why is the exit setting acting on all rooms?
"""
DIRECTIONS = {
    'north' :   'south',
    'south' :   'north',
    'east'  :   'west',
    'west'  :   'east',
    'up'    :   'down',
    'down'  :   'up',
}

class Room:
    
    def __init__(self, title='', description=''):
        self.title = title
        self.description = description
        self.exits = {}
        
    def set_exit(self, dir, room2):
        self.exits[dir]=room2
        room2.exits[DIRECTIONS[dir]]=self

    
    def display(self):
        print self.title
        print '\t', self.description
        if self.exits.keys():
            print "\tExits: "
            for i in self.exits.items():
                print "\t\t", i[0], ": ", i[1].title 
        else:
            print "\tNo exits"
            
            
def connect_rooms(r1, dir, r2):
    """
    The lexicon would be 'room two is [direction] of room one.
    """
    print 'I am connecting rooms ', r1.title, 'and ', r2.title
    print r1.title, ' has exits ', r1.exits 
    print r2.title, ' has exits ', r2.exits
    dir = DIRECTIONS[dir]
    print dir
    r2.exits[dir] = r1
    print r2.exits