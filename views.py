import sys
from controllers import *

def display_item(item):
    '''
    Displays an item.\n
    Usage: display_item(item=Item)
    '''
    return (item.title.capitalize(), item.description.capitalize())

    
    
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
    exits = room.get_exits()
    if hasattr(room, 'inventory'):
        inventory = room.inventory
    else:
        inventory = []
    return (room.title, room.description, inventory, exits)
    
            
            
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
        
def menu_room_admin(dungeon, screen):
    message = ""
    while 1:
        title = "Room Admin"
        main_text = "[A]dd a room, [D]elete a room, [L]ist all rooms, [M]odify a room, go [B]ack"
        choice = user_screen(screen=screen, title=title, main_text=main_text, message=message)
        if choice.lower() == 'b':
            break
        if choice.lower() == 'a':
            main_text = "Title for room"
            room_title = user_screen(screen=screen, title=title, main_text=main_text)
            main_text= "Description for room"
            room_description = user_screen(screen=screen, title=title, main_text=main_text)
            dungeon.add_room(title=room_title, description=room_description)
            message = "Room added!"
        if choice.lower() == 'l':
            main_text = "Rooms in " + dungeon.title + ":\n"
            for room in dungeon.rooms:
                main_text = main_text + room.title + ": " + room.description + "\n\tExits:"
                exits = room.get_exits()
                if not exits:
                    main_text = main_text + " No exits"
                for exit in exits:
                    main_text = main_text + " " + exit
                main_text = main_text + "\n"
            choice = user_screen(screen=screen, title=title, main_text=main_text, message = "Enter/Return to go back.")
            message = ""
        if choice.lower() == 'm':
            main_text = "Rooms:\n"
            for room in dungeon.rooms:
                main_text = main_text + str(dungeon.rooms.index(room)+1) + " - " + room.title + "\n"
            r = user_screen(screen=screen, title=title, main_text=main_text, message = "Room #")
            room_title = user_screen(screen=screen, title=title, main_text="Room title (Return to keep title the same):")
            room_description = user_screen(screen=screen, title=title, main_text="Room description (Return to keep title the same):")
            dungeon.rooms[int(r)-1].edit(title=room_title, description=room_description)
            message = "Room updated."
        if choice.lower() == 'd':
            main_text = "Rooms:\n"
            for room in dungeon.rooms:
               main_text = main_text + str(dungeon.rooms.index(room)+1) + " - " + room.title + "\n"
            r = user_screen(screen=screen, title=title, main_text=main_text, message = "Room #")
            dungeon.delete_room(dungeon.rooms[int(r)-1])
            message = "Room deleted."
        
           
'''    
    if choice.lower() == 'd':
        display_dungeon_rooms(dungeon)
        choice = input("Which room do you want to delete (#):")
        if int(choice) < 0 or int(choice) > dungeon.rooms.__len__():
            write(choice + " is not a valid option.")
        else:
            dungeon.delete_room(dungeon.rooms[int(choice)-1])
            write("Room deleted.")
    if choice.lower() == 'b':
        pass
'''

def menu_connection_admin(dungeon):
    while 1==1:
        for room in dungeon.rooms:
            write(str(dungeon.rooms.index(room)+1) + " - " + room.title)
            exits = room.get_exits()
            for exit in exits:
                write("\t" + exit + " - " + getattr(room, exit).title)
                choice = input("[A]dd a connection, [R]emove a connection, go [B]ack to the previous menu: ")[0]
            if choice.lower() == 'a':
                r1 = int(input("Room 1 #: "))
                direction = input("Direction [N/S/E/W/U/D]: ")
                r2 = int(input("Room 2 #: "))
                dungeon.rooms[r1-1].connect_rooms(direction, dungeon.rooms[r2-1])
            if choice.lower() == 'r':
                room = int(input("Which room do you want to remove the connection from (#):"))
                exits = dungeon.rooms[room-1].get_exits()
                for exit in exits:
                    write(str(exits.index(exit)+1) + " - " + exit)
                c = int(input("Which exit (#): "))
                dungeon.rooms[room-1].disconnect_rooms(exits[ch-1])
                write("Rooms disconnected")
            if choice.lower() == 'b':
                break
    
def menu_items_admin(dungeon):
    '''
    Allows the user to admin items within the dungeon.\n
    Usage: menu_items_admin(dungeon=Dungeon)
    '''
    items = dungeon.get_all_items()
    keys = items.keys()
    for item in items.keys():
        write(str(keys.index(item) + 1) + " - " +item.title + " - " + items[item].title)
    choice = input("[A]dd an item, [E]dit an item, [D]elete an item: ")[0]
    if choice.lower() == 'a':
        title = input("Name of item: ")
        description = input("Description of item: ")
        containers = dungeon.get_all_containers()
        for container in containers:
            write(str(containers.index(container) + 1) + " - " + container.title)
        place = int(input("Which container #:"))
        dungeon.add_item(title=title, description=description, location=containers[place-1])
        
    
        
def menu_admin(dungeon, choice=""):
    title = dungeon.title
    description = "Edit: [R]ooms, [D]ungeon, [C]onnections, [I]tems, or [Q]uit: "
    return title, description
        
        
def admin_screen(dungeon, screen):
    while 1:
        title, main_text = menu_admin(dungeon=dungeon)
        c = user_screen(screen=screen, title=title, main_text=main_text)
        if c.lower()[0] == 'q':
            break
        if c.lower()[0] == 'r':
            menu_room_admin(dungeon, screen)
        
        