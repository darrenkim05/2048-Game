import random
import copy

class Game:
    def __init__(self):
        self.score = 0
        self.mat = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
        

    def start_game(self):
        self.add_blocks()
    
    def add_blocks(self):
        # spawn
            # Generate 2 numbers (2,4 or 2,2)
        x, y = random.choice([(2,2), (2,4), (4,2)])

        # place them randomly on the game state

        #Find all empty cells:
        empty_blocks =[]
        for row in range(4):
            for column in range(4):
                if self.mat[row][column] == 0:
                    empty_blocks.append(((row, column)))

        try:
            i, j = random.choice(empty_blocks)
        except IndexError:
            return self.mat

        self.mat[i][j] = x

        i, j = random.choice(empty_blocks)
  
        self.mat[i][j] = y

        return self.mat

    def print_board(self):
        print(f"Score: {self.score}")
        for row in self.mat:
            print(" | ".join(f"{num:4}" if num != 0 else "   ." for num in row))
    
    def is_zero(self):
        if self.mat == 0:
            return True
        else:
            return False
    
    def move_up(self):
        # check for duplicates in nearest non-zero number 
        # if duplicate, sum the two up and update the top block
        # else, send number to the highest non-zero column 

        for column in range(4):
           # Find & store each non-zero number
            tmp = []
            for row in range(4):
                if self.mat[row][column] != 0:
                   tmp.append(self.mat[row][column])
            # Merge adjacent equal values

            l = 0
            while l < len(tmp) - 1:
                if tmp[l] == tmp[l+1]:
                    tmp[l] = 2 * tmp[l]
                    self.score += tmp[l]
                    del tmp[l+1]
                    # Don't increment l here because we want to skip the next
                else:
                    l += 1

            # Pad the rest of the column with zeros
            while len(tmp) < 4:
                tmp.append(0)


           # Write results back into mat
            for row in range(4):
                self.mat[row][column] = tmp[row]
        return self.mat

    def move_down(self):
        # check for duplicates in nearest non-zero number 
        # if duplicate, sum the two up and update the top block
        # else, send number to the highest non-zero column 

        for column in range(4):
           # Find & store each non-zero number
            tmp = []
            for row in range(4):
                if self.mat[row][column] != 0:
                   tmp.append(self.mat[row][column])
            # Merge adjacent equal values

            l = 0
            while l < len(tmp) - 1:
                if tmp[l] == tmp[l+1]:
                    tmp[l+1] = 2 * tmp[l]
                    self.score += tmp[l+1]
                    del tmp[l]
                    # Don't increment l here because we want to skip the next
                else:
                    l += 1

            # Pad the rest of the column with zeros
            while len(tmp) < 4:
                tmp.insert(0,0)


           # Write results back into mat
            for row in range(4):
                self.mat[row][column] = tmp[row]
        return self.mat
    
    def move_right(self):
        # check for duplicates in nearest non-zero number 
        # if duplicate, sum the two up and update the top block
        # else, send number to the highest non-zero column 

        for row in range(4):
           # Find & store each non-zero number
            tmp = []
            for column in range(4):
                if self.mat[row][column] != 0:
                   tmp.append(self.mat[row][column])
            # Merge adjacent equal values
            l = 0
            while l < len(tmp) - 1:
                if tmp[l] == tmp[l+1]:
                    tmp[l+1] = 2 * tmp[l]
                    self.score += tmp[l+1]
                    del tmp[l]
                    # Don't increment l here because we want to skip the next
                else:
                    l += 1

            # Pad the rest of the column with zeros
            while len(tmp) < 4:
                tmp.insert(0,0)

           # Write results back into mat
            for column in range(4):
                self.mat[row][column] = tmp[column]
        return self.mat
    
    def move_left(self):
        # check for duplicates in nearest non-zero number 
        # if duplicate, sum the two up and update the top block
        # else, send number to the highest non-zero column 

        for row in range(4):
           # Find & store each non-zero number
            tmp = []
            for column in range(4):
                if self.mat[row][column] != 0:
                   tmp.append(self.mat[row][column])
            # Merge adjacent equal values

            l = 0
            while l < len(tmp) - 1:
                if tmp[l] == tmp[l+1]:
                    tmp[l] = 2 * tmp[l]
                    self.score += tmp[l]
                    del tmp[l+1]
                    # Don't increment l here because we want to skip the next
                else:
                    l += 1

            # Pad the rest of the column with zeros
            while len(tmp) < 4:
                tmp.append(0)


           # Write results back into mat
            for column in range(4):
                self.mat[row][column] = tmp[column]
        return self.mat
    

    def move(self, direction):
        if direction == "w":
            self.move_up()
        elif direction == "s":
            self.move_down()
        elif direction == "a":
            self.move_left()
        elif direction == "d":
            self.move_right()
    


    def is_game_over(self):
        # Loop through wasd and if there is no movement, return True
        for direction in ["w", "s", "a", "d"]:
            temp_game = Game()
            temp_game.mat = self.get_board_copy()
            before_move = copy.deepcopy(temp_game.mat)
            temp_game.move(direction)
            if temp_game.mat != before_move:
                return False #if one of the moves change board
        return True
        

     


    
    def get_board_copy(self):
        return copy.deepcopy(self.mat)

    def play(self):
        self.start_game()

        game = True
        while game:
            if self.is_game_over() == True:
                print(f"Game Over!")
                print(f"Score: {self.score}")
                game = False
            
            self.print_board()
            direction = input("Direction")
            if direction in ["w", "a", "s", "d"]:
                self.move(direction)
                self.add_blocks()
            
        
if __name__ == "__main__":
    game = Game()
    game.play()

   

