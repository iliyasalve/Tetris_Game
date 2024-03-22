class Position:
    '''
    Used to indicate to a cell that the position on row X and column Y is occupied
    '''

    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column