class GameBoard:
    def __init__(self, size):
        self.size = size
        self.num_disks = [0] * size
        self.items = [[0] * size for i in range(size)]
        self.points = [0] * 2
        
    def num_free_positions_in_column(self, column):
        # returns the amount of free spots
        return self.size - self.num_disks[column]
        
    def game_over(self): 
        '''
        for collumn number in self.size, making sure that the column is not full
        (ie has atleast one or more empty slot), if any of the collumns have 
        1 or more free spots, game is not over. but if there are no free spots, 
        then the game is over
        '''
        for column in range(self.size):
            if self.num_free_positions_in_column(column) != 0:
                return False
        return True
        
    def display(self):
        #going through the rows
        for row in range(self.size):
            # getting the collumn from 0 to n
            for column in range(self.size):
                #if there is a 0 in that spot, no token there and it is empty
                if self.items[column][row] == 0:
                    print(" ", end=" ")
                # if a one is there, put a 'o' for player 1
                elif self.items[column][row] == 1:
                    print("o", end=" ")
                # if a two is there, put a 'x' for player 2
                elif self.items[column][row] == 2:
                    print("x", end=" ")
            print() # print a line between rows
        # print a row of dashes for between board and collumn numbers
        print("-" * (self.size * 2 - 1) )
        # print the collumn number
        for i in range(0, self.size):
            print(i, end=" ")
        print()
        # printing out the points for each player
        print(f"Points player 1: {self.points[0]}")
        print(f"Points player 2: {self.points[1]}")
    
    
    def num_new_points(self, column, row, player):
        new_points = 0
        
        def count_points(count, points):
            while count >= 4:
                points += 1
                count -= 2
            return points
        
        def horizontal():
            count = 1
            try:
                #check left side
                for col in range(column -1, -1, -1):
                    if self.items[col][row] == player:
                        count += 1
                    else:
                        break
                
                # check right side
                for col in range(column + 1, self.size):
                    if self.items[col][row] == player:
                        count += 1
                    else: break
            except IndexError:
                 pass
            return count
             
        def vertical():
            count = 1
            try:
                for new_row in range(row + 1, self.size):
                    if self.items[column][new_row] == player:
                        count += 1
                    else:
                        break
            except IndexError:
                pass
            return count
             
             
        def diagonals():
            count1, count2 = 1, 1
            try:
                # bottom left to top right
                new_row, new_col = row, column
                while new_row <= self.size and new_col <= self.size:
                    if self.items[new_col][new_row] == player:
                        count1 += 1
                    new_row += 1
                    new_col += 1
                # top left to bottom right
                new_row, new_col = row, column
                while new_row <= self.size and new_col <= self.size:
                    if self.items[new_col][new_row] == player:
                        count1 += 1
                    new_row += 1
                    new_col -= 1
                # bottom right to top left
                new_row, new_col = row, column
                while new_row <= self.size and new_col <= self.size:
                    if self.items[new_col][new_row] == player:
                        count2 += 1
                    new_row -= 1
                    new_col += 1
                # top right to bottom left
                new_row, new_col = row, column
                while new_row <= self.size and new_col <= self.size:
                    if self.items[new_col][new_row] == player:
                        count2 += 1
                    new_row -= 1
                    new_col -= 1
            except IndexError:
                pass
            return count
             
             
        left_to_right_points = horizontal()
        new_points += count_points(left_to_right_points, 0)
        
        top_to_bottom_points = vertical()
        new_points += count_points(top_to_bottom_points, 0)
        
        diagonal_points = diagonals()
        new_points += count_points(diagonal_points, 0)
        
        return new_points
        
    def add(self, column, player):
        # if the column doesnt exist, return false
        if column < 0 or column >= self.size:
            return False
        # if the column is full, return false
        elif self.num_disks[column] >= self.size:
            return False
        else:
            row = self.size - 1 - self.num_disks[column]
            self.items[column][row] = player
            self.num_disks[column] += 1
            self.points[player-1] += self.num_new_points(column, row, player)
            return True
