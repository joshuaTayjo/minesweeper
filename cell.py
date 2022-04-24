from tkinter import Button
import random
import settings


class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(location, text=f'{self.x} , {self.y}', width=12, height=4)
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-2>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(self.is_mine)
        print('I am left clicked')

    def right_click_actions(self, event):
        print(event)
        print('I am right clicked')

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for cell in picked_cells:
            cell.is_mine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'
