import logging

DIRECTIONS = {
    'north' :   'south',
    'south' :   'north',
    'east'  :   'west',
    'west'  :   'east',
    'up'    :   'down',
    'down'  :   'up',
}

DIR_CHOICES = ( 'north',
                'south',
                'east',
                'west',
                'up',
                'down',
                'n',
                'e',
                'w',
                's',
                'u',
                'd')

class Room:
    title = ""
    description = ""
    north = None
    south = None
    east = None
    west = None
    content = []
    trigger = {}
      
    def __init__(self, title='', description=''):
        self.title = title
        self.description = description
   
    def display_room(self, admin=False):
        print self.title
        print '\t', self.description
        print "\tExits: "
        exits = self.get_exits()
        if exits:
            for i in exits:
                print "\t\t", i
        else:
                print "\t\tNo exits."

    def get_exits(self):
        exits = []
        for k in self.exits.keys():
            if self.exits[k]:
                exits.append(k)
        return exits
            
    def edit(self):
        self.title = raw_input("New title (blank for no change): ")
        self.description = raw_input("New description (blank for no change): ")
    
    def do_trigger(self):
        pass
        
    def set_exits(self):
        self.exits = {'north': self.north,
                      'south': self.south,
                      'east': self.east,
                      'west': self.west}
    
    def set_exit(self, direction, room2):
        print 'set_exit called with', self.title, direction, room2.title
        if direction == 'north':
            self.north=room2
            room2.south=self
        if direction == 'south':
            self.south=room2
            room2.north=self
        if direction == 'east':
            self.east=room2
            room2.west=self
        if direction == 'west':
            self.west=room2
            room2.east=self
        self.set_exits()
        room2.set_exits()
                
            
class Dungeon:
    title = ""
    description = ""
    rooms = []
    
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
            print self.rooms.index(r), r.title
            
    def admin_menu(self):
        while 1==1:
            print "What would you like to do?"
            print "Edit [d]ungeon | Edit a [r]oom | D[i]splay dungeon | Add a [c]onnection | [q]uit"
            c = raw_input()[0]
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
                
    def connect_rooms(self):
        pass
            
            
        
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
        new_room = Room(title=title, description=description, exits=exits)
        self.rooms.append(new_room)
            
    def edit_room(self):
        self.list_rooms()
        c = raw_input("Which room? [#] ")
        
class Mob:
    location = Room()
    dungeon = Dungeon()
    title = ""
    description = ""
    
    def __init__(self, location=Room(), dungeon = Dungeon(), title="", description=""):
        self.location=location
        self.dungeon=dungeon
        self.title=title
        self.description=description
        
    
class User(Mob):
    
    def __init__(self, location=Room(), dungeon=Dungeon(), title="", description=""):
        Mob.__init__(self, location=location, title=title, description=description, dungeon=dungeon)
    
    def move(self, direction):
        self.location = self.location.exits[direction]
        self.location.display_room()
        
    def dungeon_walk(self):
        print "Welcome to", self.dungeon.title, "!"
        print self.location.display_room()
        while 1==1:
            c = raw_input("> ")
            if c.__len__() != 0:                
                if c.lower()[0] == 'q':
                    print "Goodbye!"
                    break
                if DIR_CHOICES.__contains__(c.lower()):
                    self.move(c)
                
                



