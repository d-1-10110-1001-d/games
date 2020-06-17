
import random
import time

class Cell:
    
    alive_chance = 10
    cell_alive_symbol = "X"
    cell_dead_symbol = "O"

    def __init__(self):
        if random.randint(1, 100) <= alive_chance:
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
            return cell_alive_symbol
        else:
            return cell_dead_symbol

class Grid:

    grid_width = 10
    grid_height = 10

    def __init__(self):
        self.grid = []
        for i in range(grid_height):
            self.grid.add([])

        for row in self.grid:
            for i in range(grid_width):
                row.add(Cell())

class Game:

    pause_time = 1

    def __init__(self):
        self.__cycles = 0
        self.__grid = Grid()

    def run_game(self):
        while True:
            display_game()
            time.sleep(pause_time)
            cycle()
            self.__cycles += 1

    def display_game(self):
        print("cycles:", self.__cycles)
        for row in self.__grid:
            for cell in row:
                print(cell)
            print()

    def cycle(self):
        new_grid = Grid()
        for row in range(0, Grid.grid_height):
            for col in range(0, Grid.grid_width):
                new_grid.grid[row][col].status = get_updated_cell_status(row, col)

        self.__grid = new_grid


    def get_updated_cell_status(self, row, col): #row and col represent the row index and column index of the cell to be updated
        live_neighbors = 0
        
        if row > 0: # not in top row
            if self.__grid[row-1][col].status == "alive": #check right above
                live_neighbors += 1
            if col > 0: # not in left column
                if self.__grid[row-1][col-1].status == "alive": #check top left 
                    live_neighbors += 1
            if col < Grid.grid_width-1: # not in right column
                if self.__grid[row-1][col+1].status == "alive": #check top right
                    live_neighbors += 1

        if col > 0: # not in left column
            if self.__grid[row][col-1].status == "alive": #check left
                live_neighbors += 1

        if col < Grid.grid_width-1: # not in right column
            if self.__grid[row][col+1].status == "alive": #check right
                live_neighbors += 1

        if row < Grid.grid_height-1: # not in bottom row
            if self.__grid[row+1][col].status == "alive": #check right below
                live_neighbors += 1
            if col > 0: # not in left column
                if self.__grid[row+1][col-1].status == "alive": #check bottom left 
                    live_neighbors += 1
            if col < Grid.grid_width-1: # not in right column
                if self.__grid[row+1][col+1].status == "alive": #check bottom right
                    live_neighbors += 1

        return new_cell_status(self.__grid[row][col].status, live_neighbors)
                
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

if __name__ == "__main__":
    app = Game()
    app.run_game()
