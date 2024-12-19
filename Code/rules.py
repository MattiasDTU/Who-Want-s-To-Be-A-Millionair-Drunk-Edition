import pygame
from components import Box, exit, render_text, render_multiline_text, render
from screen import background
from events import mouse_position, AreaHover
from colors import *


def rules_title(screen: pygame.Surface, width: int, height: int, ACTIVE_GAME: str = None) -> None:
    header_text1 = render("Rules and Game", 50, font="arialblack" , color = WHITE_COLOR)
    screen.blit(header_text1, (width/2 - header_text1.get_width()/2, height/20))
    
    if ACTIVE_GAME == None:
        under_header_text = render("You Must Choose A Game Before Starting", 50, font="arialblack" , color = GOLD_COLOR)
        screen.blit(under_header_text, (width/2 - under_header_text.get_width()/2, height/20 + under_header_text.get_height()))



def rules_text_box(screen: pygame.Surface, width: int, height: int) -> None:
    """
    
    :param screen: Pygame screen to draw on.
    :param width: width of screen.
    :param height: height of screen.
    
    """

    #----------- Settings text box -----------#
    text_box = pygame.Surface((width/2,height/2), pygame.SRCALPHA)
    text_box.fill((0, 0, 255, 125))
    pygame.draw.rect(text_box, BLUE_COLOR, (0, 0, width/2 ,height/2), width = 10)
    screen.blit(text_box, (width/4, height/4))    # Draw Transparet Box
    rules_text = """|-------------- Information --------------|
    - You can add your own questions to the game by creating a custom excel file, but you must follow the same format as the original file.
    - You must choose a game before starting.
    
    |-------------- Rules --------------|
    1. You must answer all questions to win the final prize.
    2. For every 5 answer correct, you get a guaranteed prize.
    3. You can use 4 lifelines: 50/50, Phone a friend, Ask the audience, and Remove a wrong answer.
    4. The Fourth lifeline "Remove a wrong answer" is enabled by taking a shot (Can be used multiple times).
    5. You can only leave the game with the prize you have secured, and not while answering a question.
    6. Answering wrong will leave you with two options: Leave with guaranteed prize or down a beer to continue."""
    render_multiline_text(screen, rules_text, "arial", WHITE_COLOR,
    pygame.Rect(10+width / 4, height / 4 + 10, width / 4, height / 2- 15))


def RulesBoxes(width: int, height: int, GAMES: dict) -> list[Box]:
    """
    Create the boxes for the rules window.
    :param width: int, The width of the screen.
    :param height: int, The height of the screen.
    :return: list[Box], A list of Box objects for the rules window.
    """
    RuleBoxes = []
    for idx, name in enumerate(GAMES):
        RuleBoxes.append(Box(2* width / 4, height / 4 + 15 + idx * (50 + 5), width / 4 - 10, 50, name))
    RuleBoxes.append(exit())
    return RuleBoxes

def rules(screen: pygame.Surface, width: int, height: int, CURRENT_GAME: str, GAMES: list[str]) -> str:
    """
    Display the rules window on the screen.
    :param screen: pygame.Surface, The surface where the rules will be drawn.
    :param width: int, The width of the screen.
    :param height: int, The height of the screen.
    :param CURRENT_GAME: str, The currently selected game.
    :param GAMES: list[str], A list of available games.
    """
    boxes = RulesBoxes(width, height, GAMES)    #Create Menu Boxes
    RULESON = True   # Main menu loop flag
    PrevPos = None  # Previous position of the mouse
    UPDATE = True
    while RULESON: # Main menu loop
        pygame.display.flip()               # Update screen
        event, pos = mouse_position()       # Continously check for mouse position and events
        CurrentPos = AreaHover(boxes, pos)  # Continously check for mouse hover
        if UPDATE:
            background(screen, "images/background_image.jpg", width, height)
            rules_text_box(screen, width, height)
            rules_title(screen, width, height, CURRENT_GAME)
            for box in boxes: # Draw all the boxes
                if box.text == CURRENT_GAME:
                    box.draw_box(screen, hover = True, font = "arialback", font_size=80)
                else:
                    box.draw_box(screen, hover = False, font = "arialback", font_size=80)
            UPDATE = False

        if CurrentPos != PrevPos: # Continous
            # Only activates if the mouse is moved from an area.
            if PrevPos is not None: # Updates Prev Area Box
                if PrevPos.text == CURRENT_GAME:
                    HoverOn = True
                else:
                    HoverOn = False
                PrevPos.draw_box(screen, hover = HoverOn, font = "arialback", font_size=80)
            if CurrentPos is not None: # Updates Current Area Box
                CurrentPos.draw_box(screen, hover = True, font = "arialback", font_size=80)
            PrevPos = CurrentPos # Updates Prev Area Box
        
        
        # --- Event Handling --- #
        if event == pygame.MOUSEBUTTONDOWN and CurrentPos is not None:
            if CurrentPos.text == "EXIT":
                RULESON = False
            else:
                if CURRENT_GAME == None:
                    UPDATE = True
                CURRENT_GAME = CurrentPos.text # Update the current game
                for box in boxes: # Draw all the boxes
                    if box.text == CURRENT_GAME:
                        box.draw_box(screen, hover = True, font = "arialback", font_size=80)
                    else:
                        box.draw_box(screen, hover = False, font = "arialback", font_size=80)      
        if event == pygame.QUIT:
            RULESON = False
    return CURRENT_GAME