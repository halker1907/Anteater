import keyboard
import os
import random

COLS = 25
ROWS = 10
EMPTY = '☐'
PLAYER = 'P'
ANT = 'a'
ANTHILL = 'A'
UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'
ANTHILL_MAX = 4
ANTHILL_MINI = 1

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
    def __init__(self, y, x, image):
        self.y = y
        self.x = x
        self.image = image

    def move(self, direction, field):
        new_y, new_x = self.y, self.x

        if direction == UP and self.y > 0 and not isinstance(field.cells[self.y - 1][self.x].content, Anthill):
            new_y -= 1
        elif direction == DOWN and self.y < field.rows - 1 and not isinstance(field.cells[self.y + 1][self.x].content, Anthill):
            new_y += 1
        elif direction == LEFT and self.x > 0 and not isinstance(field.cells[self.y][self.x - 1].content, Anthill):
            new_x -= 1
        elif direction == RIGHT and self.x < field.cols - 1 and not isinstance(field.cells[self.y][self.x + 1].content, Anthill):
            new_x += 1

        field.cells[self.y][self.x].content = None
        self.y, self.x = new_y, new_x
        field.cells[self.y][self.x].content = self

    def place(self, field):
        if field.cells[self.y][self.x].content is None:
            field.cells[self.y][self.x].content = self
        else:
            empty_cells = [(i, j) for i in range(field.rows) for j in range(field.cols) if field.cells[i][j].content is None]
            if empty_cells:
                new_y, new_x = random.choice(empty_cells)
                field.cells[new_y][new_x].content = self
                self.y, self.x = new_y, new_x

    def draw(self, field):
        field.cells[self.y][self.x].content = self

class Player(GameObject):
    ''' игрок '''

    def __init__(self, y=None, x=None):
        super().__init__(y, x, PLAYER)

    def move(self, direction, field):
        super().move(direction, field)


class Anthill(GameObject):
    def __init__(self, x, y, quantity):
        super().__init__(y, x, ANTHILL)
        self.quantity = quantity

    def place(self, field):
        super().place(field)

    def draw(self, field):
        super().draw(field)


class Field:
    def __init__(self, player=Player):
        self.rows = ROWS
        self.cols = COLS
        self.cells = self.make_cells()
        self.player_y = self.rows // 2
        self.player_x = self.cols // 2
        self.player = player(self.player_y, self.player_x)
        self.cells[self.player_y][self.player_x].content = self.player

    def draw_cells(self):
        """выводит игровое поле на экран"""

        for row in self.cells:
            for cell in row:
                cell.draw()
            print()
            
    
    def make_cells(self, cell=Cell):
        cells = [[cell(Y=y, X=x) for x in range(COLS)] for y in range(ROWS)]
        return cells
    
    def spawn_anthills(self):
            available_cells = [(x, y) for x in range(self.cols) for y in range(self.rows) if (x, y) != (self.player.x, self.player.y)]

            quantity = random.randint(ANTHILL_MINI, ANTHILL_MAX)
            
            for i in range(quantity):
                if not available_cells:
                    break
                anthill_x, anthill_y = random.choice(available_cells)
                available_cells.remove((anthill_x, anthill_y))

                anthill = Anthill(x=anthill_x, y=anthill_y, quantity=random.randint(ANTHILL_MINI, ANTHILL_MAX))
                self.add_anthill(anthill)

    def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
    def move_player(self):
        ''' перемещает игрока по полю '''
        key = keyboard.read_event()
        if key.event_type == keyboard.KEY_DOWN:
            if key.name == 'right':
                self.player_y += 1

        if key.event_type == keyboard.KEY_DOWN:
            if key.name == 'down':
                self.player_x += 1
        if key.event_type == keyboard.KEY_DOWN:
            if key.name == 'up':
                self.player_x -= 1

        if key.event_type == keyboard.KEY_DOWN:
            if key.name == 'left':
                self.player_y -= 1
        
    def update_game_state(self):
        clear_screen()
        self.field.drawrows()

class Game:
    '''  '''
    def run(self):
        self.Field.draw_cells()

        while True:
            event = keyboard.read_event(suppress=True)
            if self.handle_keyboard_event(event):
                break
            self.update_game_state()
            
Game()
