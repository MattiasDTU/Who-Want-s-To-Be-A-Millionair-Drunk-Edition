import pygame
from components import Box, exit, render_text, render_multiline_text, render, box_with_text
from screen import background
from events import mouse_position, AreaHover
from colors import *
from excel import GAMES
import random

def vodka_image(screen: pygame.Surface, x_cord: int, y_cord: int, size: tuple[int,int]) -> None:
    """
    This function will draw the vodka image on the screen
    """
    vodka = pygame.image.load("images//vodka.png")
    vodka = pygame.transform.scale(vodka, (size[0], size[1]))
    screen.blit(vodka, (x_cord, y_cord))


def beer_image(screen: pygame.Surface, x_cord: int, y_cord: int, size: tuple[int,int]) -> None:
    """
    This function will draw the vodka image on the screen
    """
    beer = pygame.image.load("images//beer.png")
    beer = pygame.transform.scale(beer, (size[0], size[1]))
    screen.blit(beer, (x_cord, y_cord))

def shot_counter(screen: pygame.Surface, width: int, height: int, SHOTS: int) -> None:
    vodka_image(screen, width - 60, 10, (50, 50))
    box_with_text(screen, str(SHOTS), (width - 60, 60, 50, 50), font_name="arialblack", max_font_size=50)

def beer_counter(screen: pygame.Surface, width: int, height: int, BEERS: int) -> None:
    beer_image(screen, width - 60 - 60, 10, (50, 50))
    box_with_text(screen, str(BEERS), (width - 60 - 60 , 60, 50, 50), font_name="arialblack", max_font_size=50)


def point_window_render(screen: pygame.Surface, width: int, height: int) -> None:
    box_width = width // 5
    box_height = height // 20 - 10
    point_system = [100,200,300,500,1000,2000,4000,8000,16000,32000,64000,
                    125000,250000,500000,1000000,2000000,4000000,8000000,
                    16000000,32000000]
    box_with_text(screen, "Monitos $$", (box_width*4, 4*box_height, box_width, box_height), font_name="arialblack", InnerBox=BLUE_COLOR)
    for idx in range(20):
        box_with_text(screen, f"{point_system[idx]} $", (box_width*4, 5*box_height + idx * box_height, box_width, box_height), font_name="arialblack", InnerBox=GRAY_COLOR)

def update_point_window(screen: pygame.Surface, width: int, height: int, question_idx: int) -> None:
    """
    This function will draw the points on the screen
    """
    box_width = width // 5
    box_height = height // 20 - 10
    point_system = [100,200,300,500,1000,2000,4000,8000,16000,32000,64000,
                    125000,250000,500000,1000000,2000000,4000000,8000000,
                    16000000,32000000]
    if question_idx+1 in [5,10,15]:
        color = GOLD_COLOR
    else:
        color = GREEN_COLOR
    box_with_text(screen, f"{point_system[question_idx]} $", (box_width*4, 5*box_height + question_idx * box_height, box_width, box_height), font_name="arialblack", InnerBox=color)


def continue_screen(screen, width, height):
    LEAVEGAMEQUESTION = True
    background(screen, "images//background_image.jpg", width, height)
    EndBoxes = end_game_boxes(screen, width, height)
    PrevPos = None
    for box in EndBoxes:
        box.draw_box(screen, hover = False, font = "arialblack")
    while LEAVEGAMEQUESTION:
        pygame.display.flip()
        event, pos = mouse_position()
        CurrentPos = AreaHover(EndBoxes, pos)

        if CurrentPos != PrevPos:
            if PrevPos is not None and PrevPos.text != EndBoxes[0].text:
                PrevPos.draw_box(screen, hover = False, font = "arialblack")
            if CurrentPos is not None and CurrentPos.text != EndBoxes[0].text:
                CurrentPos.draw_box(screen, hover = True, font = "arialblack")
            PrevPos = CurrentPos
        if event == pygame.MOUSEBUTTONDOWN:
            if CurrentPos is not None:
                if CurrentPos.text == "Fuck yeah! Lets keep going!":
                    LEAVEGAMEQUESTION = False
                    return True
                elif CurrentPos.text == "Fuck no, I'm Done!":
                    LEAVEGAMEQUESTION = False
                    return False
        


