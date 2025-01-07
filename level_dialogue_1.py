#Import the necessary libraries
import pygame
import sys
import random
from pygame.locals import *




# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen setup
screen_width, screen_height = 700, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spell Bound")

# Load images
try:
    harry_image = pygame.image.load('harry_potter_level.png')  # Replace with the Harry Potter character image
    harry_image = pygame.transform.scale(harry_image, (150, 200))  # Scale if necessary
    bellatrix_image = pygame.image.load('bellatrix.png')  # Bellatrix image
    bellatrix_image = pygame.transform.scale(bellatrix_image, (200, 250))  # Increased Bellatrix image size
    background_image = pygame.image.load('platform_image.jpg')  # Background image
    
    # Scale background image to fit the full screen
    hall_image = pygame.image.load('round_background.jpg')  # Replace with your hall background image
    voldermort_image = pygame.image.load('voldermot.png') 
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))  # Fill screen
except pygame.error as e:
    print("Error loading images:", e)
    pygame.quit()
hall_image = pygame.transform.scale(hall_image, (screen_width, screen_height))
voldermort_image = pygame.transform.scale(voldermort_image, (150, 200))
voldermort_rect = voldermort_image.get_rect(center=(screen_width // 2, screen_height // 2))

# Font and colors
try:
    # Load the Harry Potter font (make sure the font file is in the same directory)
    font = pygame.font.Font('harryp__.ttf', 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    button_color = pygame.Color('green')
    #text_color = pygame.Color('black')  # Adjust the font size as needed
except FileNotFoundError:
    print("Font file not found. Please make sure the Harry Potter font is in the directory.")
    pygame.quit()
    sys.exit()
try:
    pixel_font = pygame.font.Font('pressstart2p.ttf', 16)  # Adjust size as needed
except FileNotFoundError:
    print("Pixel font file not found. Please make sure the font is in the directory.")
    pygame.quit()
    sys.exit()
text_color = pygame.Color('white')
button_color = pygame.Color('green')
bg_color = pygame.Color('black')

# Typewriter effect variables
dialogue = "Welcome to the Wizarding World! Prepare your wand and focus your magic!"
typed_text = ""
typing_index = 0
typing_speed = 5  # Lower value for faster typing effect
frame_count = 0

bellatrix_dialogue = "Defeat the Bellatrix First! To Enter this level"
bellatrix_typed_text = ""
bellatrix_typing_index = 0
bellatrix_typing_speed = 5

# Main menu button setup
btn_w, btn_h = 240, 90
btn_y_positions = [200, 300, 400]

# Back button setup for Bellatrix screen
back_btn_w, back_btn_h = 150, 50
back_btn_x = screen_width // 2 - back_btn_w // 2
back_btn_y = 450  # Position the back button at the bottom of the screen
# Input box and button
input_box = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 100, 200, 32)
button_box = pygame.Rect(screen_width // 2 + 110, screen_height // 2 + 100, 70, 32)
back_button_box = pygame.Rect(10, 10, 70, 32)  # Back button in the top left corner
active = False
input_text = ''
show_lightning = False
lightning_timer = 0

# Main menu button setup
btn_w, btn_h = 240, 90
btn_y_positions = [200, 300, 400]



# Add background music
try:
    pygame.mixer.music.load('harry_potter_music.mp3')  # Replace with the path to your music file
    pygame.mixer.music.play(-1, 0.0)  # Play music in a loop (-1 means infinite loop, 0.0 is the start position)
except pygame.error as e:
    print("Error loading music:", e)
    pygame.quit()
    sys.exit()


def fade_in(screen, duration=30):
    fade_surface = pygame.Surface((screen_width, screen_height))
    fade_surface.fill((0, 0, 0))  # Start with black
    for i in range(0, 255, 255 // duration):  # Gradual fade-in
        fade_surface.set_alpha(i)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(10)

def fade_out(screen, duration=30):
    fade_surface = pygame.Surface((screen_width, screen_height))
    fade_surface.fill((0, 0, 0))  # Start with black
    for i in range(255, 0, -(255 // duration)):  # Gradual fade-out
        fade_surface.set_alpha(i)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(10)
level_1_instructions = """
    "Find words starting with the given letter.",
    "3 lifelines are available for the game.",
    "Lose a lifeline for wrong words.",
    "If all lifelines are lost, the AI wins.",
    "Repeated words deduct 1 point from total score."
"""

level_2_instructions = """
- Find words ending with the given letter.
- Incorrect words lose 1 lifeline.
- 3 lifelines are available; game ends when they're gone (AI wins).
- Repeated words lose 1 point.
- Incorrect words are rejected, no points awarded, and 1 lifeline lost.
- Follow the word constraints.
"""

level_3_instructions = """
- Find words which does not contain the given letters.
- Incorrect words lose 1 lifeline.
- 3 lifelines are available; game ends when they're gone (AI wins).
- Repeated words lose 1 point.
- Incorrect words are rejected, no points awarded, and 1 lifeline lost.
- Follow the word constraints.
"""


def display_level_1_instructions():
    # Title text at the top of the screen
    title_text = "Level 1 Instructions"
    title_font = pygame.font.Font('harryp__.ttf', 40)  # Title font (can be adjusted)
    title_surface = title_font.render(title_text, True, (255, 255, 0))  # Yellow color for title
    title_x = (screen_width - title_surface.get_width()) // 2  # Center the title horizontally
    screen.blit(title_surface, (title_x, 20))  # Draw title at the top (20px margin)

    # Draw a box for instructions below the title
    box_width, box_height = 600, 300
    box_x, box_y = (screen_width - box_width) // 2, (screen_height - box_height) // 2 + 50  # Start below title
    pygame.draw.rect(screen, (255, 255, 255), (box_x, box_y, box_width, box_height), 3)  # White border
    pygame.draw.rect(screen, (0, 0, 0), (box_x + 5, box_y + 5, box_width - 10, box_height - 10))  # Black fill

    # Split the instructions into lines
    lines = level_1_instructions.splitlines()
    y_offset = box_y + 20  # Start drawing text after some padding
    line_height = 25  # Set height between lines for better spacing

    # Render and display the instructions in pixel font
    for line in lines:
        # Render each line of instruction
        text_surface = pixel_font.render(line, True, (255, 255, 255))  # White text
        # Ensure the text fits inside the box
        if text_surface.get_width() > box_width - 20:
            # If the text exceeds the box width, wrap it (or handle it differently)
            words = line.split()
            wrapped_line = ''
            for word in words:
                if pixel_font.size(wrapped_line + ' ' + word)[0] < box_width - 20:
                    wrapped_line += ' ' + word
                else:
                    screen.blit(pixel_font.render(wrapped_line, True, (255, 255, 255)), (box_x + 10, y_offset))
                    y_offset += line_height
                    wrapped_line = word  # Start a new line with the current word
            screen.blit(pixel_font.render(wrapped_line, True, (255, 255, 255)), (box_x + 10, y_offset))
            y_offset += line_height
        else:
            screen.blit(text_surface, (box_x + 10, y_offset))  # Padding for text
            y_offset += line_height  # Move down for next line of text

    pygame.display.flip()
def display_level_2_instructions():
    # Title text at the top of the screen
    title_text = "Level 2 Instructions"
    title_font = pygame.font.Font('harryp__.ttf', 40)  # Title font (can be adjusted)
    title_surface = title_font.render(title_text, True, (255, 255, 0))  # Yellow color for title
    title_x = (screen_width - title_surface.get_width()) // 2  # Center the title horizontally
    screen.blit(title_surface, (title_x, 20))  # Draw title at the top (20px margin)

    # Draw a box for instructions below the title
    box_width, box_height = 600, 300
    box_x, box_y = (screen_width - box_width) // 2, (screen_height - box_height) // 2 + 50  # Start below title
    pygame.draw.rect(screen, (255, 255, 255), (box_x, box_y, box_width, box_height), 3)  # White border
    pygame.draw.rect(screen, (0, 0, 0), (box_x + 5, box_y + 5, box_width - 10, box_height - 10))  # Black fill

    # Split the instructions into lines
    lines = level_2_instructions.splitlines()
    y_offset = box_y + 20  # Start drawing text after some padding
    line_height = 25  # Set height between lines for better spacing

    # Render and display the instructions in pixel font
    for line in lines:
        # Render each line of instruction
        text_surface = pixel_font.render(line, True, (255, 255, 255))  # White text
        # Ensure the text fits inside the box
        if text_surface.get_width() > box_width - 20:
            # If the text exceeds the box width, wrap it (or handle it differently)
            words = line.split()
            wrapped_line = ''
            for word in words:
                if pixel_font.size(wrapped_line + ' ' + word)[0] < box_width - 20:
                    wrapped_line += ' ' + word
                else:
                    screen.blit(pixel_font.render(wrapped_line, True, (255, 255, 255)), (box_x + 10, y_offset))
                    y_offset += line_height
                    wrapped_line = word  # Start a new line with the current word
            screen.blit(pixel_font.render(wrapped_line, True, (255, 255, 255)), (box_x + 10, y_offset))
            y_offset += line_height
        else:
            screen.blit(text_surface, (box_x + 10, y_offset))  # Padding for text
            y_offset += line_height  # Move down for next line of text

    pygame.display.flip()
def display_level_3_instructions():
    # Title text at the top of the screen
    title_text = "Level 3 Instructions"
    title_font = pygame.font.Font('harryp__.ttf', 40)  # Title font (can be adjusted)
    title_surface = title_font.render(title_text, True, (255, 255, 0))  # Yellow color for title
    title_x = (screen_width - title_surface.get_width()) // 2  # Center the title horizontally
    screen.blit(title_surface, (title_x, 20))  # Draw title at the top (20px margin)

    # Draw a box for instructions below the title
    box_width, box_height = 600, 300
    box_x, box_y = (screen_width - box_width) // 2, (screen_height - box_height) // 2 + 50  # Start below title
    pygame.draw.rect(screen, (255, 255, 255), (box_x, box_y, box_width, box_height), 3)  # White border
    pygame.draw.rect(screen, (0, 0, 0), (box_x + 5, box_y + 5, box_width - 10, box_height - 10))  # Black fill

    # Split the instructions into lines
    lines = level_3_instructions.splitlines()
    y_offset = box_y + 20  # Start drawing text after some padding
    line_height = 25  # Set height between lines for better spacing

    # Render and display the instructions in pixel font
    for line in lines:
        # Render each line of instruction
        text_surface = pixel_font.render(line, True, (255, 255, 255))  # White text
        # Ensure the text fits inside the box
        if text_surface.get_width() > box_width - 20:
            # If the text exceeds the box width, wrap it (or handle it differently)
            words = line.split()
            wrapped_line = ''
            for word in words:
                if pixel_font.size(wrapped_line + ' ' + word)[0] < box_width - 20:
                    wrapped_line += ' ' + word
                else:
                    screen.blit(pixel_font.render(wrapped_line, True, (255, 255, 255)), (box_x + 10, y_offset))
                    y_offset += line_height
                    wrapped_line = word  # Start a new line with the current word
            screen.blit(pixel_font.render(wrapped_line, True, (255, 255, 255)), (box_x + 10, y_offset))
            y_offset += line_height
        else:
            screen.blit(text_surface, (box_x + 10, y_offset))  # Padding for text
            y_offset += line_height  # Move down for next line of text

    pygame.display.flip()




# Game loop
running = True
screen_state = 1  # 1 for main menu, 2 for Bellatrix screen, 3 for level 1 instructions
level_1_completed = False  # Track if Level 1 is completed
# Define button dimensions for Back and Go buttons
go_btn_w, go_btn_h = 150, 50  # Go button size
go_btn_x = screen_width - go_btn_w - 20  # Position the Go button towards the right
go_btn_y = screen_height -50 # Position the Go button towards the bottom

back_btn_w, back_btn_h = 150, 50  # Back button size
back_btn_x = 20  # Position the Back button towards the left
back_btn_y = screen_height - 50  # Position the Back button towards the bottom

# Game loop
running = True
screen_state = 1  # 1 for main menu, 2 for Bellatrix screen, 3 for level 1 instructions, 4 for Voldemort screen
level_1_completed = False  # Track if Level 1 is completed
user_input = ''  # Variable to store user input

# Game loop
while running:
    screen.fill(bg_color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # Main menu button clicks
            if screen_state == 1 and len(typed_text) == len(dialogue):  # Wait until dialogue finishes
                if screen_width // 2 - btn_w // 2 <= mx <= screen_width // 2 + btn_w // 2:
                    if btn_y_positions[0] <= my <= btn_y_positions[0] + btn_h:  # Level 1 Button
                        screen_state = 3  # Go to Level 1 instructions screen
                    elif btn_y_positions[1] <= my <= btn_y_positions[1] + btn_h:  # Level 2 Button
                        screen_state = 5  # Show Bellatrix (Level 2)
                    elif btn_y_positions[2] <= my <= btn_y_positions[2] + btn_h:  # Level 3 Button
                        screen_state = 6 # Show Bellatrix (Level 3)

            # Level 1 instructions back button click
            elif screen_state == 3:  # If Level 1 instructions
                if back_btn_x <= mx <= back_btn_x + back_btn_w and back_btn_y <= my <= back_btn_y + back_btn_h:
                    screen_state = 1  # Go back to the main menu
                elif go_btn_x <= mx <= go_btn_x + go_btn_w and go_btn_y <= my <= go_btn_y + go_btn_h:
                    level_1_completed=True
                    with open('balletrix_dialogue.py') as file:
                            exec(file.read())

            elif screen_state == 5: 
                display_level_2_instructions()
                if back_btn_x <= mx <= back_btn_x + back_btn_w and back_btn_y <= my <= back_btn_y + back_btn_h:
                    screen_state = 1  # Go back to the main menu
                elif go_btn_x <= mx <= go_btn_x + go_btn_w and go_btn_y <= my <= go_btn_y + go_btn_h:
                    with open('umbridge_dialogue.py') as file:
                            exec(file.read())
                    
                         

                    
                   
            elif screen_state == 6: 
                display_level_3_instructions()
                if back_btn_x <= mx <= back_btn_x + back_btn_w and back_btn_y <= my <= back_btn_y + back_btn_h:
                    screen_state = 1  # Go back to the main menu
                elif go_btn_x <= mx <= go_btn_x + go_btn_w and go_btn_y <= my <= go_btn_y + go_btn_h:
                     with open('voldermot_dialogue.py') as file:
                            exec(file.read())
                    
                    
                    
                   

        '''elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and screen_state == 4:  # When user presses 'Enter' after Voldemort's dialogue
                print(f"User Input: {user_input}")  # You can store or use this input further
                # Optionally, reset the input after pressing 'Enter'
                user_input = ''
            
            # Handle text input (type into the box)
            if screen_state == 4:
                if back_btn_x <= mx <= back_btn_x + back_btn_w and back_btn_y <= my <= back_btn_y + back_btn_h:
                    screen_state = 1
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]  # Remove last character on backspace
                else:
                    user_input += event.unicode  # Add typed character'''

    # Main menu screen
    if screen_state == 1:
        # Display Harry Potter character image
        screen.blit(harry_image, (screen_width // 2 - 300, 100))  # Adjust position as needed

        # Animate dialogue with typewriter effect
        if typing_index < len(dialogue):
            frame_count += 1
            if frame_count % typing_speed == 0:
                typed_text += dialogue[typing_index]
                typing_index += 1

        # Render and display the dialogue text using the Harry Potter font
        dialogue_surface = font.render(typed_text, True, text_color)
        screen.blit(dialogue_surface, (screen_width // 2 - dialogue_surface.get_width() // 2, 50))

        # Draw buttons for levels (centered horizontally)
        btn_x = screen_width // 2 - btn_w // 2  # Center horizontally
        pygame.draw.rect(screen, button_color, (btn_x, btn_y_positions[0], btn_w, btn_h))
        pygame.draw.rect(screen, button_color, (btn_x, btn_y_positions[1], btn_w, btn_h))
        pygame.draw.rect(screen, button_color, (btn_x, btn_y_positions[2], btn_w, btn_h))

        # Display level text on buttons
        level_text1 = font.render("Level 1", True, text_color)
        screen.blit(level_text1, (btn_x + (btn_w // 2) - (level_text1.get_width() // 2), btn_y_positions[0] + 30))

        level_text2 = font.render("Level 2", True, text_color)
        screen.blit(level_text2, (btn_x + (btn_w // 2) - (level_text2.get_width() // 2), btn_y_positions[1] + 30))

        level_text3 = font.render("Level 3", True, text_color)
        screen.blit(level_text3, (btn_x + (btn_w // 2) - (level_text3.get_width() // 2), btn_y_positions[2] + 30))

    # Bellatrix dialogue screen (for Level 2 and Level 3)
    elif screen_state == 2:
       
        # Display full screen background
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
        bellatrix_font = pygame.font.Font('harryp__.ttf', 48)  # Larger font size for Bellatrix dialogue
        bellatrix_surface = bellatrix_font.render(bellatrix_typed_text, True, pygame.Color('white'))
        screen.blit(bellatrix_surface, (screen_width // 2 - bellatrix_surface.get_width() // 2, 350))

        # Draw Back button on the Bellatrix screen
        pygame.draw.rect(screen, button_color, (back_btn_x, back_btn_y, back_btn_w, back_btn_h))
        back_text = font.render("Back", True, text_color)
        screen.blit(back_text, (back_btn_x + (back_btn_w // 2) - (back_text.get_width() // 2), back_btn_y + (back_btn_h // 2) - (back_text.get_height() // 2)))

    # Level 1 instruction screen
    elif screen_state == 3:
        display_level_1_instructions()  # Display the instructions

        # Draw Back button at the left end
        pygame.draw.rect(screen, button_color, (back_btn_x, back_btn_y, back_btn_w, back_btn_h))
        back_text = font.render("Back", True, text_color)
        screen.blit(back_text, (back_btn_x + (back_btn_w // 2) - (back_text.get_width() // 2), back_btn_y + (back_btn_h // 2) - (back_text.get_height() // 2)))
        
        # Draw Go button at the right end
        pygame.draw.rect(screen, button_color, (go_btn_x, go_btn_y, go_btn_w, go_btn_h))
        go_text = font.render("Go", True, text_color)
        screen.blit(go_text, (go_btn_x + (go_btn_w // 2) - (go_text.get_width() // 2), go_btn_y + (go_btn_h // 2) - (go_text.get_height() // 2)))

    # Voldemort screen
    

  
     
    elif screen_state == 5:
        display_level_2_instructions()  # Display the instructions

        # Draw Back button at the left end
        pygame.draw.rect(screen, button_color, (back_btn_x, back_btn_y, back_btn_w, back_btn_h))
        back_text = font.render("Back", True, text_color)
        screen.blit(back_text, (back_btn_x + (back_btn_w // 2) - (back_text.get_width() // 2), back_btn_y + (back_btn_h // 2) - (back_text.get_height() // 2)))
        
        # Draw Go button at the right end
        pygame.draw.rect(screen, button_color, (go_btn_x, go_btn_y, go_btn_w, go_btn_h))
        go_text = font.render("Go", True, text_color)
        screen.blit(go_text, (go_btn_x + (go_btn_w // 2) - (go_text.get_width() // 2), go_btn_y + (go_btn_h // 2) - (go_text.get_height() // 2)))

    elif screen_state == 6:
        display_level_3_instructions()  # Display the instructions

        # Draw Back button at the left end
        pygame.draw.rect(screen, button_color, (back_btn_x, back_btn_y, back_btn_w, back_btn_h))
        back_text = font.render("Back", True, text_color)
        screen.blit(back_text, (back_btn_x + (back_btn_w // 2) - (back_text.get_width() // 2), back_btn_y + (back_btn_h // 2) - (back_text.get_height() // 2)))
        
        # Draw Go button at the right end
        pygame.draw.rect(screen, button_color, (go_btn_x, go_btn_y, go_btn_w, go_btn_h))
        go_text = font.render("Go", True, text_color)
        screen.blit(go_text, (go_btn_x + (go_btn_w // 2) - (go_text.get_width() // 2), go_btn_y + (go_btn_h // 2) - (go_text.get_height() // 2)))
    
    # Update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()