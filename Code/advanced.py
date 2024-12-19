import pygame
from components import Box, exit, render_text, render_multiline_text, render
from screen import background
from events import mouse_position, AreaHover
from colors import *


def AdvancedBoxes(width: int, height: int) -> list[Box]:
    AdvancedBoxes = [
    Box(width / 4 + 10, height / 4*2 + 0 * (100 + 5), width / 4 - 10, 100, "Call A Friend"),
    Box(width / 4 + 10 + width / 4 - 10, height / 4*2 + 0 * (100 + 5), width / 4 - 10, 100, "Ask The Audience"),
    Box(width / 4 + 10, height / 4*2 + 1 * (100 + 5), width / 4 - 10, 100, "50/50"),
    Box(width / 4 + 10 + width / 4 - 10, height / 4*2 + 1 * (100 + 5), width / 4 - 10, 100, "Remove One Answers"),
    exit()]
    return AdvancedBoxes


def advanced_title(screen: pygame.Surface, width: int, height: int) -> None:
    text1 = "Rules and Game Settings"
    header_text1 = render(text1, 50, font="arialblack" , color = WHITE_COLOR)
    screen.blit(header_text1, (width/2 - header_text1.get_width()/2, height/20))

def advanced_text_box(screen: pygame.Surface, width: int, height: int) -> None:
    text1 = """Please pick which lifelines you would like to remove/add."""
    rect = pygame.Rect(10+width / 4, height / 4 + 10, width / 2 - 20, height / 4)
    text_box1 = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    text_box1.fill((0, 0, 0, 0))  # Semi-transparent black
    screen.blit(text_box1, rect.topleft)

    text_box2 = pygame.Surface((width/2,height/2), pygame.SRCALPHA)
    text_box2.fill((0, 0, 255, 125))
    pygame.draw.rect(text_box2, BLUE_COLOR, (0, 0, width/2 ,height/2), width = 10)
    screen.blit(text_box2, (width/4, height/4))    # Draw Transparet Box
    screen.blit(text_box1, rect.topleft)
    render_multiline_text(screen, text1, "arialblack", WHITE_COLOR, rect, max_font_size=30)




# Box(WIDTH / 4, HEIGHT / 4, WIDTH / 4, HEIGHT / 4)
def advanced(screen: pygame.Surface, width: int, height: int, rules: tuple[bool,bool,bool,bool]) -> tuple[bool,bool,bool,bool]:
    boxes = AdvancedBoxes(width, height)    #Create Menu Boxes

    (FIFTY_FIFTY, ASK_AUDIENCE, CALL_FRIEND, REMOVE_ONE) = rules

    background(screen, "images/background_image.jpg", width, height)
    advanced_title(screen, width, height)
    advanced_text_box(screen, width, height)



    rulesnames = {
        "Call A Friend": CALL_FRIEND,
        "Ask The Audience": ASK_AUDIENCE,
        "50/50": FIFTY_FIFTY,
        "Remove One Answers": REMOVE_ONE
    }
    PrevPos = None  # Previous position of the mouse
    UPDATE = True
    for box in boxes: # Draw all the boxes
        if box.text in rulesnames:
            if rulesnames[box.text]:
                locked = 1
            else:
                locked = 2
            box.draw_box(screen, hover=False, font="arial", font_size=80, locked = locked)
        else:
            box.draw_box(screen, hover=False, font="arial", font_size=80)
    while True:
        pygame.display.flip()               # Update screen
        event, pos = mouse_position()       # Continously check for mouse position and events
        CurrentPos = AreaHover(boxes, pos)

        if (CurrentPos != PrevPos) or UPDATE:
            if UPDATE:
                pos = (0,0)
            if PrevPos is not None:
                if PrevPos.text in rulesnames:
                    if rulesnames[PrevPos.text]:
                        locked = 1
                    else:
                        locked = 2
                    PrevPos.draw_box(screen, hover=False, font="arial", font_size=80, locked = locked)
                else:
                    PrevPos.draw_box(screen, hover=False, font="arial", font_size=80)
            if CurrentPos is not None:
                CurrentPos.draw_box(screen, hover=True, font="arial", font_size=80)
            PrevPos = CurrentPos
            UPDATE = False
            locked = 0
        
        if event == pygame.MOUSEBUTTONDOWN and CurrentPos is not None:
            if CurrentPos.text == "Call A Friend":
                rulesnames["Call A Friend"] = not rulesnames["Call A Friend"]
                UPDATE = True
            elif CurrentPos.text == "Ask The Audience":
                rulesnames["Ask The Audience"] = not rulesnames["Ask The Audience"]
                UPDATE = True
            elif CurrentPos.text == "50/50":
                rulesnames["50/50"] = not rulesnames["50/50"]
                UPDATE = True
            elif CurrentPos.text == "Remove One Answers":
                rulesnames["Remove One Answers"] = not rulesnames["Remove One Answers"]
                UPDATE = True
            elif CurrentPos.text == "EXIT":
                return (rulesnames["50/50"], rulesnames["Ask The Audience"], rulesnames["Call A Friend"], rulesnames["Remove One Answers"])

    return rules