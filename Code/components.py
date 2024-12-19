import pygame
# ----- Color Constants ----- #
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)
GRAY_COLOR = (128, 128, 128)
GOLD_COLOR = (255, 215, 0)
RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)
BLACK_COLOR = (0, 0, 0)

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
        if locked == 0:
            InnerColor = BLACK_COLOR
            TextColor = WHITE_COLOR
        if locked == 1:
            InnerColor = GREEN_COLOR
            TextColor = WHITE_COLOR
        if locked == 2:
            InnerColor = RED_COLOR
            TextColor = WHITE_COLOR
        if hover and locked != 2:
            box_with_text(screen, self.text, (self.x, self.y, self.width, self.height), font_name = font,
                          text_color = BLACK_COLOR, InnerBox = GOLD_COLOR, max_font_size=font_size)
        else:
            box_with_text(screen, self.text, (self.x, self.y, self.width, self.height), font_name = font,
                          text_color = TextColor, InnerBox = InnerColor, max_font_size=font_size)



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

def render(text: str, size: int,  font : str = None, Anti_aliasing: bool = True,
                 color : str | tuple = (0,0,0)) -> None:
    """
    This function will render the text on the screen.
    variabels:
        text: str           -> The text that needs to be rendered
        size: int           -> The size of the text
        font: str           -> The font of the text
        Anti_aliasing: bool -> If True, the text will be smooth
        color: tuple        -> The color of the text
    """
    if font != None:
        font = pygame.font.match_font(font)
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, Anti_aliasing, color)
    return text_surface

def render_text(screen: pygame.Surface, text: str, font_size: int, font_name: str, color: tuple[int,int,int],
                y_position: int, screen_width: int) -> None:
    """
    Renders and centers text on the screen at a given y-coordinate.

    :param screen: pygame.Surface, The surface to render the text onto.
    :param text: str, The text to display.
    :param font_size: int, The size of the font.
    :param font_name: str, The name of the font.
    :param color: tuple, The color of the text.
    :param y_position: int, The vertical position of the text.
    :param screen_width: int, The width of the screen to center the text.
    """
    rendered_text = render(text, font_size, font=font_name, color=color)
    x_position = screen_width / 2 - rendered_text.get_width() / 2
    screen.blit(rendered_text, (x_position, y_position))




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



