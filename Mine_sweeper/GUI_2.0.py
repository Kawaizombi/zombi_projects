__author__ = 'Андрей'
import tkinter
import mine_sweeper

WIDTH = 100
HEIGHT = 100

class Gui():
    def __init__(self):
        self.width = 9
        self.height = 9
        self.cell_size = 10
        self.master = tkinter.Tk()
        self.master.title('Mine sweeper')
        self.window = tkinter.Canvas(self.master, width=self.width * self.cell_size, height=self.height * self.cell_size)
        self.window.pack()
        self.quit_bottom = tkinter.Button(text = 'Quit', command = self.quit)
        self.quit_bottom.pack(side = 'left')
        self.clone_field()
        self.draw_field()
        self.window.bind("<Button-1>", self.on_left_click)
        self.window.bind("<Button-3>", self.on_right_click)
        print(self.field.field)
        self.master.mainloop()

    def quit(self):
        self.master.destroy()

    def clone_field(self):
        self.field = mine_sweeper.BattleField(self.width, self.height, 'hard')

    def draw_field(self):
        self.window.delete("all")
        for j in range(0, self.field.width):
            for i in range(0, self.field.width):
                rect = [i * self.cell_size, j * self.cell_size, i * self.cell_size + 10, j * self.cell_size + 10]
                if self.field.field[i][j].visibility == False:
                    self.window.create_rectangle(*rect, fill = 'gray')
                if self.field.field[i][j].visibility == False and self.field.field[i][j].flag == True:
                    self.window.create_rectangle(*rect, fill = 'pink')
                if self.field.field[i][j].visibility == True:
                    self.window.create_rectangle(*rect, fill = 'white')
                if self.field.field[i][j].content == 'bomb':
                    self.window.create_rectangle(*rect, fill = 'blue')
                if self.field.field[i][j].content == 'bad_bomb':
                    self.window.create_rectangle(*rect, fill = 'red')

    def _event_to_xy(self, event):
        x = int(self.window.canvasx(event.x) // self.cell_size)
        y = int(self.window.canvasy(event.y) // self.cell_size)
        return x, y

    def on_left_click(self, event):
        x, y = self._event_to_xy(event)
        for j in range(0, self.field.width):
            for i in range(0, self.field.height):
                if self.field.field[i][j].content == 'bomb':
                    if (i, j) == (x, y):
                        self.field.field[i][j].content = 'bad_bomb'
                if self.field.field[i][j].content == 'empty':
                    if (i, j) == (x, y):
                        self.field.field[i][j].visibility = True
                if self.field.field[i][j].flag == True:
                    if (i, j) == (x, y):
                        pass
            self.draw_field()

    def on_right_click(self,event):
        x, y = self._event_to_xy(event)
        cell = self.field.get_at(x, y)
        if not cell.visibility:
            cell.flag = not cell.flag
        self.draw_field()


if __name__ == '__main__':
    app = Gui()

