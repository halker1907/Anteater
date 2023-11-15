class Cell:
    '''клетка игрового поля'''
    def __init__(self, image='.', Y=None, X=None):
        self.image = image
        self.Y = Y
        self.X = X
        self.content = None

class Player:
    ''' игрок '''
    def __init__(self, image='p', Y=None, X=None):
        self.image = image
        self.Y = Y
        self.X = X

class Field:
    def __init__(self, ROWS=10, COLS=25, cell=Cell, palyer=Player):
        self.rows = ROWS
        self.cols = COLS
        self.cells = self.make_cells()
        self.player = Player()

    def draw_cells(self):
        """выводит игровое поле на экран"""
        #TODO вывести игрока на поле
        for row in self.cells:
            for col in row:
                print(col.image, end='')
            print()
            '''
        for row in self.player:
            for gr in row:
                print(gr.image)
            print()
            '''
    
    def make_cells(self, ROWS=10, COLS=25, cell=Cell):
        cells = [[cell(Y=y, X=x) for x in range(COLS)] for y in range(ROWS)]
        return cells
    

MCs = Field()
MCs.draw_cells()
