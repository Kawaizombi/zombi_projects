import random

__author__ = 'Андрей'


class BattleField():
    def __init__(self, width, height, difficulty):
        self.width = width
        self.height = height
        self.field = self.generate_field()
        self.difficulty = difficulty

    def generate_field(self):
        field = [['.' for i in range (self.width)] for j in range(self.height)]
        return field

    def put_mine(self, x, y):
        self.field[y][x] = '*'

    def create_mines(self):
        for m in range(40):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            self.put_mine(x, y)

    def on_click(self, x, y):
        if self.field[y][x] == '*':
            self.game_over = True
            self.field[y][x] = 'X'
            return '*'
#        else:
#            self.field[y][x] = self.count_mines_around(x, y)

    def _neighbour_cells(self, x, y):
        min_x = x-1 if x > 0 else x
        max_x = x+1 if x < self.width-1 else x
        min_y = y-1 if y > 0 else y
        max_y = y+1 if y < self.height-1 else y

        for i in range(min_x, max_x+1):
            for j in range(min_y, max_y+1):
                yield (i, j,)

    def count_mines_around(self):
        for j in range(0, self.width):
            for i in range(0, self.height):
                if self.field[i][j] == '.':

                    # how_many_mines = len(filter(self._neighbour_cells(i, j), lambda x, y: self.field[y][x] == '*'))
                    how_many_mines = 0
                    for y, x in self._neighbour_cells(i, j):
                        if self.field[y][x] == '*':
                            how_many_mines += 1
                    if how_many_mines > 0:
                        self.field[i][j] = how_many_mines

        print('Generating and checking mines numbers complete...')
        # return how_many_mines


if __name__ == '__main__':
    field = BattleField(10,10,'hard')
    field.create_mines()
    field.count_mines_around()
    print (field.field)


