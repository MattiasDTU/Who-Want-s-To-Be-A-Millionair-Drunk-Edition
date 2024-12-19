import pygame

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
