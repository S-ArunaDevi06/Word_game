import pygame
import sys
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Voldemort Text Input with Lightning Effect")

# Load Voldemort image
try:
    character_image = pygame.image.load('voldermot.png')  # Replace with your Voldemort image file
except pygame.error as e:
    print("Error loading image:", e)
    pygame.quit()
    sys.exit()

# Scale and position character image
character_image = pygame.transform.scale(character_image, (150, 200))  # Adjust dimensions as needed
character_rect = character_image.get_rect(center=(screen_width // 2, screen_height // 2 - 50))

# Wand position (adjust based on character image)
wand_position = (character_rect.centerx, character_rect.centery - 50)

# Set up font for text input and button
font = pygame.font.Font(None, 32)
input_box = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 100, 200, 32)
button_box = pygame.Rect(screen_width // 2 + 110, screen_height // 2 + 100, 70, 32)

# Colors
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
button_color = pygame.Color('green')
text_color = pygame.Color('black')
active = False
input_text = ''
show_lightning = False
lightning_segments = []

# Function to create lightning segments, with end points constrained to the lower part of the screen
def generate_lightning(start_pos, segments=8, spread=30):
    end_pos = (random.randint(0, screen_width), random.randint(screen_height // 2, screen_height))  # End only in lower half
    points = [start_pos]
    for i in range(1, segments):
        x = start_pos[0] + (end_pos[0] - start_pos[0]) * i / segments + random.randint(-spread, spread)
        y = start_pos[1] + (end_pos[1] - start_pos[1]) * i / segments + random.randint(-spread, spread)
        points.append((x, y))
    points.append(end_pos)
    return points

# Game loop
running = True
lightning_timer = 0  # Timer for lightning display duration
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            
            if button_box.collidepoint(event.pos):
                print(f"User entered: {input_text}")
                input_text = ''
                show_lightning = True
                lightning_segments = generate_lightning(wand_position)
                lightning_timer = 50  # Increased lightning display duration

        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(f"User entered: {input_text}")
                    input_text = ''
                    show_lightning = True
                    lightning_segments = generate_lightning(wand_position)
                    lightning_timer = 50  # Increased lightning display duration
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    # Draw background and character image
    screen.fill((30, 30, 30))
    screen.blit(character_image, character_rect)

    # Draw text box
    txt_surface = font.render(input_text, True, text_color)
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    screen.fill(color_active if active else color_inactive, input_box)
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

    # Draw Enter button
    pygame.draw.rect(screen, button_color, button_box)
    button_text = font.render("Enter", True, text_color)
    screen.blit(button_text, (button_box.x + 10, button_box.y + 5))

    # Lightning effect
    if show_lightning and lightning_timer > 0:
        lightning_color = (255, 255, 200)
        # Draw lightning segments
        for i in range(len(lightning_segments) - 1):
            pygame.draw.line(screen, lightning_color, lightning_segments[i], lightning_segments[i + 1], 2)
        lightning_timer -= 1  # Decrease timer
    else:
        show_lightning = False

    # Update display
    pygame.display.flip()

pygame.quit()
