
import random
import time
from tkinter import *


class Cell:
    
    alive_chance = 30
    cell_alive_symbol = "X"
    cell_dead_symbol = "O"

    def __init__(self):
        if random.randint(1, 100) <= Cell.alive_chance:
            self.__status = "alive"
        else:
            self.__status = "dead"
        
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status

    def __str__(self):
        if self.__status == "alive":
            return Cell.cell_alive_symbol
        else:
            return Cell.cell_dead_symbol

class Grid:

    grid_width = 20
    grid_height = 20

    def __init__(self):
        self.grid = []
        for i in range(Grid.grid_height):
            self.grid.append([])

        for row in self.grid:
            for i in range(Grid.grid_width):
                row.append(Cell())

class Game:

    pause_time = 1
    canvas_width = 500
    canvas_height = 500

    def __init__(self):
        self.__cycles = 0
        self.__grid = Grid()
        self.root = Tk()
        self.canvas = Canvas(self.root, width = Game.canvas_width, height = Game.canvas_height)
        self.canvas.grid(row=0, column=0)
        self.cycle_label = Label(self.root, text="cycles: " + str(self.__cycles), padx=5, pady=5)
        self.cycle_label.grid(row=1, column=0)
        

    def update_game(self):

        self.cycle_label.config(text="cycles: " + str(self.__cycles))
        
        for row in range(0, Grid.grid_height):
            for col in range(0, Grid.grid_width):
                
                top_left_x = col*Game.canvas_width/Grid.grid_width
                top_left_y = row*Game.canvas_height/Grid.grid_height
                bottom_right_x = top_left_x + Game.canvas_width/Grid.grid_width
                bottom_right_y = top_left_y + Game.canvas_height/Grid.grid_height
                
                fill_color= "white"

                if self.__grid.grid[row][col].status == "alive":
                    fill_color = "green"

                self.canvas.create_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y, fill=fill_color)

                
    def new_cell_status(self, current_status, live_neighbors):
        if current_status == "alive":
            if live_neighbors == 2 or live_neighbors == 3:
                return "alive"
            else:
                return "dead"
        else:
            if live_neighbors == 3:
                return "alive"
            else:
                return "dead"


    def get_updated_cell_status(self, row, col): #row and col represent the row index and column index of the cell to be updated
        live_neighbors = 0
        
        if row > 0: # not in top row
            if self.__grid.grid[row-1][col].status == "alive": #check right above
                live_neighbors += 1
            if col > 0: # not in left column
                if self.__grid.grid[row-1][col-1].status == "alive": #check top left 
                    live_neighbors += 1
            if col < Grid.grid_width-1: # not in right column
                if self.__grid.grid[row-1][col+1].status == "alive": #check top right
                    live_neighbors += 1

        if col > 0: # not in left column
            if self.__grid.grid[row][col-1].status == "alive": #check left
                live_neighbors += 1

        if col < Grid.grid_width-1: # not in right column
            if self.__grid.grid[row][col+1].status == "alive": #check right
                live_neighbors += 1

        if row < Grid.grid_height-1: # not in bottom row
            if self.__grid.grid[row+1][col].status == "alive": #check right below
                live_neighbors += 1
            if col > 0: # not in left column
                if self.__grid.grid[row+1][col-1].status == "alive": #check bottom left 
                    live_neighbors += 1
            if col < Grid.grid_width-1: # not in right column
                if self.__grid.grid[row+1][col+1].status == "alive": #check bottom right
                    live_neighbors += 1

        return self.new_cell_status(self.__grid.grid[row][col].status, live_neighbors)

    def cycle(self):
        new_grid = Grid()
        for row in range(0, Grid.grid_height):
            for col in range(0, Grid.grid_width):
                new_grid.grid[row][col].status = self.get_updated_cell_status(row, col)

        self.__grid = new_grid

    def press_cycle(self):
            self.update_game()
            self.root.update()
            self.cycle()
            self.__cycles += 1

    def run_game(self, max_cycles):
        while self.__cycles <= max_cycles:
            self.update_game()
            self.root.update()
            time.sleep(Game.pause_time)
            self.cycle()
            self.__cycles += 1

        

        self.canvas.bind("<ButtonPress>", self.press_cycle)
        
        self.root.mainloop()



if __name__ == "__main__":
    game = Game()
    game.run_game(5)
