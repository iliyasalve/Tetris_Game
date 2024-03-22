class Colors:
    '''
    List of colors that can be used in the project
    '''

    dark_purple = (37, 22, 39) # cells field

    green = (34, 151, 86) # JBlock
    red = (196, 52, 45)  # LBlock
    orange = (255, 140, 0) # IBlock
    burlywood  = (222, 184, 135) # OBlock
    cyan = (21, 204, 209) # SBlock
    pink = (230, 62, 98) # TBlock
    blue = (34, 79, 183) # ZBlock

    white = (255, 255, 255)

    background_purple = (67, 15, 67) # background
    rec_purple = (128, 0, 128) # rectangle


    @classmethod
    def get_cell_colors(cls):
        '''
        Returns a list of colors to use for figures
        '''
        
        return [cls.dark_purple, cls.green, cls.red, cls.orange, cls.burlywood, cls.cyan, cls.pink, cls.blue]