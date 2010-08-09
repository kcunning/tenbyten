from views import *

def display_init():
    print "Welcome to tenbyten!"

def quit(stdscr=None):
    print "Goodbye!"
    
def write(string):
    '''
    Writes a message to stdout, and appends a newline.\n
    Usage: write(string=string)
    '''
    sys.stdout.write(string+'\n')
    
    
def user_screen(screen=None, title="", subtitle="", main_text="",exits=[], inventory=[], prompt="> ", message=""):
    print message
    print subtitle
    print main_text
    if exits:
        print "Exits:"
        for exit in exits:
            print exit
    if inventory:
        print "You see:"        
        for item in inventory:
            print item.title

    c = raw_input(prompt)
    return c
    
    
def admin_screen(dungeon, screen):
    message = ""
    while 1:
        title = dungeon.title
        main_text = "Edit: [R]ooms, [D]ungeon, [C]onnections, [I]tems, or [Q]uit: "
        c = user_screen(screen=screen, title=title, main_text=main_text, message = message)
        if c.lower()[0] == 'q':
            break
        if c.lower()[0] == 'r':
            menu_room_admin(dungeon, screen)
            message = ""
        if c.lower()[0] == 'c':
            menu_connection_admin(dungeon, screen)
            message = ""
        if c.lower()[0] == 'd':
            message = dungeon_admin(dungeon, screen)
        if c.lower()[0] == 'i':
            menu_items_admin(dungeon, screen)

def dungeon_admin(dungeon, screen):
    title = "Dungeon Admin"
    main_text = "New dungeon title (nothing for no change):"
    new_title = user_screen(screen=screen, title=title, main_text=main_text)
    main_text = "New dungeon description (nothing for no change):"
    new_description = user_screen(screen=screen, title=title, main_text=main_text)
    dungeon.edit(title=new_title, description=new_description)
    message = "Dungeon updated"
    return message

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
            main_text = display_all_rooms(dungeon=dungeon, no_exits=False)
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

def menu_connection_admin(dungeon, screen):
    title = "Connections admin"
    main_text = "[A]dd a connection, [R]emove a connection, go [B]ack to the previous menu: "
    message = ""
    while 1:
        choice = user_screen(title=title, main_text=main_text, message=message, screen=screen)
        if choice.lower() == 'b':
            break
        if choice.lower() == 'a':
            main_text = display_all_rooms(dungeon, no_exits=False)
            main_text += "Room 1 #:"
            r1 = int(user_screen(title=title, main_text=main_text, screen=screen))
            direction = user_screen(title=title, main_text="Direction [N/S/E/W/U/D]: ", screen=screen)
            main_text = display_all_rooms(dungeon, no_exits=False)
            main_text += "Room 2 #:"
            r2 = int(user_screen(title=title, main_text=main_text, screen=screen))
            dungeon.rooms[r1-1].connect_rooms(direction, dungeon.rooms[r2-1])
            message = "Connection added"
        if choice.lower() == 'r':
            main_text = display_all_rooms(dungeon, no_exits=False)
            main_text += "\nWhich room do you want to remove the connection from?"
            r = int(user_screen(title=title, main_text=main_text, screen=screen))-1
            exits = dungeon.rooms[r].get_exits()
            main_text = "Which exit do you want to remove?\n"
            for exit in exits:
                main_text += str(exits.index(exit)+1) + " -  " + exit
            e = int(user_screen(title=title, main_text=main_text, screen=screen))
            dungeon.rooms[r].disconnect_rooms(exits[e-1])
            message = "Connection removed"
        main_text = "[A]dd a connection, [R]emove a connection, go [B]ack to the previous menu: "

def menu_items_admin(dungeon, screen):
    '''
    Allows the user to admin items within the dungeon.\n
    Usage: menu_items_admin(dungeon=Dungeon)
    '''
    items = dungeon.get_all_items()
    keys = items.keys()
    title = "Items admin"
    message = ""
    main_text = "[A]dd an item, [E]dit an item, , [L]ist all items, [D]elete an item, [B]ack to the previous menu: "
    while 1:
        choice = user_screen(title=title, main_text=main_text, message = message, screen=screen)
        if choice.lower()[0] == 'b':
            break
        if choice.lower()[0] == 'a':
            main_text = "Name of item"
            name = user_screen(title=title, main_text=main_text, screen=screen)
            main_text = "Item description"
            description = user_screen(title=title, main_text=main_text, screen=screen)
            containers = dungeon.get_all_containers()
            main_text = "And where should I put it?\n"
            for container in containers:
                main_text += str(containers.index(container) + 1) + " - " + container.title + "\n"
            c = int(user_screen(title=title, main_text=main_text, screen=screen))
            dungeon.add_item(title=name, description=description, location=containers[c-1])
            message = "Item added!"
        if choice.lower()[0] == 'e':
            main_text = display_all_items(dungeon)
            main_text += "Item # to edit:"
            i = int(user_screen(title=title, main_text=main_text, screen=screen))-1
            items = dungeon.get_all_items()
            item = items.keys()[i]
            new_title = user_screen(title=title, main_text="New title (Return for no change)", screen=screen)
            new_description = user_screen(title=title, main_text="New description (Return for no change)", screen=screen)
            containers = dungeon.get_all_containers()
            main_text = ""
            for container in containers:
                main_text += str(containers.index(container) + 1) + " - " + container.title + "\n"
            main_text += "And where should I put it? (Return for no change)"
            c = int(user_screen(title=title, main_text=main_text, screen=screen))-1
            item.edit(title=new_title, description=new_description)
            if c:
                dungeon.rooms[c].add_item(item)
            message = "Item updated."
        if choice.lower()[0] == 'l':
            main_text = display_all_items(dungeon)
            c = user_screen(title=title, main_text=main_text, screen=screen, message="Press enter to go back.")

        main_text = "[A]dd an item, [E]dit an item, , [L]ist all items, [D]elete an item, [B]ack to the previous menu: "
    
