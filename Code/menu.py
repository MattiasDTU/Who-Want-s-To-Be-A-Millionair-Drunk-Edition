import pygame
from components import Box, exit, render_text, render
from screen import background
from events import mouse_position, AreaHover
from rules import rules
from advanced import advanced
from colors import *
from game import game

def MenuBoxes(width: int, height: int) -> list[Box]:
    """
    Create the boxes for the main menu.
    :param width: int, The width of the screen.
    :param height: int, The height of the screen.
    :return: list[Box], A list of Box objects for the main menu.
    """
    margin = 10
    button_width    =   (width/2 - 2 * margin) 
    button_height   =   (height/2 - 4 * margin) // 3     
    MenuBoxPlay     =   Box(width/4 + margin, height/4 + 2 * margin, button_width, button_height, "Play")                      #MenuBoxPlay
    MenuBoxRules    =   Box(width/4 + margin, height/4 + button_height + 2 * margin, button_width, button_height, "Rules")      #MenuBoxSettings
    MenuBoxSettings =   Box(width/4 + margin, height/4 + 2 * button_height + 2 * margin, button_width, button_height, "Settings")  #MenuBoxAdvanced
    return [MenuBoxPlay, MenuBoxRules, MenuBoxSettings, exit()]


def MenuUpdate(screen: pygame.Surface, width: int, height: int) -> None:
    """
    Update the main menu.
    :param screen: pygame.Surface, The surface where the menu will be drawn.
    :param width: int, The width of the screen.
    :param height: int, The height of the screen.
    """
    background(screen, "images//background_image.jpg", width, height)
    render_text(screen, "Who Want's to be a", 50, "arialblack", WHITE_COLOR, height / 20, width)
    render_text(screen, "MILLIONAIRE", 100, "arialblack", GOLD_COLOR, height / 12, width)
    

def menu(screen: pygame.Surface, width: int, height: int, GAMES: dict) -> None:
    """
    Display the main menu on the screen.
    
    :param screen: pygame.Surface, The surface where the menu will be drawn.
    :param width: int, The width of the screen.
    :param height: int, The height of the screen.
    :return: None
    """
    # ---- Game Constants ---- #
    CURRENT_GAME = None
    FIFTY_FIFTY = True
    ASK_AUDIENCE = True
    CALL_FRIEND = True
    REMOVE_ONE = True
    GAMERULES = (FIFTY_FIFTY, ASK_AUDIENCE, CALL_FRIEND, REMOVE_ONE)
    SCORE = 0


    boxes = MenuBoxes(width, height)    #Create Menu Boxes

    # Main menu loop constants
    MENUON = True   # Main menu loop flag
    PrevPos = None  # Previous position of the mouse
    UPDATE = True
    while MENUON: # Main menu loop
        event, pos = mouse_position()       # Continously check for mouse position and events
        CurrentPos = AreaHover(boxes, pos)  # Continously check for mouse hover

        if UPDATE:
            MenuUpdate(screen, width, height)
            for box in boxes: # Draw all the boxes
                box.draw_box(screen, hover = False, font = "arialback", font_size=80)
            UPDATE = False

        if CurrentPos != PrevPos: # Continous
            # Only activates if the mouse is moved from an area.
            if PrevPos is not None: # Updates Prev Area Box
                PrevPos.draw_box(screen, hover = False, font = "arialback", font_size=80)
            if CurrentPos is not None: # Updates Current Area Box
                CurrentPos.draw_box(screen, hover = True, font = "arialback", font_size=80)
            PrevPos = CurrentPos # Updates Prev Area Box
        
        # --- Event Handling --- #
        if event == pygame.MOUSEBUTTONDOWN:
            if CurrentPos is not None:
                if CurrentPos.text == "EXIT":
                    MENUON = False
                    return False
                elif CurrentPos.text == "Play":
                    UPDATE = True
                    if CURRENT_GAME == None:
                        CURRENT_GAME = rules(screen, width, height, CURRENT_GAME, GAMES.keys())
                    else:
                        SCORE = game(screen, width, height, GAMERULES, CURRENT_GAME)
                elif CurrentPos.text == "Rules":
                    UPDATE = True
                    CURRENT_GAME = rules(screen, width, height, CURRENT_GAME, GAMES.keys())
                elif CurrentPos.text == "Settings":
                    UPDATE = True
                    GAMERULES = advanced(screen, width, height, GAMERULES)
                    print("Settings")
            if event == pygame.QUIT:
                MENUON = False
                return False
    
        # Update screen and control frame rate
        pygame.display.flip()
