import sys

def display_item(item):
    write(item.title + ' - ' + item.description)
    
def write(string):
    sys.stdout.write(string+'\n')
    
def input(prompt="> "):
    return raw_input(prompt)
    
def display_room(room, admin=False):
    write(room.title)
    write('\t' + room.description)
    if room.inventory:
        write('You see:')
        for i in room.inventory:
            write(i.title)
    write("\tExits:")
    exits = room.get_exits()
    if exits:
        for i in exits:
            write("\t\t" + i)
    else:
            write("\t\tNo exits.")
            
            
def display_dungeon(dungeon):
    write(dungeon.title)
    write('\t' + dungeon.description)
    write("Rooms: ")
    display_dungeon_rooms(dungeon)
    
def display_dungeon_rooms(dungeon):
    for r in dungeon.rooms:
        write(str(dungeon.rooms.index(r)+1) + ' - ' + r.title)
        
def menu_edit_dungeon(dungeon):
    pass