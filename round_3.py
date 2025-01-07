import pygame
import csv
import random
import enchant
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Game - Round 3")

# Load background image
background_img = pygame.image.load("first_background.jpg").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
try:
    title_font = pygame.font.Font("retro_computer.ttf", 15) 
    title_font.set_bold(True)
    text_font = pygame.font.Font("retro_computer.ttf", 15)  
except FileNotFoundError:
    print("Font file not found. Make sure retro_computer.ttf is in the same directory.")
    pygame.quit()
    sys.exit()

# Initialize Enchant dictionary
d = enchant.Dict("en_US")
width, height = 700, 500
exit_button = pygame.Rect(width // 2 - 75, height - 100, 150, 50)
exit_text = text_font.render("Exit", True, (255, 0, 0))

def score_represent(lifelines, user_life,ai_life):
    # Initialize pygame
    pygame.init()

    # Set up display
    width, height = 700, 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game Scorecard")
    player_name = "Harry Potter"
    total_score = 30
    lifelines = lifelines
    background_image_path = 'first_background.jpg' 


    # Load and scale the background image
    try:
        background_image = pygame.image.load(background_image_path)
        background_image = pygame.transform.scale(background_image, (width, height))
    except pygame.error as e:
        print(f"Error loading background image: {e}")
        pygame.quit()
        sys.exit()

    # Create texts for the scorecard
    title_text = title_font.render("Game Scorecard", True, (255, 215, 0)) 
    player_text = text_font.render(f"Player Name: {player_name}", True, (255, 255, 255))
    lifelines_text = text_font.render(f"Lifelines Remaining: {lifelines}", True, (255, 255, 255))

    
    # Define Exit button
    exit_button = pygame.Rect(width // 2 - 75, height - 100, 150, 50)
    exit_text = text_font.render("Exit", True, (255, 0, 0))

    # Main loop to display the scorecard until user exits
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Detect button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):  
                    with open('level_dialogue_1.py') as file:
                        exec(file.read()) 
                    running = False  

        # Draw background image
        screen.blit(background_image, (0, 0))

        # Draw texts on screen
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, 20))
        screen.blit(player_text, (50, 100))
        
        screen.blit(lifelines_text, (50, 180))
        user_points,ai_points=user_life,ai_life
        # Display each word and corresponding points
        y_offset = 220
        word_text = text_font.render(f"Your power: {user_points} | AI Power: {ai_points}\n", True, (255, 255, 255))
        screen.blit(word_text, (50, y_offset))
        if user_life <= 0:
            defeat_text1 = text_font.render("YOU GOT DEFEATED BY BELLATRIX!!", True, (255, 0, 0))
            
            screen.blit(defeat_text1, (50, 280))
            
        
        elif ai_life <= 0:
            victory_text1 = text_font.render("WELL DONE POTTER!", True, (0, 255, 0))
            
            screen.blit(victory_text1, (50, 280))
            

        else:
            rule_text = text_font.render("IN MY PLACE, YOU HAVE TO OBEY MY RULES!", True, (255, 255, 255))
            screen.blit(rule_text, (50, 280))
        pygame.display.flip()
    pygame.quit()
    sys.exit()



def score_representing(lifelines, user_life,ai_life):
    # Initialize pygame
    pygame.init()

    # Set up display
    width, height = 700, 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game Scorecard")
    player_name = "Harry Potter"
    total_score = 30
    lifelines = lifelines
    background_image_path = 'first_background.jpg'  # Path to the background image file


    # Load and scale the background image
    try:
        background_image = pygame.image.load(background_image_path)
        background_image = pygame.transform.scale(background_image, (width, height))
    except pygame.error as e:
        print(f"Error loading background image: {e}")
        pygame.quit()
        sys.exit()

    # Created texts for the scorecard
    title_text = title_font.render("Game Scorecard", True, (255, 215, 0))  # Gold color for title
    player_text = text_font.render(f"Player Name: {player_name}", True, (255, 255, 255))
    lifelines_text = text_font.render(f"Lifelines Remaining: {lifelines}", True, (255, 255, 255))

    # Main loop to display the scorecard until user exits
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

       
        screen.blit(background_image, (0, 0))

       
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, 20))
        screen.blit(player_text, (50, 100))
        
        screen.blit(lifelines_text, (50, 180))
        user_points,ai_points=user_life,ai_life
       
        y_offset = 220
        word_text = text_font.render(f"Your power: {user_points} | AI Power: {ai_points}\n", True, (255, 255, 255))
        screen.blit(word_text, (50, y_offset))
        if user_life <= 0:
            defeat_text1 = text_font.render("YOU GOT DEFEATED BY VOLDEMORT!!", True, (255, 0, 0))
            
            screen.blit(defeat_text1, (50, 280))
            
        
        elif ai_life <= 0:
            victory_text1 = text_font.render("WELL DONE POTTER!", True, (0, 255, 0))
            
            screen.blit(victory_text1, (50, 280))
            

        else:
            rule_text = text_font.render("IN MY PLACE, YOU HAVE TO OBEY MY RULES!", True, (255, 255, 255))
            screen.blit(rule_text, (50, 280))
        pygame.display.flip()
    pygame.quit()
    sys.exit()





