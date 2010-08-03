from controllers import *
        
class Dungeon:
    '''
    A dungeon is a collection of rooms.\n 
    Usage: Dungeon(title=string, description=string, rooms=list of rooms)
    '''
    
    def __init__(self, title='', description='', rooms = [], users=[]):
        '''
        Usage: Dungeon(title=string, description=string, rooms=list of Rooms)
        '''
        self.title = title
        self.description = description
        self.rooms = rooms
        self.users = users
        
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
            
    def add_item(self, title, description, location):
        '''
        Adds an item to the dungeon. The item can be placed in a room, or on a user.\n
        Usage: dungeon.add_item(title=string, description=string, location=User or Room object)
        '''
        item = Item(title=title, description=description)
        location.add_item(item)
            
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
    
    def get_all_items(self):
        '''
        Returns a dictionary of all items in the dungeon, including items on users. The key is the item, and the value is the location.\n
        Usage: items = dungeon.get_all_items()
        '''
        items = {}
        for room in self.rooms:
            if hasattr(room, 'inventory'):
                for item in room.inventory:
                    items[item] = room
        for user in self.users:
            for item in user.inventory:
                items[item] = user
        return items
        
    def get_all_containers(self):
        '''
        Returns a list of all containers.\n
        Usage: list = dungeon.get_all_containers()
        '''
        containers = []
        for room in self.rooms:
            containers.append(room)
        for user in self.users:
            containers.append(user)
        return containers
