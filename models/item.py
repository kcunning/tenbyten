class Item:
    '''
    A non-mobile object within a dungeon. \n
    Usage: Item(title=string, description=string, synonmys=list)
    '''    
    
    def __init__(self, title='', description='', synonyms=[]):
        '''
        Usage: Item(title=string, description=string, synonyms=list)
        '''
        # Todo -- have it also grab other synonyms from the item's initial name.
        self.title = title
        self.description = description
        self.synonyms = synonyms    
    
    def display(self):
        '''
        Displays the item's title and description.\n
        Usage: item.display()
        '''
        return self.title, self.description
    
    def edit(self, title='', description='', location=None):
        '''
        Edits the attributes of an item. Blank values are not updated.\n
        Usage: item.edit(title=string, description=string, location=Room)
        TODO: not interactive
        '''
        # TODO -- Add location and synonyms
        if not title:
            t = input("New title (return to keep the same): ")
            self.title = t
        if not description:
            d = input("New description (return to keep the same):")
            self.description = d