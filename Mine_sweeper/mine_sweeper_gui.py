# -*- coding: utf-8 -*-
import mine_sweeper
import tkinter

__author__ = 'Андрей'
CELL_SIZE = 12
WIDTH = 50
HEIGHT = 50
FIELD_WIDTH = WIDTH
FIELD_HEIGHT = HEIGHT
NUM = [1, 2, 3, 4, 5, 6, 7, 8, 9]
DEBUG = 0
NUMBER_OF_MINES = 40
NUMBER_OF_FLAG = NUMBER_OF_MINES
CHEATS = 0
game_over = False



def restart():
    global game_over, NUMBER_OF_FLAG, NUMBER_OF_FLAG, field
    print('Restarting...')
    field = mine_sweeper.BattleField(FIELD_WIDTH,FIELD_HEIGHT, 'hard')
    field.generate_field()
    field.create_mines()
    field.count_mines_around()
    game_over = False
    NUMBER_OF_MINES = 40
    NUMBER_OF_FLAG = NUMBER_OF_MINES
    draw_on_canvas()



def cheat_win():
    global CHEATS
    for j in range(0, field.width):
        for i in range(0, field.height):
            if field.field[i][j] == '*':
                field.field[i][j] = '+'
    draw_on_canvas()
    CHEATS = 1
    win_check()

def win_check():
    global field, CHEATS, game_over
    win_score = 0
    for j in range(0, field.width):
        for i in range(0, field.height):
            if field.field[i][j] == '+':
                win_score += 1
                if win_score == NUMBER_OF_MINES:
                    game_over = True
    if CHEATS == 0:
        print('You win!')
    elif CHEATS == 1:
        print ('You cheater!')

def debug():
    global DEBUG
    if DEBUG == 0:
        DEBUG = 1
        print('Debug mod on')
    else:
        DEBUG = 0
        print('Debug mod off')
    draw_on_canvas()


