import pygame
import sys
from PIL import Image, ImageFilter
import subprocess

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer module for sound

# Set up screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spell Bound")

# Load Harry Potter font
try:
    harry_potter_font = pygame.font.Font('HARRYP__.TTF', 20)  
except FileNotFoundError:
    print("Harry Potter font file not found.")
    pygame.quit()
    sys.exit()

# Load and play Harry Potter music
try:
    pygame.mixer.music.load('harry_potter_music.mp3')  
    pygame.mixer.music.play(-1)  
except pygame.error as e:
    print("Error loading music:", e)

# Load background image
try:
    background_image = pygame.image.load('first_background.jpg') 
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))  
except pygame.error as e:
    print("Error loading background image:", e)


def blur_image_with_pillow(pygame_image, radius=1):  
    # Convert the Pygame image to a Pillow Image
    pygame_image_str = pygame.image.tostring(pygame_image, 'RGBA')
    pil_image = Image.frombytes("RGBA", pygame_image.get_size(), pygame_image_str)
    
    # Apply blur using Pillow
    blurred_pil_image = pil_image.filter(ImageFilter.GaussianBlur(radius))
    
    # Convert back to Pygame format
    pygame_blurred_image = pygame.image.fromstring(blurred_pil_image.tobytes(), pygame_image.get_size(), 'RGBA')
    return pygame_blurred_image

# Text and animation variables
text = "Spell Bound"
text_color = (220, 142, 0)  
font_size = 30  
max_font_size = 150  
font_size_increment = 2 

# Define the 'Next' button dimensions and fixed font size for "Next" text
next_button_width, next_button_height = 200, 50
next_button_x = screen_width // 2 - next_button_width // 2
next_button_y = screen_height - 100
next_font_size = 30 

# Game loop
running = True
showing_title_screen = True  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.mixer.music.stop()  

        if event.type == pygame.KEYDOWN:
            # If the user presses Enter or Space, transition to the next screen
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                showing_title_screen = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            # Check if "Next" button is clicked
            if next_button_x <= mx <= next_button_x + next_button_width and next_button_y <= my <= next_button_y + next_button_height:
                showing_title_screen = False

    if showing_title_screen:
        # Apply blur to the background using Pillow with a reduced blur effect
        blurred_background = blur_image_with_pillow(background_image, radius=5) 

        # Title screen animation with zoom-in effect for text
        screen.fill((0, 0, 0))  
        screen.blit(blurred_background, (0, 0))  

        # Zoom-in effect for the "Spell Bound" text (increasing font size)
        if font_size < max_font_size:
            font_size += font_size_increment  

        # Update the font size and render the "Spell Bound" text
        harry_potter_font = pygame.font.Font('HARRYP__.TTF', font_size)
        text_surface = harry_potter_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text_surface, text_rect)

        # Draw the "Next" button with fixed font size (no zoom effect)
        next_font = pygame.font.Font('HARRYP__.TTF', next_font_size)
        pygame.draw.rect(screen, (0, 255, 0), (next_button_x, next_button_y, next_button_width, next_button_height))  
        next_text = next_font.render("Next", True, (255, 255, 255)) 
        screen.blit(next_text, (next_button_x + (next_button_width // 2) - (next_text.get_width() // 2), next_button_y + (next_button_height // 2) - (next_text.get_height() // 2)))

        pygame.display.flip()
        pygame.time.Clock().tick(60)  

    else:
       
        print("Transitioning to next screen...")
        with open('level_dialogue_1.py') as file:
            exec(file.read())
        

pygame.quit()
