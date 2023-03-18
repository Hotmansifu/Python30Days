import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodger")

# Set up the player
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size * 2
player_speed = 5
player_image = pygame.Surface((player_size, player_size))
player_image.fill((255, 0, 0))

# Set up the obstacles
obstacle_size = 50
obstacle_speed = 3
obstacle_image = pygame.Surface((obstacle_size, obstacle_size))
obstacle_image.fill((0, 0, 255))
obstacles = []

def spawn_obstacle():
    """Spawn a new obstacle"""
    obstacle_x = random.randint(0, screen_width - obstacle_size)
    obstacle_y = 0
    obstacles.append((obstacle_x, obstacle_y))

# Set up the clock
clock = pygame.time.Clock()
fps = 60

# Main game loop
game_over = False
score = 0
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # Spawn obstacles
    if random.random() < 0.02:
        spawn_obstacle()

    # Move obstacles
    for i, obstacle in enumerate(obstacles):
        obstacle_x, obstacle_y = obstacle
        obstacle_y += obstacle_speed
        obstacles[i] = (obstacle_x, obstacle_y)

        # Check for collision with player
        if (obstacle_x < player_x + player_size and obstacle_x + obstacle_size > player_x
                and obstacle_y < player_y + player_size and obstacle_y + obstacle_size > player_y):
            game_over = True

        # Remove obstacles that are off the screen
        if obstacle_y > screen_height:
            obstacles.pop(i)
            score += 1

    # Draw everything on the screen
    screen.fill((255, 255, 255))
    screen.blit(player_image, (player_x, player_y))
    for obstacle in obstacles:
        obstacle_x, obstacle_y = obstacle
        screen.blit(obstacle_image, (obstacle_x, obstacle_y))
    pygame.display.update()

    # Wait for the next frame
    clock.tick(fps)

# Clean up
pygame.quit()

# Print the score
print("Your score was:", score)
