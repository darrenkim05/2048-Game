import random

def start_game():
    # Empy list, then append 4 list each with 4 elements as 0

    mat =[[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
   
        
    
    # Generate 2 numbers (2,4 or 2,2)
    x, y = random.choice([(2,2), (2,4), (4,2)])

    # place them randomly on the game state
    i = random.randint(0,3)
    j = random.randint(0,3)

    mat[i][j] = x
    i = random.randint(0,3)
    j = random.randint(0,3)
    mat[i][j] = y

    return mat

def up(mat):
    ...
    # check for duplicates in nearest non-zero number 
        # if duplicate, sum the two up and update the top block
    # else, send number to the highest non-zero column 

    for i in range(4).reverse():
        for j in range(4).reverse():
            print(f"column{i}: {mat[j][i]}")

    
    return mat



    

            
def is_zero(match):
    if match == 0:
        return True
    else:
        return False

def print_game_state(match):
    for i in range(4):
        print(match[i])


def main():
    match = start_game()
    up(match)
    print_game_state(match)
            
    inp = input("Move").lower()
   
    
    
    

        
        
            




if __name__ == "__main__":
    main()
    


