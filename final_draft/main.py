import pygame
from layout import default_background, box_with_text, render_text
from classes import Box
from controls import *
from colors import *
from global_variables import *
from excel_loader import excel_file
from image import *
import random

# Initialize Pygame
pygame.init()
CLOCK = pygame.time.Clock()
games = excel_file()
CURRENT_GAME = None
SOUNDON = False
TEST = False
SCORE = 0
SHOT_COUNTER = 0
BEER_COUNTER = 0

if WINDOW == None:
    WINDOW = "MENU"
    UPDATE_BACKGROUND = True

# Initialize Screen
def initialize_screen(test_mode=False, size=(1280, 720)):
    screen_size = size if test_mode else (pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode(screen_size)
    return screen, screen_size

SCREEN, (WIDTH, HEIGHT) = initialize_screen(test_mode=False) # Creating Screen, width and height global variables
background_image_url = "images//background_image.jpg"


# ----------------- Main Program ----------------- #
MENUBOX1, MENUBOX2, MENUBOX3 = None, None, None # Create Menu interaction Boxes
SETTINGSBOX1, SETTINGSBOX2, SETTINGSBOX3,SETTINGSBOX4,SETTINGSBOX5,SETTINGSBOX6,SETTINGSBOX7 = None, None, None, None, None, None, None # Create Menu interaction Boxes
EXITBOX = None
SETTINGSTEXTBOX = None

#----------- Advanced Rule Boxes -----------#
RULEBOX_CALL_FRIEND = None
RULEBOX_ASK_AUDIENCE = None
RULEBOX_50_50 = None
RULEBOX_REMOVE_ANSWER = None
CALL_FRIEND = True
ASK_AUDIENCE = True
FIFTY_FIFTY = True
REMOVE_ANSWER = True
#----------- Advanced settings Boxes -----------#
SOUNDONBOX = None

#----------- GAME settings Boxes -----------#
ANSWERBOX1 = None
ANSWERBOX2 = None
ANSWERBOX3 = None
ANSWERBOX4 = None
QUESTIONBOX = None
HELPERBOX1 = None
HELPERBOX2 = None
HELPERBOX3  = None
HELPERBOX4 = None

def create_boxes(width: int, height: int) -> None:
    """
    This function will create the boxes for the game
    """
    global MENUBOX1, MENUBOX2, MENUBOX3
    #----------- Menu Boxes -----------#
    margin = 10
    button_width = (width/2 - 2 * margin) 
    button_height = (height/2 - 4 * margin) // 3     
    MENUBOX1 = Box(width/4 + margin, height/4 + 2*margin                    , button_width  ,button_height) #Box1
    MENUBOX2 = Box(width/4 + margin, height/4 + button_height + 2*margin    , button_width  ,button_height) #Box2
    MENUBOX3 = Box(width/4 + margin, height/4 + 2 * button_height + 2*margin, button_width  ,button_height) #Box3
    global SETTINGSBOX1, SETTINGSBOX2, SETTINGSBOX3,SETTINGSBOX4,SETTINGSBOX5,SETTINGSBOX6,SETTINGSBOX7
    global EXITBOX, SETTINGSTEXTBOX
    x0 = 2* WIDTH / 4
    y0 = HEIGHT / 4 + 10
    box_width = WIDTH / 4 - 10 # Fixed width for all boxes
    box_height = 50  # Fixed height for each box
    margin = 5  # Space between boxes
    current_y = y0 + margin
    SETTINGSBOX1 = Box(x0, current_y + 0 * (box_height + margin), box_width, box_height)
    SETTINGSBOX2 = Box(x0, current_y + 1 * (box_height + margin), box_width, box_height)
    SETTINGSBOX3 = Box(x0, current_y + 2 * (box_height + margin), box_width, box_height)
    SETTINGSBOX4 = Box(x0, current_y + 3 * (box_height + margin), box_width, box_height)
    SETTINGSBOX5 = Box(x0, current_y + 4 * (box_height + margin), box_width, box_height)
    SETTINGSBOX6 = Box(x0, current_y + 5 * (box_height + margin), box_width, box_height)
    SETTINGSBOX7 = Box(x0, current_y + 6 * (box_height + margin), box_width, box_height)
    SETTINGSTEXTBOX = Box(WIDTH / 4, HEIGHT / 4, WIDTH / 4, HEIGHT / 4)
    EXITBOX = Box(WIDTH / 2 - 100, HEIGHT - 50 , 200 , 50)

    global SOUNDONBOX
    SOUNDONBOX = Box(10, 10, 50, 50)
    #----------- Advanced Rule Boxes -----------#
    global RULEBOX_50_50, RULEBOX_REMOVE_ANSWER, RULEBOX_CALL_FRIEND, RULEBOX_ASK_AUDIENCE
    x0 = WIDTH / 4 + 10
    y0 = HEIGHT / 4*2
    box_width = WIDTH / 4 - 10 # Fixed width for all boxes 
    box_height = 100  # Fixed height for each box
    RULEBOX_CALL_FRIEND = Box(x0, y0 + 0 * (box_height + margin), box_width, box_height)
    RULEBOX_ASK_AUDIENCE = Box(x0 + box_width, y0 + 0 * (box_height + margin), box_width, box_height)
    RULEBOX_50_50 = Box(x0, y0 + 1 * (box_height + margin), box_width, box_height)
    RULEBOX_REMOVE_ANSWER = Box(x0 + box_width, y0 + 1 * (box_height + margin), box_width, box_height)
    #----------- GAME settings Boxes -----------#
    global ANSWERBOX1, ANSWERBOX2, ANSWERBOX3, ANSWERBOX4, QUESTIONBOX
    global HELPERBOX1, HELPERBOX2, HELPERBOX3, HELPERBOX4
    margin = 10
    button_width = width / 4
    button_height = (height / 4) // 2
    ANSWERBOX1=Box(width / 8 * 2, height / 2, button_width, button_height)  # top left
    ANSWERBOX2=    Box(width / 8 * 2 + button_width, height / 2, button_width, button_height)  # top right
    ANSWERBOX3=    Box(width / 8 * 2, height / 2 + button_height, button_width, button_height)  # bottom left
    ANSWERBOX4=    Box(width / 8 * 2 + button_width, height / 2 + button_height, button_width, button_height)  # bottom right
    QUESTIONBOX = Box(width/6, 50 , 4*width/6, height/4*2  )

    HELPERBOX1 = Box(width/4, height/4*3, width/8, 100) 
    HELPERBOX2 = Box(width/4 + 1 * (width/8), height/4*3, width/8, 100)
    HELPERBOX3 = Box(width/4 + 2 * (width/8), height/4*3, width/8, 100)
    HELPERBOX4 = Box(width/4 + 3 * (width/8), height/4*3, width/8, 100)

create_boxes(WIDTH, HEIGHT)
print(SETTINGSBOX1.cords())
#Update Variables
MENU_HEADER_UPDATE = True
SETTINGS_HEADER_UPDATE = True
ADVANCED_HEADER_UPDATE = True

def menu_window():
    global MENUBOX1, MENUBOX2, MENUBOX3, SCREEN, MENU_HEADER_UPDATE, HEIGHT, WIDTH
    if MENU_HEADER_UPDATE:
        #----------- Header -----------#
        print("Updating Menu Header")
        text1 = "Who Want's to be a"
        text2 = "MILLIONAIRE"
        header_text1 = render_text(text1, 50, font="arialblack" , color = WHITE_COLOR)
        header_text2 = render_text(text2, 100, font="arialblack" , color = GOLD_COLOR)
        SCREEN.blit(header_text1, (WIDTH/2 - header_text1.get_width()/2, HEIGHT/20))
        SCREEN.blit(header_text2, (WIDTH/2 - header_text2.get_width()/2, HEIGHT/12))
        MENU_HEADER_UPDATE = False
    exit()
    box_with_text(SCREEN, "Start Game", MENUBOX1,font_name="arialblack", max_font_size=50)
    box_with_text(SCREEN, "Rules and Game Settings", MENUBOX2,font_name="arialblack", max_font_size=50)
    box_with_text(SCREEN, "Advanced Rules", MENUBOX3,font_name="arialblack", max_font_size=50)


def settings_choose_team():
    global games, SCREEN, WIDTH, HEIGHT
    global SETTINGSBOX1, SETTINGSBOX2, SETTINGSBOX3,SETTINGSBOX4,SETTINGSBOX5,SETTINGSBOX6,SETTINGSBOX7
    boxes = [SETTINGSBOX1, SETTINGSBOX2, SETTINGSBOX3,SETTINGSBOX4,SETTINGSBOX5,SETTINGSBOX6,SETTINGSBOX7]
    for idx, game_name in enumerate(games.keys()):
        box_with_text(SCREEN, game_name, boxes[idx], font_name="arialblack", max_font_size=30)
        
def settings_window():
    global SETTINGS_HEADER_UPDATE, SCREEN, HEIGHT, WIDTH
    if SETTINGS_HEADER_UPDATE:
        #----------- Header -----------#
        print("Updating Settings Header")
        text1 = "Rules and Game Settings"
        header_text1 = render_text(text1, 50, font="arialblack" , color = WHITE_COLOR)
        SCREEN.blit(header_text1, (WIDTH/2 - header_text1.get_width()/2, HEIGHT/20))
        #----------- Settings -----------#
        text_box = pygame.Surface((WIDTH/2,HEIGHT/2), pygame.SRCALPHA)
        text_box.fill((0, 0, 255, 125))
        draw_border(text_box, WIDTH/2, HEIGHT/2)      # Draw Border
        SCREEN.blit(text_box, (WIDTH/4, HEIGHT/4))    # Draw Transparet Box
        SETTINGS_HEADER_UPDATE = False
        settings_window_text()
    exit()
    settings_choose_team()
    settings_chosen_game()

def render_multiline_text(surface, text, font_name, color, rect, line_spacing=5, max_font_size=15):
    """
    Render multi-line text inside a box with automatic word wrapping for each rule.

    Args:
        surface (pygame.Surface): The surface to render text on.
        text (str): The multi-line text to render, with rules separated by newlines.
        font_name (str): The name of the font to use.
        color (tuple): The color of the text.
        rect (pygame.Rect): The rectangle area to draw the text in.
        line_spacing (int): Spacing between lines.
    """
    size = max_font_size
    if TEST:
        size = 12
    font = pygame.font.SysFont(font_name, size)  # Adjust font size as needed
    rules = text.split("\n")  # Split text into rules based on newlines
    x, y = rect.topleft

    for rule in rules:
        words = rule.split(' ')  # Split the rule into words for wrapping
        current_line = ''
        lines = []

        for word in words:
            test_line = current_line + ('' if current_line == '' else ' ') + word
            if font.size(test_line)[0] <= rect.width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        for line in lines:
            rendered_text = font.render(line, True, color)
            if y + rendered_text.get_height() > rect.bottom:
                break  # Stop if text exceeds the box height
            surface.blit(rendered_text, (x, y))
            y += rendered_text.get_height() + line_spacing

        # Add extra spacing between rules
        y += line_spacing

def settings_window_text():
    global SCREEN, WIDTH, HEIGHT
    text1 = """Reglerne er meget simple:
1. Du skal svare på 20 spørgsmål for at vinde 1 million kroner.
2. Du har 4 hjælpemidler: 50/50, Telefon en ven, Publikum, tag et shot og fjern en svarmulighed.
3. Du kan til enhver tid stoppe og tage pengene, du har vundet.
4. Hvis du svarer forkert, mister du alt undtagen dit sikrede beløb.
5. Du har ubegrænset tid til at svare på hvert spørgsmål, men du vil have begrænset tid til at bruge hjælpemidler.
6. Svarer du forkert, kan du bunde din drink og få et liv igen!"""

    # Define a rectangle area for the text box
    rect = pygame.Rect(10+WIDTH / 4, HEIGHT / 4 + 10, WIDTH / 4, HEIGHT / 2- 15)

    # Draw a semi-transparent box as background (optional)
    text_box = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    text_box.fill((0, 0, 0, 0))  # Semi-transparent black
    SCREEN.blit(text_box, rect.topleft)

    # Render the multi-line text
    render_multiline_text(SCREEN, text1, "arialblack", WHITE_COLOR, rect)

def settings_chosen_game():
    global games, SCREEN, WIDTH, HEIGHT, CURRENT_GAME
    global SETTINGSBOX1, SETTINGSBOX2, SETTINGSBOX3,SETTINGSBOX4,SETTINGSBOX5,SETTINGSBOX6,SETTINGSBOX7
    boxes = [SETTINGSBOX1, SETTINGSBOX2, SETTINGSBOX3,SETTINGSBOX4,SETTINGSBOX5,SETTINGSBOX6,SETTINGSBOX7]
    if CURRENT_GAME != None:
        idx = list(games.keys()).index(CURRENT_GAME)
        box_with_text(SCREEN, CURRENT_GAME, boxes[idx], font_name="arialblack", boxcolor1=GOLD_COLOR, max_font_size=30)


def advanced_rules_window():
    global ADVANCED_HEADER_UPDATE, SCREEN, HEIGHT, WIDTH
    if ADVANCED_HEADER_UPDATE:
        #----------- Header -----------#
        print("Updating Advhanced Header")
        text1 = "Advanced Rules"
        header_text1 = render_text(text1, 50, font="arialblack" , color = WHITE_COLOR)
        SCREEN.blit(header_text1, (WIDTH/2 - header_text1.get_width()/2, HEIGHT/20))
        #----------- Settings -----------#
        text_box = pygame.Surface((WIDTH/2,HEIGHT/2), pygame.SRCALPHA)
        text_box.fill((0, 0, 255, 125))
        draw_border(text_box, WIDTH/2, HEIGHT/2)      # Draw Border
        SCREEN.blit(text_box, (WIDTH/4, HEIGHT/4))    # Draw Transparet Box
        ADVANCED_HEADER_UPDATE = False
        advanced_rules_text()
    exit()
    advanced_rules_rule_box()

def advanced_rules_text():
    global SCREEN, WIDTH, HEIGHT
    text1 = """Venligst Vælg hvilke hjælpemidler der skal være tilladt at benytte i spillet."""
        # Define a rectangle area for the text box
    rect = pygame.Rect(10+WIDTH / 4, HEIGHT / 4 + 10, WIDTH / 2 - 20, HEIGHT / 4)

    # Draw a semi-transparent box as background (optional)
    text_box = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    text_box.fill((0, 0, 0, 0))  # Semi-transparent black
    SCREEN.blit(text_box, rect.topleft)

    # Render the multi-line text
    render_multiline_text(SCREEN, text1, "arialblack", WHITE_COLOR, rect, max_font_size=30)

def advanced_rules_rule_box():
    fifty_fifty_color = GREEN_COLOR if FIFTY_FIFTY else RED_COLOR
    remove_answer_color = GREEN_COLOR if REMOVE_ANSWER else RED_COLOR
    call_friend_color = GREEN_COLOR if CALL_FRIEND else RED_COLOR
    ask_audience_color = GREEN_COLOR if ASK_AUDIENCE else RED_COLOR
    box_with_text(SCREEN, "50/50", RULEBOX_50_50, font_name="arialblack", max_font_size=30, boxcolor1=fifty_fifty_color)
    box_with_text(SCREEN, "Fjern svarmulighed", RULEBOX_REMOVE_ANSWER, font_name="arialblack", max_font_size=30, boxcolor1=remove_answer_color)
    box_with_text(SCREEN, "Ring en ven", RULEBOX_CALL_FRIEND, font_name="arialblack", max_font_size=30, boxcolor1=call_friend_color)
    box_with_text(SCREEN, "Spørg publikum", RULEBOX_ASK_AUDIENCE, font_name="arialblack", max_font_size=30, boxcolor1=ask_audience_color)

def draw_answer_squares(screen: pygame.Surface, answers: list[str]) -> None:
    """
    Draws answer squares on the screen with text wrapping.
    """
    background_color = (41, 112, 227)
    foreground_color = (3, 35, 87)
    ekstra_text = ["A", "B", "C", "D"]
    font_size = 35
    boxes = [ANSWERBOX1, ANSWERBOX2, ANSWERBOX3, ANSWERBOX4]
    for idx, answer_option in enumerate(answers):
        text = ekstra_text[idx] + ": " + answers[idx]
        box_with_text(screen, text, boxes[idx], font_name="arialblack", max_font_size=font_size, boxcolor1=background_color, boxcolor2=foreground_color)


def draw_question_box(screen: pygame.Surface, question: str, question_idx: int) -> None:
    """
    Draws the question box on the screen with text wrapping.
    """
    background_color = (0, 0, 0)
    foreground_color = (41, 112, 227)
    text = f"Q{question_idx} : {question}"
    box_with_text(screen, text, QUESTIONBOX, font_name="arialblack", max_font_size=30, color=WHITE_COLOR,  boxcolor1=background_color, boxcolor2=foreground_color)

GAME_ON = False

def draw_help_boxes(screen: pygame.Surface, width: int, height: int) -> None:
    if FIFTY_FIFTY:
        box_with_text(screen, "50/50", HELPERBOX1, font_name="arialblack", max_font_size=30, boxcolor1=GREEN_COLOR)
    else:
        box_with_text(screen, "50/50", HELPERBOX1, font_name="arialblack", max_font_size=30, boxcolor1=RED_COLOR)
    if CALL_FRIEND:
        box_with_text(screen, "Ring en ven", HELPERBOX2, font_name="arialblack", max_font_size=30, boxcolor1=GREEN_COLOR)
    else:
        box_with_text(screen, "Ring en ven", HELPERBOX2, font_name="arialblack", max_font_size=30, boxcolor1=RED_COLOR)
    if ASK_AUDIENCE:
        box_with_text(screen, "Spørg publikum", HELPERBOX3, font_name="arialblack", max_font_size=30, boxcolor1=GREEN_COLOR)
    else:
        box_with_text(screen, "Spørg publikum", HELPERBOX3, font_name="arialblack", max_font_size=30, boxcolor1=RED_COLOR)
    if REMOVE_ANSWER:
        box_with_text(screen, "Tag et shot", HELPERBOX4, font_name="arialblack", max_font_size=30, boxcolor1=GREEN_COLOR)
    else:
        box_with_text(screen, "Tag et shot", HELPERBOX4, font_name="arialblack", max_font_size=30, boxcolor1=RED_COLOR)


def point_window(Screen: pygame.Surface, width: int, height: int, question_idx: int) -> None:
    """
    This function will draw the points on the screen
    """
    box_width = width // 5
    box_height = height // 20 - 10
    point_system = [100,200,300,500,1000,2000,4000,8000,16000,32000,64000,
                    125000,250000,500000,1000000,2000000,4000000,8000000,
                    16000000,32000000]
    box_with_text(Screen, "Monitos $$", Box(box_width*4, 4*box_height, box_width, box_height), font_name="arialblack", max_font_size=50, boxcolor1=BLUE_COLOR)
    for idx in range(20):
        if idx < question_idx:
            box_with_text(Screen, f"{point_system[idx]} $", Box(box_width*4, 5*box_height + idx * box_height, box_width, box_height), font_name="arialblack", max_font_size=50, boxcolor1=GREEN_COLOR)
        elif idx == question_idx:
            box_with_text(Screen, f"{point_system[idx]} $", Box(box_width*4, 5*box_height + idx * box_height, box_width, box_height), font_name="arialblack", max_font_size=50, boxcolor1=GOLD_COLOR)
        else:
            box_with_text(Screen, f"{point_system[idx]} $", Box(box_width*4, 5*box_height + idx * box_height, box_width, box_height), font_name="arialblack", max_font_size=50)


def shot_counter(SCREEN: pygame.Surface, WIDTH: int, HEIGHT: int) -> None:
    vodka_image(SCREEN, WIDTH - 60, 10, (50, 50))
    box_with_text(SCREEN, str(SHOT_COUNTER), Box(WIDTH - 60, 60, 50, 50), font_name="arialblack", max_font_size=50)
def beer_counter(SCREEN: pygame.Surface, WIDTH: int, HEIGHT: int) -> None:
    beer_image(SCREEN, WIDTH - 60 - 60, 10, (50, 50))
    box_with_text(SCREEN, str(BEER_COUNTER), Box(WIDTH - 60 - 60 , 60, 50, 50), font_name="arialblack", max_font_size=50)

def end_game_window() -> None:
    default_background(SCREEN, background_image_url, WIDTH, HEIGHT)
    box_with_text(SCREEN, f"Du vandt {SCORE} $", Box(WIDTH/4, HEIGHT/4, WIDTH/2, HEIGHT/6), font_name="arialblack", max_font_size=50)
    box_with_text(SCREEN, f"DU TOG {SHOT_COUNTER} SHOTS", Box(WIDTH/4, HEIGHT/4 + HEIGHT/4, WIDTH/2, HEIGHT/6), font_name="arialblack", max_font_size=50)
    box_with_text(SCREEN, f"DU DRAK {BEER_COUNTER} ØL", Box(WIDTH/4, HEIGHT/4 + 2*HEIGHT/4, WIDTH/2, HEIGHT/6), font_name="arialblack", max_font_size=50)
    exit()
    

def end_game_controls(screen: pygame.Surface, pos: callable):
    global EXITBOX, WINDOW, UPDATE_BACKGROUND
    global SCORE, SHOT_COUNTER, BEER_COUNTER
    (x, y) = pos[1]
    event = pos[0]
    if EXITBOX.contains_point(point = (x, y)):
        box_with_text(screen, "Exit", EXITBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=RED_COLOR)
    else:
        box_with_text(screen, "Exit", EXITBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
    if event == pygame.MOUSEBUTTONDOWN:
        if EXITBOX.contains_point(point = (x, y)):
            UPDATE_BACKGROUND = True
            SCORE = 0
            BEER_COUNTER = 0
            SHOT_COUNTER = 0
            WINDOW = "MENU"
    


def game_window():
    global SHOT_COUNTER, BEER_COUNTER, SCORE
    global FIFTY_FIFTY, CALL_FRIEND, ASK_AUDIENCE, REMOVE_ANSWER
    global SCREEN, WIDTH, HEIGHT, GAME_ON
    global EXITBOX, SOUNDONBOX, WINDOW, UPDATE_BACKGROUND
    current_game = games[CURRENT_GAME]
    questions_and_answers = [[q['question'], q['answers']] for q in current_game['questions']]
    GAME_ON = True
    LEAVE_GAME_QUESTION = False
    GAME_END_QUESTION = False
    question_idx = 0
    answered = 0
    question_count = len(questions_and_answers)
    points = 0
    point_system = [100,200,300,500,1000,2000,4000,8000,16000,32000,64000,
                    125000,250000,500000,1000000,2000000,4000000,8000000,
                    16000000,32000000]
    save_point_idx= [5,10,15]
    while GAME_ON:
        has_question_been_answered = False
        question = questions_and_answers[question_idx][0]
        answers = questions_and_answers[question_idx][1]
        answer_idx = answers[0]
        random.shuffle(answers)
        answer_idx = answers.index(answer_idx)
        draw_question_box(SCREEN, question , question_idx + 1)
        draw_answer_squares(SCREEN, answers)
        #------------- Draw Points -------------#
        point_window(SCREEN, WIDTH, HEIGHT, question_idx)
        draw_help_boxes(SCREEN, WIDTH, HEIGHT)
        available_answers_idx = [0,1,2,3]
        shot_counter(SCREEN, WIDTH, HEIGHT)
        beer_counter(SCREEN, WIDTH, HEIGHT)

        while not has_question_been_answered:
            CLOCK.tick(60)
            #------------- Background -------------#
            if question_idx in save_point_idx:
                save_point_idx.pop(0)
                LEAVE_GAME_QUESTION = True
                while LEAVE_GAME_QUESTION:
                    box_with_text(SCREEN, "Vil du tage pengene?", Box(WIDTH/4, HEIGHT/4, WIDTH/2, HEIGHT/4), font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GRAY_COLOR)
                    YESBOX = Box(WIDTH/4, HEIGHT/4 + HEIGHT/4, WIDTH/4, HEIGHT/4)
                    NOBOX = Box(WIDTH/4 + WIDTH/4, HEIGHT/4 + HEIGHT/4, WIDTH/4, HEIGHT/4)
                    mouse_input = mouse_position()
                    (x, y) = mouse_input[1]
                    event = mouse_input[0]
                    if YESBOX.contains_point(point = (x, y)):
                        box_with_text(SCREEN, "Ja", YESBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
                    else:
                        box_with_text(SCREEN, "Ja", YESBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GREEN_COLOR)
                    if NOBOX.contains_point(point = (x, y)):
                        box_with_text(SCREEN, "Nej", NOBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
                    else:
                        box_with_text(SCREEN, "Nej", NOBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=RED_COLOR)
                    if event == pygame.MOUSEBUTTONDOWN:
                        if YESBOX.contains_point(point = (x, y)):
                            LEAVE_GAME_QUESTION = False
                            GAME_ON = False
                            has_question_been_answered = True
                        elif NOBOX.contains_point(point = (x, y)):
                            LEAVE_GAME_QUESTION = False
                            default_background(SCREEN, background_image_url, WIDTH, HEIGHT)
                            draw_question_box(SCREEN, question , question_idx + 1)
                            draw_answer_squares(SCREEN, answers)
                            point_window(SCREEN, WIDTH, HEIGHT, question_idx)
                            draw_help_boxes(SCREEN, WIDTH, HEIGHT)
                            shot_counter(SCREEN, WIDTH, HEIGHT)
                            beer_counter(SCREEN, WIDTH, HEIGHT)
                            break
                    
                    
                    pygame.display.flip()
                    sound_image(SCREEN, SOUNDONBOX, SOUNDON)


            #------------- Controls -------------#
            mouse_input = mouse_position()
            (x, y) = mouse_input[1]
            event = mouse_input[0]
            #ANSWER A
            if ANSWERBOX1.contains_point(point = (x, y)) and (0 in available_answers_idx): box_with_text(SCREEN,"A: " + answers[0], ANSWERBOX1, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR, max_font_size=35)
            elif (0 in available_answers_idx): box_with_text(SCREEN, "A: " + answers[0], ANSWERBOX1, font_name="arialblack", max_font_size=35, boxcolor1=(41, 112, 227), boxcolor2=(3, 35, 87))
            else: box_with_text(SCREEN, "A: REMOVED", ANSWERBOX1, font_name="arialblack", max_font_size=35, boxcolor1=RED_COLOR)
            #ANSWER B
            if ANSWERBOX2.contains_point(point = (x, y)) and (1 in available_answers_idx): box_with_text(SCREEN, "B: " +answers[1], ANSWERBOX2, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR, max_font_size=35)
            elif (1 in available_answers_idx): box_with_text(SCREEN, "B: " +answers[1], ANSWERBOX2, font_name="arialblack", max_font_size=35, boxcolor1=(41, 112, 227), boxcolor2=(3, 35, 87))
            else: box_with_text(SCREEN, "B: REMOVED", ANSWERBOX2, font_name="arialblack", max_font_size=35, boxcolor1=RED_COLOR)
            #ANSWER C
            if ANSWERBOX3.contains_point(point = (x, y)) and (2 in available_answers_idx): box_with_text(SCREEN, "C: "  +answers[2], ANSWERBOX3, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR, max_font_size=35)
            elif (2 in available_answers_idx): box_with_text(SCREEN, "C: "  +answers[2], ANSWERBOX3, font_name="arialblack", max_font_size=35, boxcolor1=(41, 112, 227), boxcolor2=(3, 35, 87))
            else: box_with_text(SCREEN, "C: REMOVED", ANSWERBOX3, font_name="arialblack", max_font_size=35, boxcolor1=RED_COLOR)
            #ANSWER D
            if ANSWERBOX4.contains_point(point = (x, y)) and (3 in available_answers_idx):box_with_text(SCREEN, "D: " +answers[3], ANSWERBOX4, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR, max_font_size=35)
            elif (3 in available_answers_idx): box_with_text(SCREEN, "D: " +answers[3], ANSWERBOX4, font_name="arialblack", max_font_size=35, boxcolor1=(41, 112, 227), boxcolor2=(3, 35, 87))
            else: box_with_text(SCREEN, "D: REMOVED", ANSWERBOX4, font_name="arialblack", max_font_size=35, boxcolor1=RED_COLOR)
            
            #------------- Controls HELPER FUNCTIONS -------------#
            if HELPERBOX1.contains_point(point = (x, y)) and FIFTY_FIFTY: box_with_text(SCREEN, "50/50", HELPERBOX1, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR, max_font_size=50)
            elif FIFTY_FIFTY: box_with_text(SCREEN, "50/50", HELPERBOX1, font_name="arialblack", max_font_size=50, boxcolor1=GREEN_COLOR)
            else: box_with_text(SCREEN, "50/50", HELPERBOX1, font_name="arialblack", max_font_size=50, boxcolor1=RED_COLOR)
           
            if HELPERBOX2.contains_point(point = (x, y)) and CALL_FRIEND: box_with_text(SCREEN, "Ring en ven", HELPERBOX2, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR, max_font_size=50)
            elif CALL_FRIEND: box_with_text(SCREEN, "Ring en ven", HELPERBOX2, font_name="arialblack", max_font_size=50, boxcolor1=GREEN_COLOR)
            else: box_with_text(SCREEN, "Ring en ven", HELPERBOX2, font_name="arialblack", max_font_size=50, boxcolor1=RED_COLOR)
            
            if HELPERBOX3.contains_point(point = (x, y)) and ASK_AUDIENCE: box_with_text(SCREEN, "Spørg publikum", HELPERBOX3, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR, max_font_size=50)
            elif ASK_AUDIENCE: box_with_text(SCREEN, "Spørg publikum", HELPERBOX3, font_name="arialblack", max_font_size=50, boxcolor1=GREEN_COLOR)
            else: box_with_text(SCREEN, "Spørg publikum", HELPERBOX3, font_name="arialblack", max_font_size=50, boxcolor1=RED_COLOR)
            
            if HELPERBOX4.contains_point(point = (x, y)) and REMOVE_ANSWER: box_with_text(SCREEN, "Tag et shot", HELPERBOX4, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR, max_font_size=50)
            elif REMOVE_ANSWER: box_with_text(SCREEN, "Tag et shot", HELPERBOX4, font_name="arialblack", max_font_size=50, boxcolor1=GREEN_COLOR)
            else: box_with_text(SCREEN, "Tag et shot", HELPERBOX4, font_name="arialblack", max_font_size=50, boxcolor1=RED_COLOR)
            
            #------------- PUSH Controls -------------#
            if event == pygame.MOUSEBUTTONDOWN:
                if ANSWERBOX1.contains_point(point = (x, y)):
                    if answer_idx == 0:
                        SCORE = point_system[question_idx]
                        has_question_been_answered = True
                    else:
                        available_answers_idx.remove(0)
                        GAME_END_QUESTION = True
                        while GAME_END_QUESTION:
                            default_background(SCREEN, background_image_url, WIDTH, HEIGHT)
                            box_with_text(SCREEN, "Du tabte... MEN! Du har nu muligheden for at fortsætte... Du skal bare bunde en øl :^)", Box(WIDTH/4, HEIGHT/4, WIDTH/2, HEIGHT/4), font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GRAY_COLOR)
                            YESBOX = Box(WIDTH/4, HEIGHT/4 + HEIGHT/4, WIDTH/4, HEIGHT/4)
                            NOBOX = Box(WIDTH/4 + WIDTH/4, HEIGHT/4 + HEIGHT/4, WIDTH/4, HEIGHT/4)
                            mouse_input = mouse_position()
                            (x, y) = mouse_input[1]
                            event = mouse_input[0]

                            if YESBOX.contains_point(point = (x, y)): box_with_text(SCREEN, "TABER!", YESBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
                            else: box_with_text(SCREEN, "TABER!", YESBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=RED_COLOR)
                            if NOBOX.contains_point(point = (x, y)): box_with_text(SCREEN, "BUND!", NOBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
                            else: box_with_text(SCREEN, "BUND!", NOBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GREEN_COLOR)
                            
                            if event == pygame.MOUSEBUTTONDOWN:
                                if YESBOX.contains_point(point = (x, y)):
                                    GAME_END_QUESTION = False
                                    GAME_ON = False
                                    has_question_been_answered = True
                                elif NOBOX.contains_point(point = (x, y)):
                                    GAME_END_QUESTION = False
                                    BEER_COUNTER+=1
                                    default_background(SCREEN, background_image_url, WIDTH, HEIGHT)
                                    draw_question_box(SCREEN, question , question_idx)
                                    draw_answer_squares(SCREEN, answers)
                                    point_window(SCREEN, WIDTH, HEIGHT, question_idx)
                                    draw_help_boxes(SCREEN, WIDTH, HEIGHT)
                                    shot_counter(SCREEN, WIDTH, HEIGHT)
                                    beer_counter(SCREEN, WIDTH, HEIGHT)
                            pygame.display.flip()
                        continue
                        
                if ANSWERBOX2.contains_point(point = (x, y)):
                    if answer_idx == 1:
                        SCORE = point_system[question_idx]
                        has_question_been_answered = True
                    else:
                        available_answers_idx.remove(1)
                        GAME_END_QUESTION = True
                        while GAME_END_QUESTION:
                            default_background(SCREEN, background_image_url, WIDTH, HEIGHT)
                            box_with_text(SCREEN, "Du tabte... MEN! Du har nu muligheden for at fortsætte... Du skal bare bunde en øl :^)", Box(WIDTH/4, HEIGHT/4, WIDTH/2, HEIGHT/4), font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GRAY_COLOR)
                            YESBOX = Box(WIDTH/4, HEIGHT/4 + HEIGHT/4, WIDTH/4, HEIGHT/4)
                            NOBOX = Box(WIDTH/4 + WIDTH/4, HEIGHT/4 + HEIGHT/4, WIDTH/4, HEIGHT/4)
                            mouse_input = mouse_position()
                            (x, y) = mouse_input[1]
                            event = mouse_input[0]

                            if YESBOX.contains_point(point = (x, y)): box_with_text(SCREEN, "TABER!", YESBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
                            else: box_with_text(SCREEN, "TABER!", YESBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=RED_COLOR)
                            if NOBOX.contains_point(point = (x, y)): box_with_text(SCREEN, "BUND!", NOBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
                            else: box_with_text(SCREEN, "BUND!", NOBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GREEN_COLOR)
                            
                            if event == pygame.MOUSEBUTTONDOWN:
                                if YESBOX.contains_point(point = (x, y)):
                                    GAME_END_QUESTION = False
                                    GAME_ON = False
                                    has_question_been_answered = True
                                elif NOBOX.contains_point(point = (x, y)):
                                    BEER_COUNTER+=1
                                    GAME_END_QUESTION = False
                                    default_background(SCREEN, background_image_url, WIDTH, HEIGHT)
                                    draw_question_box(SCREEN, question , question_idx)
                                    draw_answer_squares(SCREEN, answers)
                                    point_window(SCREEN, WIDTH, HEIGHT, question_idx)
                                    draw_help_boxes(SCREEN, WIDTH, HEIGHT)
                                    shot_counter(SCREEN, WIDTH, HEIGHT)
                                    beer_counter(SCREEN, WIDTH, HEIGHT)
                            pygame.display.flip()
                        continue
                if ANSWERBOX3.contains_point(point = (x, y)):
                    if answer_idx == 2:
                        has_question_been_answered = True
                        SCORE = point_system[question_idx]
                    else:
                        available_answers_idx.remove(2)
                        GAME_END_QUESTION = True
                        while GAME_END_QUESTION:
                            default_background(SCREEN, background_image_url, WIDTH, HEIGHT)
                            box_with_text(SCREEN, "Du tabte... MEN! Du har nu muligheden for at fortsætte... Du skal bare bunde en øl :^)", Box(WIDTH/4, HEIGHT/4, WIDTH/2, HEIGHT/4), font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GRAY_COLOR)
                            YESBOX = Box(WIDTH/4, HEIGHT/4 + HEIGHT/4, WIDTH/4, HEIGHT/4)
                            NOBOX = Box(WIDTH/4 + WIDTH/4, HEIGHT/4 + HEIGHT/4, WIDTH/4, HEIGHT/4)
                            mouse_input = mouse_position()
                            (x, y) = mouse_input[1]
                            event = mouse_input[0]

                            if YESBOX.contains_point(point = (x, y)): box_with_text(SCREEN, "TABER!", YESBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
                            else: box_with_text(SCREEN, "TABER!", YESBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=RED_COLOR)
                            if NOBOX.contains_point(point = (x, y)): box_with_text(SCREEN, "BUND!", NOBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
                            else: box_with_text(SCREEN, "BUND!", NOBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GREEN_COLOR)
                            
                            if event == pygame.MOUSEBUTTONDOWN:
                                if YESBOX.contains_point(point = (x, y)):
                                    GAME_END_QUESTION = False
                                    GAME_ON = False
                                    has_question_been_answered = True
                                elif NOBOX.contains_point(point = (x, y)):
                                    BEER_COUNTER+=1
                                    GAME_END_QUESTION = False
                                    default_background(SCREEN, background_image_url, WIDTH, HEIGHT)
                                    draw_question_box(SCREEN, question , question_idx)
                                    draw_answer_squares(SCREEN, answers)
                                    point_window(SCREEN, WIDTH, HEIGHT, question_idx)
                                    draw_help_boxes(SCREEN, WIDTH, HEIGHT)
                                    shot_counter(SCREEN, WIDTH, HEIGHT)
                                    beer_counter(SCREEN, WIDTH, HEIGHT)
                            pygame.display.flip()
                        continue
                if ANSWERBOX4.contains_point(point = (x, y)):
                    if answer_idx == 3:
                        has_question_been_answered = True
                        SCORE = point_system[question_idx]
                    else:
                        available_answers_idx.remove(3)
                        GAME_END_QUESTION = True
                        while GAME_END_QUESTION:
                            default_background(SCREEN, background_image_url, WIDTH, HEIGHT)
                            box_with_text(SCREEN, "Du tabte... MEN! Du har nu muligheden for at fortsætte... Du skal bare bunde en øl :^)", Box(WIDTH/4, HEIGHT/4, WIDTH/2, HEIGHT/4), font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GRAY_COLOR)
                            YESBOX = Box(WIDTH/4, HEIGHT/4 + HEIGHT/4, WIDTH/4, HEIGHT/4)
                            NOBOX = Box(WIDTH/4 + WIDTH/4, HEIGHT/4 + HEIGHT/4, WIDTH/4, HEIGHT/4)
                            mouse_input = mouse_position()
                            (x, y) = mouse_input[1]
                            event = mouse_input[0]

                            if YESBOX.contains_point(point = (x, y)): box_with_text(SCREEN, "TABER!", YESBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
                            else: box_with_text(SCREEN, "TABER!", YESBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=RED_COLOR)
                            if NOBOX.contains_point(point = (x, y)): box_with_text(SCREEN, "BUND!", NOBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
                            else: box_with_text(SCREEN, "BUND!", NOBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=GREEN_COLOR)
                            
                            if event == pygame.MOUSEBUTTONDOWN:
                                if YESBOX.contains_point(point = (x, y)):
                                    GAME_END_QUESTION = False
                                    GAME_ON = False
                                    has_question_been_answered = True
                                elif NOBOX.contains_point(point = (x, y)):
                                    BEER_COUNTER+=1
                                    GAME_END_QUESTION = False
                                    default_background(SCREEN, background_image_url, WIDTH, HEIGHT)
                                    draw_question_box(SCREEN, question , question_idx)
                                    draw_answer_squares(SCREEN, answers)
                                    point_window(SCREEN, WIDTH, HEIGHT, question_idx)
                                    draw_help_boxes(SCREEN, WIDTH, HEIGHT)
                                    shot_counter(SCREEN, WIDTH, HEIGHT)
                                    beer_counter(SCREEN, WIDTH, HEIGHT)
                            pygame.display.flip()
                        continue
                #------------- PUSH Controls - HELPERBOX -------------#
                if HELPERBOX1.contains_point(point = (x, y)) and FIFTY_FIFTY:
                    if len(available_answers_idx) > 2:
                        FIFTY_FIFTY = False
                        available_answers_idx = FITTYFITTY(available_answers_idx, answer_idx)
                    else:
                        continue
                if HELPERBOX2.contains_point(point = (x, y)) and CALL_FRIEND:
                    CALL_FRIEND = False
                if HELPERBOX3.contains_point(point = (x, y)) and ASK_AUDIENCE:
                    ASK_AUDIENCE = False
                if HELPERBOX4.contains_point(point = (x, y)) and REMOVE_ANSWER:
                    available_answers_idx = TAKE_SHOT(available_answers_idx, answer_idx)
                    SHOT_COUNTER += 1
                    shot_counter(SCREEN, WIDTH, HEIGHT)
                    print(available_answers_idx)
            pygame.display.flip()

            sound_image(SCREEN, SOUNDONBOX, SOUNDON)
        
        
        question_idx += 1
        answered += 1

        if answered >= question_count:
            GAME_ON = False
    
    # game_controls(SCREEN, mouse_position)
        # WINDOW = "MENU"
        # UPDATE_BACKGROUND = True    

    WINDOW = "END_GAME"

        # draw_question_box(SCREEN, "Hvad er en hund?",2)
        # draw_answer_squares(SCREEN, ["Hund", "Kat", "Fisk", "Hest"])
    # vodka_image(SCREEN, 100, 100, (100, 100))

def game_controls(screen: pygame.Surface, pos: callable) -> None:
    global WINDOW, UPDATE_BACKGROUND, RUNNING, SOUNDON
    mouse_input = pos
    (x, y) = mouse_input[1]
    event = mouse_input[0]
    if EXITBOX.contains_point(point = (x, y)):
        box_with_text(screen, "EXIT", EXITBOX, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
    
    if event == pygame.MOUSEBUTTONDOWN:
        if EXITBOX.contains_point(point = (x, y)):
            WINDOW = "MENU"
            UPDATE_BACKGROUND = True
            print("Going to Menu")
            return True
        elif SOUNDONBOX.contains_point(point = (x, y)):
            SOUNDON = not SOUNDON
            UPDATE_BACKGROUND = True    
            return True    
    if event == pygame.QUIT:
        RUNNING = False
        print("Quitting Game")

def exit():
    global SCREEN, WIDTH, HEIGHT, EXITBOX
    box_with_text(SCREEN, "EXIT", EXITBOX, font_name="arialblack", max_font_size=50, color = WHITE_COLOR, boxcolor1=RED_COLOR)

def advanched_rules_controls(screen: pygame.Surface, pos: callable):
    """
    This function will control the menu window
    """
    global WINDOW, UPDATE_BACKGROUND, RUNNING, ADVANCED_HEADER_UPDATE, SOUNDON
    global FIFTY_FIFTY, REMOVE_ANSWER, CALL_FRIEND, ASK_AUDIENCE
    mouse_input = pos
    (x, y) = mouse_input[1]
    event = mouse_input[0]
    if EXITBOX.contains_point(point = (x, y)):
        box_with_text(screen, "EXIT", EXITBOX, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
    if event == pygame.QUIT:
        RUNNING = False
        print("Quitting Game")
    if RULEBOX_50_50.contains_point(point = (x, y)):
        box_with_text(screen, "50/50", RULEBOX_50_50, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR,max_font_size=30)
    if RULEBOX_REMOVE_ANSWER.contains_point(point = (x, y)):
        box_with_text(screen, "Fjern svarmulighed", RULEBOX_REMOVE_ANSWER, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR,max_font_size=30)
    if RULEBOX_CALL_FRIEND.contains_point(point = (x, y)):
        box_with_text(screen, "Ring en ven", RULEBOX_CALL_FRIEND, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR,max_font_size=30)
    if RULEBOX_ASK_AUDIENCE.contains_point(point = (x, y)):
        box_with_text(screen, "Spørg publikum", RULEBOX_ASK_AUDIENCE, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR,max_font_size=30)
    if event == pygame.MOUSEBUTTONDOWN:
        if EXITBOX.contains_point(point = (x, y)):
            WINDOW = "MENU"
            UPDATE_BACKGROUND = True
            ADVANCED_HEADER_UPDATE = True
            print("Heading to Menu")
        elif SOUNDONBOX.contains_point(point = (x, y)):
            SOUNDON = not SOUNDON
            UPDATE_BACKGROUND = True
            ADVANCED_HEADER_UPDATE = True          
        elif RULEBOX_50_50.contains_point(point = (x, y)):
            FIFTY_FIFTY = not FIFTY_FIFTY
        elif RULEBOX_REMOVE_ANSWER.contains_point(point = (x, y)):
            REMOVE_ANSWER = not REMOVE_ANSWER
        elif RULEBOX_CALL_FRIEND.contains_point(point = (x, y)):
            CALL_FRIEND = not CALL_FRIEND
        elif RULEBOX_ASK_AUDIENCE.contains_point(point = (x, y)):
            ASK_AUDIENCE = not ASK_AUDIENCE 


def settings_controls(screen: pygame.Surface, pos: callable) -> None:
    """
    This function will control the menu window
    """
    global WINDOW, UPDATE_BACKGROUND, RUNNING, CURRENT_GAME, SETTINGS_HEADER_UPDATE, SOUNDON
    boxes = [SETTINGSBOX1, SETTINGSBOX2, SETTINGSBOX3,SETTINGSBOX4,SETTINGSBOX5,SETTINGSBOX6,SETTINGSBOX7]
    mouse_input = pos
    (x, y) = mouse_input[1]
    event = mouse_input[0]
    boxes_count = len(games.keys())
    for idx in range(boxes_count):
        if boxes[idx].contains_point(point = (x, y)):
            box_with_text(screen, list(games.keys())[idx], boxes[idx], font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
    if EXITBOX.contains_point(point = (x, y)):
        box_with_text(screen, "EXIT", EXITBOX, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
    if event == pygame.QUIT:
        RUNNING = False
        print("Quitting Game")
    if event == pygame.MOUSEBUTTONDOWN:
        for idx in range(boxes_count):
            if boxes[idx].contains_point(point = (x, y)):
                CURRENT_GAME = list(games.keys())[idx]
                print(f"Chosen Game: {CURRENT_GAME}")
        if EXITBOX.contains_point(point = (x, y)):
            WINDOW = "MENU"
            UPDATE_BACKGROUND = True
            SETTINGS_HEADER_UPDATE = True
            print("Heading to Menu")
        elif SOUNDONBOX.contains_point(point = (x, y)):
            SOUNDON = not SOUNDON
            UPDATE_BACKGROUND = True
            SETTINGS_HEADER_UPDATE = True   


def menu_controls(screen: pygame.Surface, pos: callable, MenuBox: tuple[Box,Box,Box]) -> None:
    """
    This function will control the menu window
    """
    global WINDOW, UPDATE_BACKGROUND, RUNNING, SOUNDON, MENU_HEADER_UPDATE
    mouse_input = pos
    (x, y) = mouse_input[1]
    event = mouse_input[0]
    if MenuBox[0].contains_point(point = (x, y)):
        box_with_text(screen, "Start Game", MenuBox[0], font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
    if MenuBox[1].contains_point(point =(x, y)):
        box_with_text(screen, "Rules and Game Settings", MenuBox[1], font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
    if MenuBox[2].contains_point(point =(x, y)):
        box_with_text(screen, "Advanced Rules", MenuBox[2], font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
    if EXITBOX.contains_point(point = (x, y)):
        box_with_text(screen, "EXIT", EXITBOX, font_name="arialblack", color = WHITE_COLOR, boxcolor1=GOLD_COLOR)
    if event == pygame.MOUSEBUTTONDOWN:
        if MenuBox[0].contains_point(point = (x, y)):
            WINDOW = "GAME"
            UPDATE_BACKGROUND = True
            MENU_HEADER_UPDATE = True
            print("Heading to Start Game")
        elif MenuBox[1].contains_point(point = (x, y)):
            WINDOW = "SETTINGS"
            UPDATE_BACKGROUND = True
            MENU_HEADER_UPDATE = True
            print("Heading to Settings")
        elif MenuBox[2].contains_point(point = (x, y)):
            WINDOW = "ADVANCED_RULES"
            UPDATE_BACKGROUND = True
            MENU_HEADER_UPDATE = True
            print("Heading to Advanced Game Rules")
        elif EXITBOX.contains_point(point = (x, y)):
            RUNNING = False
            print("Quitting Game")
        elif SOUNDONBOX.contains_point(point = (x, y)):
            SOUNDON = not SOUNDON
            UPDATE_BACKGROUND = True
            MENU_HEADER_UPDATE = True            
    if event == pygame.QUIT:
        RUNNING = False
        print("Quitting Game")

# Map window names to their corresponding functions
window_functions = {
    "MENU": menu_window,
    "GAME": game_window,
    "SETTINGS": settings_window,
    "ADVANCED_RULES": advanced_rules_window,
    "END_GAME": end_game_window
}
window_controls = {
    "MENU": lambda: menu_controls(SCREEN, mouse_position(), (MENUBOX1, MENUBOX2, MENUBOX3)),
    "GAME": lambda: None,  # Placeholder
    "SETTINGS": lambda: settings_controls(SCREEN, mouse_position()),  # Placeholder
    "ADVANCED_RULES": lambda: advanched_rules_controls(SCREEN, mouse_position()),  # Placeholder
    "END_GAME": lambda: end_game_controls(SCREEN, mouse_position())
}

while RUNNING:

    if UPDATE_BACKGROUND:
        print("Updating Background")
        default_background(SCREEN, background_image_url, WIDTH, HEIGHT)
        UPDATE_BACKGROUND = False

    if WINDOW in window_functions:
        window_functions[WINDOW]()      
        window_controls[WINDOW]()
    sound_image(SCREEN, SOUNDONBOX, SOUNDON)
    pygame.display.flip()   #Update Screen
    CLOCK.tick(60)          #Frame Rate

pygame.quit()