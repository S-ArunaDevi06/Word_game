import pygame
import sys
import random
import csv
import enchant
from pygame.locals import *

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen setup
screen_width, screen_height = 700, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Harry Potter with Lightning Effect")

# Load images
try:
    hall_image = pygame.image.load('round_background.jpg')  
    voldermort_image = pygame.image.load('voldermot.png')  
except pygame.error as e:
    print("Error loading images:", e)
    pygame.quit()
    sys.exit()

# Scale images
hall_image = pygame.transform.scale(hall_image, (screen_width, screen_height))
voldermort_image = pygame.transform.scale(voldermort_image, (150, 200))
voldermort_rect = voldermort_image.get_rect(center=(screen_width // 2, screen_height // 2))

# Font and colors
font = pygame.font.Font(None, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
button_color = pygame.Color('green')
text_color = pygame.Color('black')

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

# Game logic functions

def get_words():
    with open('wordlist.csv', newline='') as csvfile:
        wordlist = []
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for i in spamreader:
            if ('-' in i[0]) or ("'" in i[0]):
                continue
            wordlist.append(i[0].lower())
    wordlist.sort()    
    return wordlist

def get_start_fixed_list(wordlist, letter):
    l = [i for i in wordlist if i[0] == letter]
    return l

def get_top_words(word_list, no_of_words, used_word, current_points):
    word_heuristics = {}
    top_words = []
    for i in word_list:
        word_heuristics[i] = calculate_heuristic(i, used_word, current_points)
    val = list(word_heuristics.values())
    key = list(word_heuristics.keys())
    i = 0
    while i < no_of_words:   
        mini = min(val)
        freq = val.count(mini)
        for j in range(freq):
            if len(top_words) == no_of_words:
                return top_words
            min_word = key[val.index(mini)]
            top_words.append(min_word)
            key.pop(val.index(mini))
            val.pop(val.index(mini))
            i += 1
    return top_words

def calculate_heuristic(word, used_words, current_points):
    heuristic = 0
    heuristic += 15 - len(word)
    if word in used_words:
        heuristic += 2
    heuristic += (30 - current_points)
    return heuristic

def round1(used_words, user_used_words, lifelines, d):
    letter = chr(random.randint(97, 122))
    print("\nALL THE WORDS FORMED SHOULD START WITH THE LETTER : ", letter)

    user_life = 30
    ai_life = 30

    while ai_life > 0 and user_life > 0:
        print("USER LIFE: ", user_life, "\n AI LIFE: ", ai_life)
        user_word = input_text
        print(d.check(user_word))
        print("USER USED WORDS: ", user_used_words, "USED_WORDS: ", used_words)
        if user_word.startswith(letter) and user_word not in user_used_words and user_word not in used_words and d.check(user_word):
            user_used_words.append(user_word)
        elif (not (user_word.startswith(letter)) or (user_word in user_used_words or user_word in used_words) or not (d.check(user_word)) and lifelines > 0):
            while (not (user_word.startswith(letter)) or (user_word in user_used_words or user_word in used_words) or not (d.check(user_word)) and lifelines > 0):
                print("\nYOU HAVE ENTERED A WORD THAT GO AGAINST THE CONDITION SPECIFIED! TRY AGAIN POTTER!!")
                lifelines -= 1
                user_word = input_text
            if lifelines == 0:
                print("\nYOU LOST POTTER!!!!!!!")
            else:
                user_used_words.append(user_word)

        if ai_life <= 0 or lifelines <= 0:
            break

        ai_life -= len(user_word)

        start_word_list = get_start_fixed_list(wordlist, letter)
        start_top_words = get_top_words(start_word_list, 10, used_words, (30 - user_life))
        reply_word = start_top_words[random.randint(0, len(start_top_words) - 1)]

        while reply_word in used_words or reply_word in user_used_words:
            reply_word = start_top_words[random.randint(0, len(start_top_words) - 1)]
        print("AI: ", reply_word)
        user_life -= len(reply_word)
        used_words.append(reply_word)

    print("\nUSER LIFE: ", user_life, "\nAI_LIFE: ", ai_life)
    if user_life <= 0:
        print("YOU GOT DEFEATED BY BELLATRIX!!")
    elif ai_life <= 0:
        print("WELL DONE POTTER!")
    else:
        print("IN MY PLACE, YOU HAVE TO OBEY MY RULES!")

# Word list
d = enchant.Dict("en_US")
wordlist = get_words()
used_words = []
user_used_words = []

# Lightning effect function
def draw_lightning_effect(start_pos, end_pos):
    segments = [start_pos]
    for _ in range(10):  
        x = segments[-1][0] + random.randint(-15, 15)
        y = segments[-1][1] + random.randint(10, 30)
        segments.append((x, y))

    for i in range(len(segments) - 1):
        pygame.draw.line(screen, (255, 255, 200), segments[i], segments[i + 1], 2)

# Play background music
def play_music():
    try:
        pygame.mixer.music.load('harry_potter_music.mp3')  
        pygame.mixer.music.play(-1, 0.0)
    except pygame.error as e:
        print("Error loading music:", e)

# Game loop
running = True
screen_state = 1  # 1 for main menu, 2 for level selection, 3 for Voldemort screen
display_text = ""  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.mixer.music.stop()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            if screen_state == 1:
                if screen_width // 2 - btn_w // 2 <= mx <= screen_width // 2 + btn_w // 2:
                    if btn_y_positions[0] <= my <= btn_y_positions[0] + btn_h:
                        screen_state = 3  
                    elif btn_y_positions[1] <= my <= btn_y_positions[1] + btn_h:
                        screen_state = 3  
                    elif btn_y_positions[2] <= my <= btn_y_positions[2] + btn_h:
                        screen_state = 3  

            if screen_state == 3:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                if button_box.collidepoint(event.pos):
                    show_lightning = True
                    lightning_timer = 50
                    round1(used_words, user_used_words, 3, d)
                if back_button_box.collidepoint(event.pos):
                    screen_state = 1  

        elif event.type == pygame.KEYDOWN:
            if screen_state == 3 and active:
                if event.key == pygame.K_RETURN:
                    display_text = input_text.strip()
                    input_text = " "  
                    print(f"Entered text: {display_text}")  
                    show_lightning = True
                    lightning_timer = 50
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    if screen_state == 1:
        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, button_color, (screen_width // 2 - btn_w // 2, btn_y_positions[0], btn_w, btn_h))
        pygame.draw.rect(screen, button_color, (screen_width // 2 - btn_w // 2, btn_y_positions[1], btn_w, btn_h))
        pygame.draw.rect(screen, button_color, (screen_width // 2 - btn_w // 2, btn_y_positions[2], btn_w, btn_h))

    elif screen_state == 3:
        if not pygame.mixer.music.get_busy():
            play_music()

        screen.blit(hall_image, (0, 0)) 
        screen.blit(voldermort_image, voldermort_rect) 

        # Draw input box
        txt_surface = font.render(input_text, True, text_color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.fill(color_active if active else color_inactive, input_box)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        # Display Enter button
        pygame.draw.rect(screen, button_color, button_box)
        button_text = font.render("Enter", True, text_color)
        screen.blit(button_text, (button_box.x + 10, button_box.y + 5))

        # Display Back button
        pygame.draw.rect(screen, button_color, back_button_box)
        back_text = font.render("Back", True, text_color)
        screen.blit(back_text, (back_button_box.x + 10, back_button_box.y + 5))

        # Display entered text
        if display_text:
            entered_text_surface = font.render(display_text, True, text_color)
            screen.blit(entered_text_surface, (screen_width // 2 - entered_text_surface.get_width() // 2, screen_height - 50))

        # Lightning effect towards the screen
        if show_lightning and lightning_timer > 0:
            lightning_start = (screen_width // 2, screen_height // 2 - 50)
            lightning_end = (screen_width // 2, screen_height // 2 + 100)
            draw_lightning_effect(lightning_start, lightning_end)
            lightning_timer -= 1
        else:
            show_lightning = False  

        pygame.display.flip()  # Update the screen


pygame.quit()