def on_right_click(event):
    global field, game_over, NUMBER_OF_FLAG

    if game_over:
        return

    w = event.widget
    x = int(w.canvasx(event.x) // CELL_SIZE)
    y = int(w.canvasy(event.y) // CELL_SIZE)

    for j in range(0, field.width):
        for i in range(0, field.height):
            if field.field[i][j] == '*':
                if (i, j) == (x, y) and NUMBER_OF_FLAG >= 1:
                    field.field[i][j] = '+'
                    #print ('Bomb has been defused! Counter-terrorist win!')
                    NUMBER_OF_FLAG = NUMBER_OF_FLAG - 1
                    break

            if field.field[i][j] == '.' and NUMBER_OF_FLAG >= 1:
                if (i, j) == (x, y):
                    field.field[i][j] = '-'
                    #print ('It is not a mine')
                    NUMBER_OF_FLAG = NUMBER_OF_FLAG - 1
                    break

            if field.field[i][j] == '+':
                if (i, j) == (x, y):
                    field.field[i][j] = '*'
                    #print ('Bomb has not been defused! But Counter-terrorist can win!')
                    NUMBER_OF_FLAG = NUMBER_OF_FLAG + 1

            if field.field[i][j] == '-':
                if (i, j) == (x, y):
                    field.field[i][j] = '.'
                    #print ('☺')
                    NUMBER_OF_FLAG = NUMBER_OF_FLAG + 1

    if NUMBER_OF_FLAG == 0:
        flag_lable.config(text ='We need more flags!',bg = 'black', foreground= 'white' )
    else:
        flag_lable.config(text ='Flags = ' + str(NUMBER_OF_FLAG),bg = 'black', foreground= 'white' )
    draw_on_canvas()



def on_left_click(event):
    global game_over, field, NUM

    if game_over:
        return

    w = event.widget
    x = int(w.canvasx(event.x) // CELL_SIZE)
    y = int(w.canvasy(event.y) // CELL_SIZE)
    #print ("clicked at", event.x, event.y)

    cell = field.on_click(x, y)

    for j in range(0, field.width):
        for i in range(0, field.height):
            if field.field[i][j] == '*':
                if (i, j) == (x, y):
                    #print ('i = {}, y = {}, x = {}, y = {}'.format(i, j, x, y))
                    field.field[i][j] = 'X'
                    print ('Btoooom! Allah akbar! Terrorist win!')
                    lable.config(text ="You lost!", bg = 'black', foreground= 'white' )
                    #game_over = True
                    break

    for j in range(0, field.height):
        for i in range(0, field.width):
            if field.field[i][j] != '*' and field.field[i][j] == '.':
                for n in NUM:
                    if field.field[i][j] == n:
                        field.field[i][j] = str(n) + 'v'
            if field.field[i][j] == '.':
                if field.field[i][j] not in ['*', 'X']:
                    if (i, j) == (x, y):
                        field.field[i][j] = '!'



    for j in range(0, field.width):
        for i in range(0, field.height):
            for n in NUM:
                if field.field[i][j] == n:
                    if (i, j) == (x, y):
                        field.field[i][j] = str(n) + 'v'

    if cell == 'X':
        game_over = True

    lable.config(text ="x = {}, y = {}".format (event.x, event.y), bg = 'black', foreground= 'white' )
    draw_on_canvas()


master = tkinter.Tk()
w = tkinter.Canvas(master, width=WIDTH*CELL_SIZE, height=HEIGHT*CELL_SIZE)
w.pack()
lable = tkinter.Label(master, text="Welcome to Mine sweeper!", bg = 'black', foreground= 'white')
lable.pack()
flag_lable = tkinter.Label(master, text="Flags = " + str(NUMBER_OF_FLAG), bg = 'black', foreground= 'white')
flag_lable.pack()
debug_button = tkinter.Button(master, text = "Debug off/on", command = debug)
debug_button.pack()
cheat_button = tkinter.Button(master, text = "Cheat win", command = cheat_win)
cheat_button.pack()
restart_button = tkinter.Button(master, text = "Restart", command = restart)
restart_button.pack()
w.bind("<Button-1>", on_left_click)
w.bind("<Button-3>", on_right_click)



def print_field(field):
    for i in range(0, field.height):
        for j in range(0, field.width):
            print(field.field[i][j], end=' ')
        print()

def draw_on_canvas():
    global field, DEBUG
    w.delete("all")
    for j in range(0, field.width):
        for i in range(0, field.height):
            #мины не нужно
            if field.field[i][j] == '*':
                w.create_rectangle(i*CELL_SIZE, j*CELL_SIZE, i*CELL_SIZE+10, j*CELL_SIZE+10, fill = 'red')

            #закрытые поля
            if DEBUG == 0:
                w.create_rectangle(i*CELL_SIZE, j*CELL_SIZE, i*CELL_SIZE+10, j*CELL_SIZE+10, fill = 'grey', outline='black')
            elif DEBUG == 1:
                w.create_rectangle(i*CELL_SIZE, j*CELL_SIZE, i*CELL_SIZE+10, j*CELL_SIZE+10, fill = '', outline='green')

            #открытое поле
            if field.field[i][j] == '!':
                w.create_rectangle(i*CELL_SIZE, j*CELL_SIZE, i*CELL_SIZE+10, j*CELL_SIZE+10, fill = 'white', outline='green')

            #взорваная мина
            if field.field[i][j] == 'X':
                w.create_rectangle(i*CELL_SIZE, j*CELL_SIZE, i*CELL_SIZE+10, j*CELL_SIZE+10, fill = 'blue', outline='red')

            #цыфры
            if field.field[i][j] == '1v':
                w.create_text(i*CELL_SIZE + 5, j*CELL_SIZE + 5, text = '1')
            if field.field[i][j] == '2v':
                w.create_text(i*CELL_SIZE + 5, j*CELL_SIZE + 5, text = '2')
            if field.field[i][j] == '3v':
                w.create_text(i*CELL_SIZE + 5, j*CELL_SIZE + 5, text = '3')
            if field.field[i][j] == '4v':
                w.create_text(i*CELL_SIZE + 5, j*CELL_SIZE + 5, text = '4')
            if field.field[i][j] == '5v':
                w.create_text(i*CELL_SIZE + 5, j*CELL_SIZE + 5, text = '5')
            if field.field[i][j] == '6v':
                w.create_text(i*CELL_SIZE + 5, j*CELL_SIZE + 5, text = '6')
            if field.field[i][j] == '7v':
                w.create_text(i*CELL_SIZE + 5, j*CELL_SIZE + 5, text = '7')
            if field.field[i][j] == '8v':
                w.create_text(i*CELL_SIZE + 5, j*CELL_SIZE + 5, text = '8')
            if field.field[i][j] == '9v':
                w.create_text(i*CELL_SIZE + 5, j*CELL_SIZE + 5, text = '9')

            if field.field[i][j] == '+':
                w.create_rectangle(i*CELL_SIZE, j*CELL_SIZE, i*CELL_SIZE+10, j*CELL_SIZE+10, fill = 'green', outline='black')
            if field.field[i][j] == '-':
                w.create_rectangle(i*CELL_SIZE, j*CELL_SIZE, i*CELL_SIZE+10, j*CELL_SIZE+10, fill = 'green', outline='black')

if __name__ == '__main__':
    restart()
    draw_on_canvas()
    #print_field(field)


tkinter.mainloop()
