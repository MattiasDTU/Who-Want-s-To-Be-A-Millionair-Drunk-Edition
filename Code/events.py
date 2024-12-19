import pygame
from components import Box

def AreaHover(boxes: list[Box], mouse_pos: tuple[int, int]) -> None | Box:
    for box in boxes:
        if box.x <= mouse_pos[0] <= box.x_lim and box.y <= mouse_pos[1] <= box.y_lim:
            return box
    return None

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
