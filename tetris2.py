import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración del juego
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
FPS = 30

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Formas de las piezas
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1],
     [1]],
    [[1, 1, 1],
     [0, 0, 1]],
    [[1, 1, 1],
     [0, 1]],
    [[1, 1, 1],
     [1, 0, 0]],
    [[1, 1],
     [1, 1]],
    [[1, 1, 0],
     [0, 1, 1]],
]

# Clase Pieza
class Piece:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.rotation = 0
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

# Inicializar pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_piece(piece):
    shape = piece.shape[piece.rotation]
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                pygame.draw.rect(screen, piece.color, (piece.x + col, piece.y + row, 1, 1))

def main():
    running = True
    current_piece = Piece(random.choice(SHAPES), random.choice([RED, CYAN, MAGENTA, YELLOW, GREEN, BLUE, ORANGE]))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.move_left()
                elif event.key == pygame.K_RIGHT:
                    current_piece.move_right()
                elif event.key == pygame.K_DOWN:
                    current_piece.move_down()
                elif event.key == pygame.K_UP:
                    current_piece.rotate()

        screen.fill(BLACK)
        draw_grid()
        draw_piece(current_piece)

        # Mover la pieza hacia abajo cada cierto tiempo (FPS)
        if pygame.time.get_ticks() % (1000 // FPS) == 0:
            current_piece.move_down()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()

