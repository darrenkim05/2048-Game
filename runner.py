import pygame
import logic as game
import sys

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TILE_COLOR = (200, 200, 200)
FONT_COLOR = (50, 50, 50)
BACKGROUND_COLOR = (250, 248, 239)
GRID_COLOR = (187, 173, 160)

# Constants
WIDTH, HEIGHT = 400, 500
TILE_SIZE = 100
FONT_SIZE = 32
SCORE_HEIGHT = 100

# Setup
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048.")
font = pygame.font.SysFont("Arial", FONT_SIZE)
clock = pygame.time.Clock()

g = game.Game()
g.start_game()

def draw_board():
    window.fill(BACKGROUND_COLOR)
    
    score_text = font.render(f"Score: {g.score}", True, BLACK)
    window.blit(score_text, (10,10))
    control_text = font.render("Use Arrow Keys to Play", True, BLACK)
    window.blit(control_text, (10,40))
    
    grid_width = 4 * TILE_SIZE
    x_offset = (WIDTH - grid_width) // 2
    for i in range(4):
        for j in range(4):
            value = g.mat[i][j]
            x = j * TILE_SIZE + x_offset
            y = i * TILE_SIZE + SCORE_HEIGHT
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(window, TILE_COLOR, rect)
            pygame.draw.rect(window, GRID_COLOR, rect, 4)
            if value != 0:
                text = font.render(str(value), True, FONT_COLOR)
                text_rect = text.get_rect(center=rect.center)
                window.blit(text, text_rect)
    pygame.display.update()

running = True
game_over = False

while running:
    draw_board()

    if g.is_game_over():
        game_over = True
        text = font.render("Game Over!", True, (255, 0, 0))
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(text, rect)
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_over:
            board_before = g.get_board_copy()
            if event.key == pygame.K_UP:
                g.move("w")
            elif event.key == pygame.K_DOWN:
                g.move("s")
            elif event.key == pygame.K_LEFT:
                g.move("a")
            elif event.key == pygame.K_RIGHT:
                g.move("d")
            if g.mat != board_before:
                g.add_blocks()

    clock.tick(10)