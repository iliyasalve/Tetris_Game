from block import Block
from position import Position


class LBlock(Block):
    '''
    Initialization of a given figure, as well as listing possible positions 
    of the figure on the playing field
    '''

    def __init__(self, cell_size: int):

        super().__init__(id = 1, cell_size = cell_size)

        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
		}

        self.move(0, 3)


class JBlock(Block):
    '''
    Initialization of a given figure, as well as listing possible positions 
    of the figure on the playing field
    '''
    
    def __init__(self, cell_size: int):

        super().__init__(id = 2, cell_size = cell_size)

        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }

        self.move(0, 3)


class IBlock(Block):
    '''
    Initialization of a given figure, as well as listing possible positions 
    of the figure on the playing field
    '''
    
    def __init__(self, cell_size: int):

        super().__init__(id = 3, cell_size = cell_size)

        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }

        self.move(-1, 3)


class OBlock(Block):
    '''
    Initialization of a given figure, as well as listing possible positions 
    of the figure on the playing field
    '''
    
    def __init__(self, cell_size: int):

        super().__init__(id = 4, cell_size = cell_size)

        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }

        self.move(0, 4)


class SBlock(Block):
    '''
    Initialization of a given figure, as well as listing possible positions 
    of the figure on the playing field
    '''
    
    def __init__(self, cell_size: int):

        super().__init__(id = 5, cell_size = cell_size)

        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }

        self.move(0, 3)


class TBlock(Block):
    '''
    Initialization of a given figure, as well as listing possible positions 
    of the figure on the playing field
    '''
    
    def __init__(self, cell_size: int):

        super().__init__(id = 6, cell_size = cell_size)

        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }

        self.move(0, 3)


class ZBlock(Block):
    '''
    Initialization of a given figure, as well as listing possible positions 
    of the figure on the playing field
    '''
    
    def __init__(self, cell_size: int):

        super().__init__(id = 7, cell_size = cell_size)

        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        
        self.move(0, 3)