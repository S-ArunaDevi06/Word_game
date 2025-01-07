import pygame

# Initialize Pygame
pygame.init()

# Set up screen dimensions
screen_width, screen_height = 700, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Harry Potter Background")

# Load the HD Harry Potter background image
image = pygame.image.load('background.jpg')  # Replace with your image file path

def Background_sky(image):
    # Scale the image to fit the screen
    size = pygame.transform.scale(image, (screen_width, screen_height))
    screen.blit(size, (0, 0))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background
    Background_sky(image)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
