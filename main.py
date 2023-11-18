import random

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
    def __init__(self, ROWS=10, COLS=25, player=Player):
        self.rows = ROWS
        self.cols = COLS
        self.cells = self.make_cells()
        self.player = player(Y=random.randint(0, ROWS-1), X=random.randint(0, COLS-1))
        self.cells[self.player.Y][self.player.X].content = self.player

    def draw_cells(self):
        """выводит игровое поле на экран"""
        for row in self.cells:
            for cell in row:
                if cell.content is not None:
                    print(cell.content.image, end=' ')
                else:
                    print(cell.image, end=' ')
            print()
            
    
    def make_cells(self, ROWS=10, COLS=25, cell=Cell):
        cells = [[cell(Y=y, X=x) for x in range(COLS)] for y in range(ROWS)]
        return cells
    

MCs = Field()
MCs.draw_cells()
