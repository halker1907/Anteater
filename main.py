import keyboard
from os import system
from random import randint, sample, choice
from sys import exit


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
ANTHILL_MAX = 4
ANTHILL_MIN = 1
ANTS_PER_ANTHILL_MIN = 1
ANTS_PER_ANTHILL_MAX = 10

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
        self.ants_counter = randint(ANTS_PER_ANTHILL_MIN, ANTS_PER_ANTHILL_MAX)


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
        self.ants = []


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


    def make_anthills(self):
        anthills_ammount = randint(ANTHILL_MIN, ANTHILL_MAX)
        empty_cells = self.get_empty_cells()
        if not empty_cells:
            print('Ошибка! На поле нет свободных клеток!')
            exit()
        if anthills_ammount > len(empty_cells):
            print('Ошибка! На поле нет свободных клеток для всех муравейников!')
            exit()
        anthills_cells = sample(anthills_ammount, empty_cells)
        anthills = []
        for cell in anthills_cells:
            new_anthill = Anthill(cell.y, cell.x)
            cell.content = new_anthill
            anthills.append(new_anthill)
        return anthills

    def get_neighbours(self, y, x):
        neighbours_coords = []
        for row in (-1, 0, 1):
                for col in (-1, 0, 1):
                    if row == 0 and col == 0:
                        continue
                    neighbours_coords.append((anthill.y + row, anthill.x + col))

    def spawn_ants(self):
        """
        выберает пустые клетки поля вокруг муравейника меняет контент одной
        из них Ant()
        уменьшает Anthill.ants_counter на 1
        прекращает спаун при Anthill.ant_counter < 1
        """
        for anthill in self.anthills:
            if not anthill.ants_counter:
                continue
            neighbours_coords = self.get_neighbours
            if not neighbours_coords:
                return
            for y, x in neighbours_coords:
                if  y < 0 and y > self.rows:
                    if x < 0 and x > self.cols:
                        continue
                if self.cells[y][x].content:
                    continue
                ant = Ant(y, x)
                self.cells[y][x].content = ant
                self.ants.append(ant)
                anthill.ants_counter -= 1
                break
    

    def move_ants(self):
        ''' перемещает каждого муравья на 1 клетку '''
        for ant in self.ants:
            neighbourds_coords = self.get_neighbours(ant.y, ant.x)
            if not neighbourds_coords:
                continue
            for y, x in neighbourds_coords:
                if  y < 0 and y > self.rows:
                    if x < 0 and x > self.cols:
                        # +1 в счетчик сбежавших
                        self.ants.remove(ant)
                        self.cells[ant.y][ant.x].content = None
                        break
                    else:
                        new_cell = self.cells[y][x]
                        if new_cell.content:
                            continue
                        self.cells[ant.y][ant.x] = None
                        new_cell.content = ant
                        ant.y = y
                        ant.x = x


class Ant(GameObject):
    def __init__(self, y, x, image) -> None:
        self.image = ANT
        super().__init__(y, x, self.image)
    
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
            self.field.spawn_ants()
            self.MCs.move_player()
            
Game()