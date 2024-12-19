import pygame
from colors import *

# ----- Program Constants ----- #
TEST_MODE = True       # Flag to run in test mode
RUNNING = True         # Main game loop flag
FRAME_RATE = 60        # Frames per second



# Initialize pygame and the clock
pygame.init()
CLOCK = pygame.time.Clock()


def initialize_screen(test_mode=False, size=(1280, 720), fullscreen=False):
    """
    Initializes and returns the game screen and its dimensions.
    
    :param test_mode: bool, If True, uses the specified size. If False, uses the current display resolution.
    :param size: tuple, The default screen size for test mode (default: (1280, 720)).
    :param fullscreen: bool, If True, initializes the screen in fullscreen mode (default: False).
    :return: tuple, (screen, (width, height))
    """
    screen_size = size if test_mode else (pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen_mode = pygame.FULLSCREEN if fullscreen else 0
    screen = pygame.display.set_mode(screen_size, screen_mode)
    return screen, screen_size


def background(screen: pygame.Surface, image_url: str, width: int, height: int) -> None:
    """
    Sets and scales a background image to the specified dimensions on the game screen.
    
    :param screen: pygame.Surface, The surface where the background will be drawn.
    :param image_url: str, The file path to the background image.
    :param width: int, The desired width of the background.
    :param height: int, The desired height of the background.
    :return: None
    """
    bg_image = pygame.image.load(image_url)                       # Load the image from the file
    bg_image = pygame.transform.scale(bg_image, (width, height))  # Scale to the desired size
    screen.blit(bg_image, (0, 0))                                 # Draw the image at the top-left corner of the screen

class Box:
    """
    A class representing a rectangular box with a position, dimensions, and color.
    """
    def __init__(self, x: int, y: int, width: int, height: int, text: str = ""):
        """
        Initialize a Box object.

        :param x: The x-coordinate of the top-left corner of the box.
        :param y: The y-coordinate of the top-left corner of the box.
        :param width: The width of the box.
        :param height: The height of the box.
        :param text: The text to be displayed inside the box (default is an empty string).
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        # Compute the x and y limits (boundaries of the box)
        self.x_lim = self.x + self.width
        self.y_lim = self.y + self.height    
    def draw_box(self, screen: pygame.Surface, font: str = 'Arial', font_size: int = 50, hover: bool = False, locked: int = 0) -> None:
        """
        Draw a box on the screen.
        :param screen: pygame.Surface, The surface where the box will be drawn.
        :param text: str, The text to be displayed inside the box.
        :param font: str, The font to use for the text (default: 'Arial').
        :param hover: bool, If True, the box is being hovered over (default: False).
        :param locked: int, [0: InnerBox = (0,0,0). If 1, the box is locked (default: 0).
        """
        if hover:
            box_with_text(screen, self.text, (self.x, self.y, self.width, self.height), font_name = font,
                          text_color = BLACK_COLOR, InnerBox = GOLD_COLOR, max_font_size=font_size)
        else:
            box_with_text(screen, self.text, (self.x, self.y, self.width, self.height), font_name = font,
                          text_color = WHITE_COLOR, InnerBox = BLACK_COLOR, max_font_size=font_size)



def box_with_text(screen: pygame.Surface, text: str, cords: tuple[int,int,int,int], font_name: str="Arial", text_color: tuple[int,int,int] =(0, 0, 0),
                   InnerBox: tuple[int,int,int] = GRAY_COLOR, OuterBox: tuple[int,int,int] = BLUE_COLOR, max_font_size: int=50, line_spacing: int=5, remove: bool = False) -> None:
    """
    Draws wrapped text inside a box, automatically wrapping or scaling down the text to fit within the box.
    
    :param screen: Pygame screen to draw on.
    :param text: The text to be displayed.
    :param box: A Box object or tuple (x, y, width, height).
    :param font_name: The name of the font to use (default: Arial).
    :param color: The color of the text (default: black).
    :param max_font_size: Maximum font size to start scaling from.
    :param line_spacing: Spacing between lines of wrapped text.
    """
    # Extract box dimensions
    pygame.draw.rect(screen, InnerBox, cords, border_radius = 10)  # Button rectangle
    pygame.draw.rect(screen, OuterBox, cords, 2, border_radius = 10)  # Button border    
    
    if isinstance(cords, tuple):
        x, y, width, height = cords
    else:
        print("Error: cords must be a tuple")
        return None

    font_size = max_font_size                         # Initialize font size
    font = pygame.font.SysFont(font_name, font_size)  # Initialize font

    while font_size > 0:
        # Wrap the text
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            text_surface = font.render(test_line, True, text_color)
            if text_surface.get_width() > width:  # if text exceeds the box width
                if current_line:  # Push the current line to lines
                    lines.append(current_line.strip())
                current_line = word + " "
            else: # if text fits in the box
                current_line = test_line

        if current_line:
            lines.append(current_line.strip())

        # Calculate total text height
        total_text_height = len(lines) * (font.size("Tg")[1] + line_spacing)

        # Check if the wrapped text fits in the box
        if total_text_height <= height:
            break

        # Reduce font size if it doesn't fit
        font_size -= 1
        font = pygame.font.SysFont(font_name, font_size)

    if font_size <= 0:
        raise ValueError("Text is too large to fit within the box.")

    # Draw each line
    y_offset = y + (height - total_text_height) // 2  # Center the text vertically
    for line in lines:
        text_surface = font.render(line, True, text_color)
        text_rect = text_surface.get_rect(centerx=x + width // 2, top=y_offset)
        screen.blit(text_surface, text_rect)
        y_offset += font.size(line)[1] + line_spacing

def exit() -> Box:
    """
    Create a box for the exit button.

    :param width: width of screen
    :param height: height of screen.
    """
    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h
    ExitBox = Box(width / 2 - 100, height - 50 , 200 , 50, "EXIT")
    return ExitBox

def MenuBoxes(screen: pygame.Surface, width: int, height: int) -> list[Box]:
    """
    Create the boxes for the main menu.
    :param screen: pygame.Surface, The surface where the menu will be drawn.
    :param width: int, The width of the screen.
    :param height: int, The height of the screen.
    :return: list[Box], A list of Box objects for the main menu.
    """
    margin = 10
    button_width = (width/2 - 2 * margin) 
    button_height = (height/2 - 4 * margin) // 3     
    MenuBoxPlay     =   Box(width/4 + margin, height/4 + 2 * margin, button_width, button_height, "Play")                      #MenuBoxPlay
    MenuBoxRules    =   Box(width/4 + margin, height/4 + button_height + 2 * margin, button_width, button_height, "Rules")      #MenuBoxSettings
    MenuBoxSettings =   Box(width/4 + margin, height/4 + 2 * button_height + 2 * margin, button_width, button_height, "Settings")  #MenuBoxAdvanced
    return [MenuBoxPlay, MenuBoxRules, MenuBoxSettings, exit()]


def AreaHover(boxes: list[Box], mouse_pos: tuple[int, int]) -> None | Box:
    for box in boxes:
        if box.x <= mouse_pos[0] <= box.x_lim and box.y <= mouse_pos[1] <= box.y_lim:
            return box
    return None


def menu(screen: pygame.Surface, width: int, height: int) -> None:
    """
    Display the main menu on the screen.
    
    :param screen: pygame.Surface, The surface where the menu will be drawn.
    :param width: int, The width of the screen.
    :param height: int, The height of the screen.
    :return: None
    """
    global RUNNING
    background(screen, "images//background_image.jpg", width, height)
    boxes = MenuBoxes(screen, width, height)
    for box in boxes:
        box.draw_box(screen, hover = False, font = "arialback", font_size=80)
    MENUON = True
    PrevPos = None
    while MENUON:
        event, pos = mouse_position()       # Continous
        CurrentPos = AreaHover(boxes, pos)  # Continous

        if CurrentPos != PrevPos: # Continous
            # Only activates if the mouse is moved from an area.
            if PrevPos is not None:
                PrevPos.draw_box(screen, hover = False, font = "arialback", font_size=80)
            if CurrentPos is not None:
                CurrentPos.draw_box(screen, hover = True, font = "arialback", font_size=80)
            PrevPos = CurrentPos
        
        if event == pygame.MOUSEBUTTONDOWN:
            if CurrentPos.text == "EXIT":
                MENUON = False
                RUNNING = False
            elif CurrentPos.text == "Play":
                print("Play")
            elif CurrentPos.text == "Rules":
                print("Rules")
            elif CurrentPos.text == "Settings":
                print("Settings")
        if event == pygame.QUIT:
            MENUON = False
            RUNNING = False
    
        # Update screen and control frame rate
        pygame.display.flip()
        CLOCK.tick(FRAME_RATE)
def mouse_position() -> tuple[int | None, tuple[int, int]]:
    """
    Returns the current mouse position and the event type of interest.
    
    Event types include:
    - pygame.MOUSEBUTTONDOWN: Indicates a mouse button press.
    - pygame.QUIT: Indicates a quit event.
    - None: If no relevant event occurred.
    
    :return: A tuple (event_type, mouse_position):
             - event_type: int | None (event constant or None if no event).
             - mouse_position: tuple[int, int] (current cursor position).
    """
    for event in pygame.event.get():
        if event.type in {pygame.MOUSEBUTTONDOWN, pygame.QUIT}:
            return event.type, pygame.mouse.get_pos()
    return (None, pygame.mouse.get_pos())


def main():
    """
    Main game loop function.
    Handles screen updates and quitting the game.
    """
    global RUNNING
    screen, (width, height) = initialize_screen(test_mode=TEST_MODE)
    
    while RUNNING:
        menu(screen, width, height)


        # Update screen and control frame rate
        pygame.display.flip()
        CLOCK.tick(FRAME_RATE)

    pygame.quit()


if __name__ == "__main__":
    main()