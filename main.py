import keyboard
import os


COLS = 20
ROWS = 10
EMPTY = '.'
PLAYER = 'P'
ANTHILL = 'A'
ANT = 'a'

class Cell:
    '''клетка игрового поля'''
    def __init__(self, Y=None, X=None):
        self.image = EMPTY
        self.Y = Y
        self.X = X
        self.content = None

    def draw(self):
        if self.content:
            print(self.content.image, end=' ')
        else:
            print(self.image, end=' ')

class Player:
    ''' игрок '''

    def __init__(self, Y=None, X=None):
        self.image = PLAYER
        self.Y = Y
        self.X = X

class Field:
    def __init__(self, player=Player):
        self.rows = ROWS
        self.cols = COLS
        self.cells = self.make_cells()
        player_y = self.rows // 2
        player_x = self.cols // 2
        self.player = player(player_y, player_x)
        self.cells[player_y][player_x].content = self.player

    def draw_cells(self):
        """выводит игровое поле на экран"""

        for row in self.cells:
            for cell in row:
                cell.draw()
            print()
            
    
    def make_cells(self, cell=Cell):
        cells = [[cell(Y=y, X=x) for x in range(COLS)] for y in range(ROWS)]
        return cells
    

    
    def move_player(self):
        ''' перемещает игрока по полю '''
        key = keyboard.read_event()
        if key.event_type == keyboard.KEY_DOWN:
            if key.name == 'right':
                print('право')


        if key.event_type == keyboard.KEY_DOWN:
            if key.name == 'down':
                print('назад')

        if key.event_type == keyboard.KEY_DOWN:
            if key.name == 'up':
                print('вперед')

        if key.event_type == keyboard.KEY_DOWN:
            if key.name == 'left':
                print('лево')

class Game:
    '''  '''
    def __init__(self):
        self.MCs = Field()
        self.is_game = True
        self.run()

    def run(self):
        ''' запускает главный цикл игры '''
        while self.is_game:
            self.MCs.draw_cells()
            self.MCs.move_player()
            
Game()
