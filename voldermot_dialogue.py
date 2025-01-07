import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 700, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bellatrix Dialogue")

# Load Bellatrix's image and background
background_image = pygame.image.load("first_background.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
bellatrix_image = pygame.image.load("voldermot.png").convert_alpha()
bellatrix_image = pygame.transform.scale(bellatrix_image, (250, 250))  # Increase image size

# Fonts
font = pygame.font.Font("retro_computer.ttf", 25)  # Font for "Back" button
bellatrix_font = pygame.font.Font("harryp__.ttf", 48)  # Larger font size for Bellatrix dialogue

# Dialogue setup
bellatrix_dialogue = "You cannot hide from me,Potter.This is your End"
bellatrix_typed_text = ""
bellatrix_typing_index = 0
bellatrix_typing_speed = 5  # Faster typing effect
frame_count = 0

# Button setup
button_color = (0, 0, 0)  # Black color for button
text_color = (255, 255, 255)  # White color for button text
back_btn_x, back_btn_y, back_btn_w, back_btn_h = 250, 400, 200, 50  # Button position and size

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle Back button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_btn_x <= event.pos[0] <= back_btn_x + back_btn_w and back_btn_y <= event.pos[1] <= back_btn_y + back_btn_h:
                with open('round_3.py') as file:
                        exec(file.read())
                # Here you can call the function to transition to the previous screen or game state

    # Fill screen with background
    screen.blit(background_image, (0, 0))  # Full-screen background

    # Display Bellatrix's image at the center (increased size)
    screen.blit(bellatrix_image, (screen_width // 2 - bellatrix_image.get_width() // 2, 100))

    # Animate Bellatrix dialogue with typewriter effect
    if bellatrix_typing_index < len(bellatrix_dialogue):
        frame_count += 1
        if frame_count % bellatrix_typing_speed == 0:
            bellatrix_typed_text += bellatrix_dialogue[bellatrix_typing_index]
            bellatrix_typing_index += 1

    # Render and display the Bellatrix dialogue text (white and larger font)
    bellatrix_surface = bellatrix_font.render(bellatrix_typed_text, True, pygame.Color('white'))
    screen.blit(bellatrix_surface, (screen_width // 2 - bellatrix_surface.get_width() // 2, 350))

    # Draw Back button on the Bellatrix screen
    pygame.draw.rect(screen, button_color, (back_btn_x, back_btn_y, back_btn_w, back_btn_h))  # Back button
    back_text = font.render("Go", True, text_color)
    screen.blit(back_text, (back_btn_x + (back_btn_w // 2) - (back_text.get_width() // 2), back_btn_y + (back_btn_h // 2) - (back_text.get_height() // 2)))

    pygame.display.flip()

pygame.quit()
sys.exit()
