import random

class RoboticVacuum:
    def __init__(self, grid):
        self.grid = grid  
        self.position = self.find_start_position()
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

    def find_start_position(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0:
                    return (i, j)  
        return (0, 0)
    
    def is_valid_move(self, x, y):
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] != -1
    
    def clean(self):
        while any(1 in row for row in self.grid):  
            x, y = self.position
            if self.grid[x][y] == 1:
                self.grid[x][y] = 0  
                print(f"Cleaned at ({x}, {y})")
            
            possible_moves = [(x + dx, y + dy) for dx, dy in self.moves if self.is_valid_move(x + dx, y + dy)]
            if possible_moves:
                self.position = random.choice(possible_moves)  
            else:
                break  

        print("Cleaning Complete!")

room = [
    [0, 1, 0, -1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [-1, 0, 1, -1, 0]
]

vacuum = RoboticVacuum(room)
vacuum.clean()
