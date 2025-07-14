from logic import Game

g = Game()
g.mat = [[4,32,16,4],
         [128,8,4,2],
         [16,4,2,4],
         [8,2,4,2]]
g.print_board()
print(g.is_game_over())
g.print_board()