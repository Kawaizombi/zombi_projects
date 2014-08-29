__author__ = 'Андрей'
import tkinter
import mine_sweeper

WIDTH = 100
HEIGHT = 100

class Gui():
    def _init_(self):
        self.master = tkinter.Tk()
        self.master.title('Mine sweeper')
        self.w = tkinter.Canvas(self.master, width=WIDTH, height=HEIGHT)
        self.w.pack()
        self.quit_bottom = tkinter.Button(text = 'Quit', command = self.quit)
        self.quit_bottom.pack(side = 'left')
        self.clone_field()
        print(self.clone_field.field)
        self.master.mainloop()

    def quit(self):
        self.master.destroy()

    def clone_field(self):
        self.clone_field = mine_sweeper.BattleField(WIDTH, HEIGHT, 'hard')


if __name__ == '__main__':
    app = Gui()
    app._init_()
