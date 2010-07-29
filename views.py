import sys

def display_item(item):
    '''
    Displays an item.\n
    Usage: display_item(item=Item)
    '''
    write(item.title + ' - ' + item.description)
    
def write(string):
    '''
    Writes a message to stdout, and appends a newline.\n
    Usage: write(string=string)
    '''
    sys.stdout.write(string+'\n')
    
def input(prompt="> "):
    '''
    Gets a value from the user.\n
    Usage: response = input(prompt=string)
    '''
    return raw_input(prompt)
    
def display_room(room, admin=False):
    '''
    Displays a room and its attributes.\n
    Usage: display_room(room=Room, admin=Boolean)\n
    TODO: implement admin (displays title of connecting room, hidden items)
    '''
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
            if not admin:
                write("\t\t" + i)
            else:
                write("\t\t" + i + " - " + room.title)
    else:
            write("\t\tNo exits.")
            
            
def display_dungeon(dungeon):
    '''
    Displays a dungeon's attributes.\n
    Usage: display_dungeon(dungeon=Dungeon)
    '''
    write(dungeon.title)
    write('\t' + dungeon.description)
    write("Rooms: ")
    display_dungeon_rooms(dungeon)
    
def display_dungeon_rooms(dungeon):
    '''
    Displays all of the rooms in the dungeon.\n
    Usage: display_dungeon_rooms(dungeon=Dungeon)
    '''
    for r in dungeon.rooms:
        write(str(dungeon.rooms.index(r)+1) + ' - ' + r.title)
        
def menu_edit_dungeon(dungeon):
    write("Editing " + dungeon.title)
    while 1==1:
        c = input("Edit: [R]ooms, [D]ungeon, [C]onnections or [Q]uit: ")[0]
        if c.lower() == 'r':
            while 1==1:
                choice = input("[A]dd a room, [E]dit a room, [D]elete a room, or go [B]ack to the previous menu: ")[0]
                if choice.lower() == 'a':
                    title = input("Title for room: ")
                    description = input("Description for room: ")
                    dungeon.add_room(title=title, description=description)
                    write("Room added!")
                if choice.lower() == 'e':
                    display_dungeon_rooms(dungeon)
                    choice = input("Which room do you want to change (#): ")
                    if int(choice) < 0 or int(choice) > dungeon.rooms.__len__():
                        write(choice + " is not a valid option.")
                        break
                    else:
                        title = input("New title (blank for no change): ")
                        description = input("New description (blank for no change): ")
                        dungeon.rooms[int(choice)-1].edit(title=title, description=description)
                        write("Room updated!")
                        display_room(dungeon.rooms[ing(choice)-1])
                if choice.lower() == 'd':
                    display_dungeon_rooms(dungeon)
                    choice = input("Which room do you want to delete (#):")
                    if int(choice) < 0 or int(choice) > dungeon.rooms.__len__():
                        write(choice + " is not a valid option.")
                        break
                    else:
                        dungeon.delete_room(dungeon.rooms[int(choice)-1])
                        write("Room deleted.")
                if choice.lower() == 'b':
                    break

            
        if c.lower() == 'd':
            title = input("New title (blank for no change): ")
            description = input("New description (blank for no change): ")
            dungeon.edit(title, description)
            display_dungeon(dungeon)
        if c.lower() == 'c':
            while 1==1:
                for room in dungeon.rooms:
                    write(str(dungeon.rooms.index(room)+1) + " - " + room.title)
                    exits = room.get_exits()
                    for exit in exits:
                        write("\t" + exit + " - " + getattr(room, exit).title)
                choice = input("[A]dd a connection, [R]emove a connection: ")[0]
                if choice.lower() == 'a':
                    r1 = int(input("Room 1 #: "))
                    direction = input("Direction [N/S/E/W/U/D]: ")
                    r2 = int(input("Room 2 #: "))
                    dungeon.rooms[r1-1].connect_rooms(direction, dungeon.rooms[r2-1])
                break
                
        if c.lower() == 'q':
            break
        