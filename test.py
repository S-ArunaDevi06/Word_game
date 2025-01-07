import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move the Player")

# Set up player
player_color = (255, 0, 0)  # Red
player_width, player_height = 50, 50
player_x, player_y = (screen_width - player_width) // 2, (screen_height - player_height) // 2
player_speed = 5  # Speed of movement

# Game clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move the player
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Ensure player stays within the screen bounds
    player_x = max(0, min(screen_width - player_width, player_x))
    player_y = max(0, min(screen_height - player_height, player_y))

    # Fill the screen with a background color
    screen.fill((0, 0, 128))  # Blue background

    # Draw the player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)  # 60 frames per second
