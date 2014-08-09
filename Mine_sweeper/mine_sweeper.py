import random
__author__ = 'Андрей'


class BattleField():
    def __init__(self, width, height, difficulty):
        self.width = width
        self.height = height
        self.field = self.generate_field()
        self.difficulty  = difficulty

    def generate_field(self):
        field = [['.' for i in range (self.width)] for j in range(self.height)]
        return field


    def create_mines (self):
        for m in range(40):
            x =  random.randint(0, self.width-1)
            y =  random.randint(0, self.height-1)
            self.field[y][x] = '*'

    def on_click(self, x, y):
        if self.field[y][x] == '*':
            self.game_over = True
            self.field[y][x] = 'X'
            return '*'
#        else:
#            self.field[y][x] = self.count_mines_around(x, y)

    def count_mines_around(self):

        for j in range(0, self.width):
            for i in range(0, self.height):
                if self.field[i][j] == '.':

                    if i < self.width - 1 and j < self.height - 1:
                        how_many_mines = 0

                        if self.field[i+1][j] == '*':
                            how_many_mines += 1
                        if self.field[i+1][j+1] == '*':
                            how_many_mines += 1
                        if self.field[i+1][j-1] == '*':
                            how_many_mines += 1

                        if self.field[i][j-1] == '*':
                            how_many_mines += 1
                        if self.field[i][j+1] == '*':
                            how_many_mines += 1

                        if self.field[i-1][j-1] == '*':
                            how_many_mines += 1
                        if self.field[i-1][j] == '*':
                            how_many_mines += 1
                        if self.field[i-1][j+1] == '*':
                            how_many_mines += 1
                        if how_many_mines >= 1:
                            self.field[i][j] = int(how_many_mines)


                    elif i == self.width-1 and j != self.height-1:
                        how_many_mines = 0

                        if self.field[i][j-1] == '*':
                            how_many_mines += 1

                        if self.field[i-1][j-1] == '*':
                            how_many_mines += 1
                        if self.field[i-1][j] == '*':
                            how_many_mines += 1
                        if self.field[i][j+1] == '*':
                            how_many_mines += 1


                        if how_many_mines >= 1:
                            self.field[i][j] = int(how_many_mines)


                    elif j == self.width-1 and i != self.height-1:
                        how_many_mines = 0

                        if self.field[i+1][j] == '*':
                            how_many_mines += 1

                        if self.field[i+1][j-1] == '*':
                            how_many_mines += 1

                        if self.field[i][j-1] == '*':
                            how_many_mines += 1

                        if self.field[i-1][j-1] == '*':
                            how_many_mines += 1
                        if self.field[i-1][j] == '*':
                            how_many_mines += 1

                        if how_many_mines >= 1:
                            self.field[i][j] = int(how_many_mines)


                    elif i == self.width - 1 and j == self.height - 1:
                        how_many_mines = 0
                        if self.field[i][j-1] == '*':
                            how_many_mines += 1
                        if self.field[i-1][j-1] == '*':
                            how_many_mines += 1
                        if self.field[i-1][j] == '*':
                            how_many_mines += 1
                        if how_many_mines >= 1:
                            self.field[i][j] = int(how_many_mines)

                    else:
                        print ('Mines number error in i = {}, j = {}'.format(i,j))

        print('Generating and checking mines numbers complete')
        return how_many_mines


if __name__ == '__main__':
    field = BattleField(10,10,'hard')
    field.create_mines()
    field.count_mines_around()
    print (field.field)


