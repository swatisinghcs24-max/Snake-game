import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Clock for controlling speed
clock = pygame.time.Clock()
FPS = 10  # Speed of snake

# Font for score
font = pygame.font.SysFont("Arial", 24, bold=True)

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, CELL_SIZE, CELL_SIZE])

def draw_food(food_x, food_y):
    pygame.draw.rect(screen, RED, [food_x, food_y, CELL_SIZE, CELL_SIZE])

def show_score(score):
    value = font.render(f"Score: {score}", True, BLUE)
    screen.blit(value, [10, 10])

def game_loop():
    # Starting position
    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0
    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
    food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE

    score = 0
    game_over = False

    while True:
        while game_over:
            screen.fill(BLACK)
            msg = font.render("Game Over! Press R to Restart or Q to Quit", True, RED)
            screen.blit(msg, [WIDTH // 8, HEIGHT // 3])
            show_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r:
                        game_loop()

        # Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -CELL_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = CELL_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -CELL_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = CELL_SIZE
                    x_change = 0

        # Move snake
        x += x_change
        y += y_change

        # Check boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        # Draw background
        screen.fill(BLACK)

        # Draw food and snake
        draw_food(food_x, food_y)
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for self collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        draw_snake(snake_list)
        show_score(score)
        pygame.display.update()

        # Food eaten
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            snake_length += 1
            score += 10

        # Control speed
        clock.tick(FPS)

# Run the game
game_loop()