def end_game_boxes(screen: pygame.Surface, width: int, height: int) -> list[Box]:
        textbox = Box(width/4, height/4, width/2, height/4,"You answered Wrong!... but! You now have the opportunity to continue... All you need to do is empty a beer :^)")
        YESBOX = Box(width/4, height/4 + height/4, width/4, height/4, "Fuck yeah! Lets keep going!")
        NOBOX = Box(width/4 + width/4, height/4 + height/4, width/4, height/4, "Fuck no, I'm Done!")
        return [textbox, YESBOX, NOBOX]


def question_screen(screen: pygame.Surface, width: int, height: int, question: str, question_idx: int) -> bool:
    QUESTIONBOX = Box(width/6, 50 , 4*width/6, height/4*2, text = f"Q{question_idx} : {question}" )
    QUESTIONBOX.draw_box(screen, hover=False, font="arial", font_size=80)


def GameBoxes(screen: pygame.Surface, width: int, height: int, answers: list[str]) -> list[Box]:
    Boxes = [Box(width / 8 * 2, height / 2, width / 4, (height / 4) // 2, "A: " + answers[0]),  # top left
    Box(width / 8 * 2 + width / 4, height / 2, width / 4, (height / 4) // 2, "B: " + answers[1]),  # top right
    Box(width / 8 * 2, height / 2 + (height / 4) // 2, width / 4, (height / 4) // 2, "C: " + answers[2]),  # bottom left
    Box(width / 8 * 2 + width / 4, height / 2 + (height / 4) // 2, width / 4, (height / 4) // 2, "D: " + answers[3]),  # bottom right
    Box(width/4, height/4*3, width/8, 100, "Call A Friend") ,
    Box(width/4 + 1 * (width/8), height/4*3, width/8, 100,"Ask The Audience"),
    Box(width/4 + 2 * (width/8), height/4*3, width/8, 100,"50/50"),
    Box(width/4 + 3 * (width/8), height/4*3, width/8, 100, "Remove One Answers"),
    exit()]
    return Boxes


def TAKE_SHOT(original_list, important_value):
    """
    Generates a new list with one random value removed from the original list,
    while ensuring the important value is always included.

    :param original_list: List of elements.
    :param important_value: The value that must always be included in the new list.
    :return: A new list with one less value and the important value included.
    """
    if important_value not in original_list:
        raise ValueError("The important value is not in the original list.")
    
    # Ensure there are other values to remove
    if len(original_list) == 1 and original_list[0] == important_value:
        return original_list  # Nothing to remove

    # Get a list of candidates for removal, excluding the important value
    removable_candidates = [value for value in original_list if value != important_value]
    
    # Randomly select a value to remove
    value_to_remove = random.choice(removable_candidates)
    
    # Create a new list excluding the randomly selected value
    new_list = original_list[:]
    new_list.remove(value_to_remove)

    return new_list


def FITTYFITTY(original_list, important_value):
    """
    Generates a new list with two random values removed from the original list,
    while ensuring the important value is always included.

    :param original_list: List of elements.
    :param important_value: The value that must always be included in the new list.
    :return: A new list with two less values and the important value included.
    """
    if important_value not in original_list:
        raise ValueError("The important value is not in the original list.")
    
    # Ensure there are enough values to remove
    if len(original_list) <= 2 and important_value in original_list:
        raise ValueError("Not enough values to remove two while keeping the important value.")
    
    # Get a list of candidates for removal, excluding the important value
    removable_candidates = [value for value in original_list if value != important_value]
    
    # Randomly select two values to remove
    values_to_remove = random.sample(removable_candidates, 2)
    
    # Create a new list excluding the selected values
    new_list = original_list[:]
    for value in values_to_remove:
        new_list.remove(value)

    return new_list




def game(screen: pygame.Surface, width: int, height: int, rules: tuple[bool, bool, bool, bool], game: str, restart: bool = True) -> bool:
    """
    Display the game window on the screen.
    :param screen: pygame.Surface, The surface where the game will be drawn.
    :param width: int, The width of the screen.
    :param height: int, The height of the screen.
    :param rules: tuple[bool, bool, bool, bool], The rules of the game.
    :param game: str, The currently selected game.
    """
    if restart:
        GAMEON = True   # Main game loop flag
        PrevPos = None  # Previous position of the mouse
        UPDATE = True
        SHOTS = 0
        BEERS = 0
        SCORE = 0



        (FIFTY_FIFTY, ASK_AUDIENCE, CALL_FRIEND, REMOVE_ONE) = rules
        CurrentGame = GAMES[game]   
        QuestAndAnswers = [[q['question'], q['answers']] for q in CurrentGame['questions']]

        QuestionIdx = 0
        Answered = 0
        QuestionCount = len(QuestAndAnswers)
        print(QuestionCount)
        point_system = [100,200,300,500,1000,2000,4000,8000,16000,32000,64000,
                        125000,250000,500000,1000000,2000000,4000000,8000000,
                        16000000,32000000]
        save_point_idx= [5,10,15]

    rulesnames = {
        "Call A Friend": CALL_FRIEND,
        "Ask The Audience": ASK_AUDIENCE,
        "50/50": FIFTY_FIFTY,
        "Remove One Answers": REMOVE_ONE
    }
    point_window_render(screen, width, height)
    shot_counter(screen, width, height, SHOTS)
    beer_counter(screen,width,height, BEERS)
    while GAMEON: # Main Game Loop
        QUESTION = QuestAndAnswers[QuestionIdx][0]
        ANSWERS = QuestAndAnswers[QuestionIdx][1]
        CORRECT_ANSWER = ANSWERS[0]
        NEW_ANSWERS = ANSWERS.copy()
        random.shuffle(NEW_ANSWERS)
        # answer_idx = ANSWERS.index(CORRECT_ANSWER)
        boxes = GameBoxes(screen, width, height, NEW_ANSWERS)
        question_screen(screen, width, height, QUESTION, QuestionIdx+1)
        for box in boxes:
            if box.text in rulesnames:
                if rulesnames[box.text]:
                    locked = 1
                else:
                    locked = 2
                box.draw_box(screen, hover=False, font="arialblack", locked = locked)
            else:
                locked = 0
                box.draw_box(screen, hover=False, font="arialblack")

        QUESTIONON = True
        PrevPos = None
        UPDATE = True
        PossibleAnswerindex = [0,1,2,3]
        while QUESTIONON:
            pygame.display.flip()               # Update screen
            event, pos = mouse_position()
            CurrentPos = AreaHover(boxes, pos)

            if UPDATE:
                question_screen(screen, width, height, QUESTION, QuestionIdx+1)
                shot_counter(screen, width, height, SHOTS)
                beer_counter(screen,width,height, BEERS)
                for box in boxes:
                    if box.text in rulesnames:
                        if rulesnames[box.text]:
                            locked = 1
                        else:
                            locked = 2
                        box.draw_box(screen, hover=False, font="arialblack", locked = locked)
                    else:
                        if box.text[3:] in NEW_ANSWERS:
                            if NEW_ANSWERS.index(box.text[3:]) in PossibleAnswerindex:
                                box.draw_box(screen, hover = False, font = "arialblack")
                            else:
                                box.draw_box(screen, hover = False, font = "arialblack", locked = 2)
                        else: continue
                UPDATE = False
            

            if (CurrentPos != PrevPos):
                # Only activates if the mouse is moved from an area.
                if (PrevPos is not None) and (PrevPos.text in rulesnames):
                    if rulesnames[PrevPos.text]:
                        locked = 1
                    else:
                        locked = 2
                    PrevPos.draw_box(screen, hover=False, font="arialblack", locked = locked)
                if (CurrentPos is not None) and (CurrentPos.text in rulesnames):
                    if rulesnames[CurrentPos.text]:
                        locked = 1
                        HoverOn = True
                    else:
                        locked = 2
                        HoverOn = False
                    CurrentPos.draw_box(screen, hover = HoverOn, font = 'arialblack', locked = locked)
                
                if PrevPos is not None:
                    if PrevPos.text == "EXIT":
                        PrevPos.draw_box(screen, hover = False, font = "arialblack")
                    if PrevPos.text[3:] in NEW_ANSWERS:
                        if NEW_ANSWERS.index(PrevPos.text[3:]) in PossibleAnswerindex:
                            PrevPos.draw_box(screen, hover = False, font = "arialblack")
                        else:
                            locked = 2
                            PrevPos.draw_box(screen, hover = False, font = "arialblack", locked = locked)
                if CurrentPos is not None:
                    if CurrentPos.text == "EXIT":
                        CurrentPos.draw_box(screen, hover = True, font = "arialblack")
                    if CurrentPos.text[3:] in NEW_ANSWERS:
                        if NEW_ANSWERS.index(CurrentPos.text[3:]) in PossibleAnswerindex:
                                CurrentPos.draw_box(screen, hover = True, font = "arialblack")
                        else:
                            locked = 2
                            CurrentPos.draw_box(screen, hover = True, font = "arialblack", locked = locked)
                PrevPos = CurrentPos # Updates Prev Area Box
            
            if event == pygame.MOUSEBUTTONDOWN:
                if CurrentPos is not None:
                    if CurrentPos.text == "Call A Friend":
                        rulesnames["Call A Friend"] = not rulesnames["Call A Friend"]
                        UPDATE = True
                    elif CurrentPos.text == "Ask The Audience":
                        rulesnames["Ask The Audience"] = not rulesnames["Ask The Audience"]
                        UPDATE = True
                    elif CurrentPos.text == "50/50":
                        if rulesnames["50/50"]:
                            if len(PossibleAnswerindex) > 2:
                                rulesnames["50/50"] = not rulesnames["50/50"]
                                PossibleAnswerindex = FITTYFITTY(PossibleAnswerindex, NEW_ANSWERS.index(CORRECT_ANSWER))
                                UPDATE = True
                            else:
                                continue
                    elif CurrentPos.text == "Remove One Answers":
                        SHOTS += 1
                        PossibleAnswerindex = TAKE_SHOT(PossibleAnswerindex, NEW_ANSWERS.index(CORRECT_ANSWER))
                        UPDATE = True
                    elif CurrentPos.text == "EXIT":
                        GAMEON = False
                        QUESTIONON = False
                        return SCORE
                    elif NEW_ANSWERS.index(CurrentPos.text[3:]) in PossibleAnswerindex:
                        if CurrentPos.text[3:] == CORRECT_ANSWER:
                            SCORE = point_system[QuestionIdx]
                            update_point_window(screen, width, height, QuestionIdx)
                            QUESTIONON = False
                            Answered += 1
                            QuestionIdx += 1
                        else:
                            PossibleAnswerindex.remove(NEW_ANSWERS.index(CurrentPos.text[3:]))
                            if continue_screen(screen, width, height):
                                BEERS += 1
                            else:
                                GAMEON = False
                                # Add a endgame screen to see the scores
                                QUESTIONON = False 
                                print("Score: ",SCORE, ". Beers: ", BEERS," Shots: " , SHOTS)
                                return SCORE
                            point_window_render(screen, width, height)
                            for i in range(QuestionIdx):
                                update_point_window(screen,width,height,i)
                            UPDATE = True
                    
        if QuestionIdx == QuestionCount:
            
            print("Score: ",SCORE, ". Beers: ", BEERS," Shots: " , SHOTS)
            return SCORE

            
                