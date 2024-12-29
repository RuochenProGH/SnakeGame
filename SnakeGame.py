# Example code for a simple snake game
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

class SnakeGame:
    def __init__(self):
        self.snake = [(100, 100), (80, 100), (60, 100)]  # Initial snake coordinates
        self.direction = "RIGHT"  # Initial direction
        self.food = self._place_food()
        self.score = 0

    def _place_food(self):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, new_direction):
        opposite_directions = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def move(self):
        head_x, head_y = self.snake[0]

        if self.direction == "UP":
            head_y -= CELL_SIZE
        elif self.direction == "DOWN":
            head_y += CELL_SIZE
        elif self.direction == "LEFT":
            head_x -= CELL_SIZE
        elif self.direction == "RIGHT":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        # Check for collisions
        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in self.snake
        ):
            return False  # Game over

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self._place_food()
        else:
            self.snake.pop()

        return True

    def get_state(self):
        return {
            "snake": self.snake,
            "food": self.food,
            "score": self.score
        }

def main():
    game = SnakeGame()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    game.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    game.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    game.change_direction("RIGHT")

        running = game.move()

        # Drawing
        screen.fill(BLACK)
        for segment in game.snake:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, RED, (*game.food, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()


