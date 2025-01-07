import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer for music
pygame.mixer.init()

# Set up screen dimensions
screen_width, screen_height = 700, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Harry Potter with Blurred Background")

# Load the Hogwarts background image
try:
    background_image = pygame.image.load('round_background.jpg')  # Replace with your Hogwarts image file
    character_image = pygame.image.load('harrypotter_background.png')  # Replace with your character image file
except pygame.error as e:
    print("Error loading images:", e)
    pygame.quit()
    sys.exit()

# Check image sizes (for debugging)
print("Background image size:", background_image.get_size())
print("Character image size:", character_image.get_size())

# Scale the background to fit the screen (make sure it fills the entire screen)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Resize the character image (e.g., scale it to 100x150 pixels)
character_image = pygame.transform.scale(character_image, (100, 150))  # Adjust these values as needed
character_rect = character_image.get_rect()  # Get the rectangle around the character image

# Set the character position to the center of the screen
character_rect.center = (screen_width // 2, screen_height // 2)

# Function to darken the character image
def darken_image(image, factor=0.7):
    """
    Darken the image by reducing the brightness of its pixels.
    The factor controls how dark the image will be (0 = fully dark, 1 = no change).
    """
    # Create a new surface to store the darkened image
    darkened_image = image.copy()
    for x in range(darkened_image.get_width()):
        for y in range(darkened_image.get_height()):
            # Get the color of the pixel
            r, g, b, a = darkened_image.get_at((x, y))
            # Darken each color channel by the given factor
            r = int(r * factor)
            g = int(g * factor)
            b = int(b * factor)
            # Set the new pixel color
            darkened_image.set_at((x, y), (r, g, b, a))
    return darkened_image

# Darken the Harry Potter character image
character_image = darken_image(character_image, factor=0.7)  # Adjust the factor to control darkness

# Load and play background music
try:
    pygame.mixer.music.load('harry_potter_music.mp3')  # Replace with your music file
    pygame.mixer.music.play(-1, 0.0)  # Loop the music indefinitely (-1) from the beginning
except pygame.error as e:
    print("Error loading music:", e)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the Hogwarts background image
    screen.blit(background_image, (0, 0))

    # Draw the Harry Potter character image at the center position
    screen.blit(character_image, character_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame and stop the music
pygame.mixer.music.stop()  # Stop the music when quitting
pygame.quit()
