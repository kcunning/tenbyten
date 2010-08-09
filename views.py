import sys

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
    '''    write(dungeon.title)
    write('\t' + dungeon.description)
    write("Rooms: ")
    display_dungeon_rooms(dungeon)
    '''
    pass
    
def display_dungeon_rooms(dungeon):
    '''
    Displays all of the rooms in the dungeon.\n
    Usage: display_dungeon_rooms(dungeon=Dungeon)
    '''
    pass
    '''
    for r in dungeon.rooms:
        write(str(dungeon.rooms.index(r)+1) + ' - ' + r.title)
    '''
     

 
def display_all_rooms(dungeon, no_exits = True):
    main_text = "Rooms in " + dungeon.title + ":\n"
    for room in dungeon.rooms:
        main_text = main_text + str(dungeon.rooms.index(room)+1) + " - " + room.title + ": " + room.description
        if not no_exits:
            main_text += "\n\tExits:"
            exits = room.get_exits()
            if not exits:
                main_text += " No exits"
            for exit in exits:
                main_text += " " + exit
        main_text += "\n"
    return main_text


    

    
def display_all_items(dungeon):
    items = dungeon.get_all_items()
    items = items.keys()
    text = "Items:\n"
    for item in items:
        text += str(items.index(item)+1) + " - " + item.title + ": " + item.description +  "\n"
    return text
    


        

        
        
        