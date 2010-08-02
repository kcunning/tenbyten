import sys
import logging
from views import *
from room import Room
from dungeon import Dungeon
from item import Item
from mob import Mob, User


# Ordinal directions and their opposites
DIRECTIONS = {
    'north' :   'south',
    'south' :   'north',
    'east'  :   'west',
    'west'  :   'east',
    'up'    :   'down',
    'down'  :   'up',
}

# All possible inputs for a direction, and their non-abbreviated counterpart
DIR_CHOICES = { 'north': 'north',
                'south': 'south',
                'east': 'east',
                'west': 'west',
                'up':'up',
                'down':'down',
                'n': 'north',
                'e': 'east',
                'w': 'west',
                's': 'south',
                'u': 'up',
                'd': 'down'}

# All possible actions a user can take, and their non-abbreviated counterpart.                
ACTIONS = {'look': 'look',
           'take': 'take',
           'go': 'go',
           'i': 'print_inventory',
           'l': 'look',
           'inventory': 'print_inventory',
           'take': 'take',
           'drop': 'drop',
           'admin': 'admin',}