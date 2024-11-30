import pygame
from colors import *
from classes import Box

# ----------------- Background Functions ----------------- #
def draw_border(screen: pygame.Surface, width: int, height: int,
                 color: tuple[int,int,int] = BLUE_COLOR) -> None:
    """
    This function draws a border around the screen.
    Variables:
        screen:     pygame.Surface
        width:      int
        height:     int
        color:      tuple[int,int,int]
    """
    pygame.draw.rect(screen, color, (0, 0, width ,height), width = 10)


def background_image(screen: pygame.Surface, image_url: str, width: int, height: int) -> None:
    """
    This function sets the background image of the screen.
    Variables:
        screen:     pygame.Surface
        image:      str
        width:      int
        height:     int
    """
    background = pygame.image.load(image_url)
    background = pygame.transform.scale(background, (width, height))
    screen.blit(background, (0, 0))


def default_background(screen: pygame.Surface, image_url: str, width: int, height: int) -> None:
    """
    This function sets the default background color of the screen.
    Variables:
        screen:     pygame.Surface
        image_url:  str
        width:      int
        height:     int
    """
    background_image(screen, image_url, width, height)
    draw_border(screen, width, height)



def box_with_text(screen: pygame.Surface, text: str, box: Box, font_name: str="Arial", color: tuple[int,int,int] =(0, 0, 0),
                   boxcolor1: tuple[int,int,int] = GRAY_COLOR, boxcolor2: tuple[int,int,int] = BLUE_COLOR, max_font_size: int=50, line_spacing: int=5, remove: bool = False) -> None:
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
    pygame.draw.rect(screen, boxcolor1, box.cords(), border_radius = 10)  # Button rectangle
    pygame.draw.rect(screen, boxcolor2, box.cords(), 2, border_radius = 10)  # Button border    
    if isinstance(box, tuple):
        x, y, width, height = box
    else:
        x, y, width, height = box.x, box.y, box.width, box.height

    # Initialize font size and font
    font_size = max_font_size
    font = pygame.font.SysFont(font_name, font_size)

    while font_size > 0:
        # Wrap the text
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            text_surface = font.render(test_line, True, color)
            if text_surface.get_width() > width:  # Exceeds the box width
                if current_line:  # Push the current line to lines
                    lines.append(current_line.strip())
                current_line = word + " "
            else:
                current_line = test_line

        # Add the last line
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
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(centerx=x + width // 2, top=y_offset)
        screen.blit(text_surface, text_rect)
        y_offset += font.size(line)[1] + line_spacing


def render_text(text: str, size: int,  font : str = None, Anti_aliasing: bool = True,
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