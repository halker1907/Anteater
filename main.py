import keyboard
import os
import random


COLS = 20
ROWS = 10
EMPTY = '.'
PLAYER = 'P'
ANTHILL = 'A'
ANT = 'a'
UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'
ANTHILL_MAX = '4'
ANTHILL_MIN = '1'

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

class GameObject:
    '''запретить создание экземпляра'''
    def __init__(self, image, Y=None, X=None):
        self.image = image
        self.Y = Y
        self.X = X

class Player(GameObject):
    ''' игрок '''

    def __init__(self, y=None, x=None):
        self.image = PLAYER
        super().__init__(y, x, self.image)

class Anthill(GameObject):
    def __init__(self, y, x, image) -> None:
        self.image = ANTHILL
        super().__init__(y, x, self.image)

class Field:
    def __init__(self, player=Player):
        self.rows = ROWS
        self.cols = COLS
        self.cells = self.make_cells()
        self.player_y = self.rows // 2
        self.player_x = self.cols // 2
        self.player = player(self.player_y, self.player_x)
        self.cells[self.player_y][self.player_x].content = self.player
        self.anthills = self.make_anthills()

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
        event = keyboard.read_event()
        dy = 0
        dx = 0
        old_cell = self.cells[self.player.Y][self.player.X]
        new_cell = self.cells[self.player.Y + dy][self.player.X + dx]
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == UP:
                dy -= 1
            elif event.name == DOWN:
                dy += 1
            elif event.name == RIGHT:
                dx += 1
            elif event.name == LEFT:
                dx -= 1
        if self.player.Y + dy >= 0 and self.player.Y + dy <= self.rows - 1:
            if self.player.X + dy >= 0 and self.player.X + dy <= self.rows - 1:
                new_y = self.player.Y + dy
                new_x = self.player.X + dx
                self.player.X = new_x
                self.player.Y = new_y
                self.cells[new_y][new_x].content = self.player


    def make_anthills(self, anthill=Anthill, Y=None, X=None) -> list:
        anthills = [anthill(random.randint(Y, X))]
        return anthills




class Game:
    ''' пе '''
    game = True
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