# Load word list from CSV
def get_words():
    with open('wordlist.csv', newline='') as csvfile:
        wordlist = []
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for i in spamreader:
            if '-' in i[0] or "'" in i[0]:
                continue
            wordlist.append(i[0].lower())
    return sorted(wordlist)

# Display text on screen
def display_text(text, x, y, font, color=WHITE):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

def get_start_fixed_list(wordlist, letter):
    return [i for i in wordlist if i[0] == letter]

def get_top_words(word_list, no_of_words, used_word, current_points):
    word_heuristics = {}
    top_words = []
    for i in word_list:
        word_heuristics[i] = calculate_heuristic(i, used_words, current_points)
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

def get_end_fixed_list(wordlist,letter):
   l=[i for i in wordlist if i[-1]==letter]
   return l

def contains(word,letters):
   for i in letters:
      if i in word:
         return False
   return True

def get_missing_letters_list(wordlist,letter_list):
   l=[]
   
   #print("MISSING LETTERS: ",letter_list)

   for i in wordlist:
      add=True
      for j in letter_list:
         if j in i:
            add=False
            break
      if add:
         l.append(i)
   return l


WHITE = (255, 255, 255)
RED = (255, 0, 0)
small_font =text_font
def display_text(text, x, y, font, color=(255, 255, 255)):
    #Displays text on the screen at a given position.
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def round3(used_words, user_used_words, lifelines, d):   
    letters = []
    for i in range(4):
        letter = chr(random.randint(0, 25) + 97)
        while letter in letters:
            letter = chr(random.randint(0, 25) + 97)
        letters.append(letter)

    print("\nALL THE WORDS FORMED SHOULD NOT CONTAIN THESE LETTERS : ", letters)
    
    user_life = 30
    ai_life = 30
    round_used_words = []
    clock = pygame.time.Clock()

    user_input = ""
    active = True  
    running = True
    game_over = False  

    while running:
        screen.blit(background_img, (0, 0))

        # Display round information
        display_text(f"Round 3 - Words should not contain {', '.join(letters)}", 20, 20, title_font)

        # Display lifelines and lives
        display_text(f"Lifelines: {lifelines}", 20, 80, text_font)
        display_text(f"User Life: {user_life}", 20, 120, text_font)
        display_text(f"AI Life: {ai_life}", 20, 160, text_font)

        # Display user input prompt
        display_text("Enter your word:", 20, 300, text_font)

        # Draw the input box
        input_box = pygame.Rect(200, 295, 300, 30)
        pygame.draw.rect(screen, WHITE, input_box, 2)
        display_text(user_input, input_box.x + 10, input_box.y + 5, text_font)

        # Display the words used by both the user and AI
        y_offset = 350
        display_text("User Words:", 20, y_offset, text_font)
        for idx, word in enumerate(user_used_words[-5:]): 
            display_text(word, 150, y_offset + (idx + 1) * 20, text_font)
        
        display_text("AI Words:", 350, y_offset, text_font)
        for idx, word in enumerate(used_words[-5:]): 
            display_text(word, 480, y_offset + (idx + 1) * 20, text_font)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle text input when box is active
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_RETURN and active:
                    # Check if user word is valid
                    if (contains(user_input, letters) and 
                        user_input not in user_used_words and 
                        user_input not in used_words and 
                        d.check(user_input)):
                        user_used_words.append(user_input)
                        round_used_words.append(user_input)
                        #user_life -= len(user_input)  # Reduce user life by word length
                        
                    elif lifelines > 0:
                        lifelines -= 1
                        user_input = ""  
                        continue
                    else:
                        print("No lifelines left!")
                        running = False
                        break

                    # AI Turn: Pick a word that doesn't contain any forbidden letters
                    start_word_list=get_missing_letters_list(wordlist,letters)
                    start_top_words=get_top_words(start_word_list,3,used_words,(30-user_life))
                    reply_word=start_top_words[random.randint(0,len(start_top_words)-1)]

                    while reply_word in round_used_words:
                        reply_word = start_top_words[random.randint(0, len(start_top_words) - 1)]
                    
                    print("AI:", reply_word)
                    ai_life -= len(user_input)
                    user_life-=len(reply_word)
                    used_words.append(reply_word)  # Append AI's chosen word to used_words

                    # Reset user input for next turn
                    user_input = ""

                    # Check for end of game
                    if user_life <= 0 or ai_life <= 0:
                        game_over = True

                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        # If game is over, display "Press any key to continue" message
        if game_over:
            score_representing(lifelines, user_life, ai_life)

        # Update display
        pygame.display.flip()
        clock.tick(60)


# Start the game
used_words = []
user_used_words = []
lifelines = 3
d = enchant.Dict("en_US")
wordlist=get_words()

#round1(used_words, user_used_words, lifelines)
#round2(used_words, user_used_words, lifelines,d)
round3(used_words, user_used_words, lifelines,d)

