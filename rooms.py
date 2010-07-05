
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
    
    def __init__(self, title='', description='', exits={}):
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
            
class Dungeon:
    
    def __init__(self, title='', description='', rooms = []):
        self.title = title
        self.description = description
        self.rooms = rooms
        
    def display(self):
        print self.title
        print '\t', self.description
        print "Rooms: "
        self.list_rooms()
    
    def list_rooms(self):
        for r in self.rooms:
            print r.title
            
    def menu(self):
        while 1==1:
            print "What would you like to do?"
            print "Edit [d]ungeon | Edit a [r]oom | D[i]splay dungeon | [q]uit"
            c = raw_input()[0]
            if c.lower() == 'd':
                self.update()
            if c.lower() == 'r':
                self.rooms_menu()
            if c.lower() == 'i':
                self.display()
            if c.lower() == 'q':
                break
    
    def update(self):
        title = raw_input("New title (blank for no change): ")
        description = raw_input("New description (blank for no change): ")
        if title:
            self.title = title
        if description:
            self.description = description
        
    def rooms_menu(self):
        while 1==1:
            c = raw_input("Create a [n]ew room | [E]dit a room | [D]elete a room | Go [b]ack ")[0]
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
        title = raw_input("Title: ")
        description = raw_input("Description: ")
        while 1==1:
            c = raw_input("Do you want to add an exit? [y/n] ")[0]
            exits = {}
            if c.lower() == 'y':
                while c.lower() == 'y':
                    dir = raw_input("Direction: [north/south/east/west/up/down] ")
                    print "Which room?"
                    for r in self.rooms:
                        print self.rooms.index(r), r.title 
                    e = raw_input("Room #: ")
                    exits[dir] = self.rooms[int(e)]
                    c = raw_input("Would you like to add another exit? [y/n] ")
                break 
            if c.lower() == 'n':
                break
        new_room = Room(title=title, description=description)
        self.rooms.append(new_room)
        for i in exits:
            self.rooms[self.rooms.index(new_room)].set_exit(i,exits[i])
            
        
            

