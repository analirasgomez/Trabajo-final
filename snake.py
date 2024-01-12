import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game Configuration
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake Game Class
class SnakeGame:
    def __init__(self):
        # Initialize game parameters
        self.width = WIDTH // GRID_SIZE
        self.height = HEIGHT // GRID_SIZE
        self.snake = [(self.width // 2, self.height // 2)]  # Initial position of the snake
        self.direction = RIGHT
        self.apple = self.spawn_apple()  # Initial position of the apple
        self.apples_eaten = 0
        self.game_over = False

    def spawn_apple(self):
        # Generate a random position for the apple within the game grid
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def move(self):
        if not self.game_over:
            head = self.snake[0]
            new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

            # Check collisions with walls or itself
            if (
                new_head[0] < 0
                or new_head[0] >= self.width
                or new_head[1] < 0
                or new_head[1] >= self.height
                or new_head in self.snake[1:]
            ):
                self.game_over = True
                return

            self.snake.insert(0, new_head)

            # Check if the snake has eaten the apple
            if new_head == self.apple:
                self.apple = self.spawn_apple()
                self.apples_eaten += 1
            else:
                self.snake.pop()

    def reset(self):
        # Reset the game state
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = RIGHT
        self.apple = self.spawn_apple()
        print(f"You have eaten {self.apples_eaten} apples!")
        self.apples_eaten = 0  # Reset the apple counter
        self.game_over = False

    def handle_events(self, events):
        # Handle Pygame events (e.g., key presses)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT
                elif event.key == pygame.K_SPACE and self.game_over:
                    self.reset()

    def draw(self, screen):
        # Draw the snake on the screen
        for segment in self.snake:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw the apple on the screen
        pygame.draw.rect(screen, RED, (self.apple[0] * GRID_SIZE, self.apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Initialize the game
game = SnakeGame()

# Main game loop
while True:
    events = pygame.event.get()
    game.handle_events(events)

    game.move()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the game
    game.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Control the game speed
    clock.tick(FPS)

    # Display the number of apples when the game is over
    if game.game_over:
        print("Press SPACE to play again.")
        pygame.display.update()
        while game.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game.reset()
                        break
