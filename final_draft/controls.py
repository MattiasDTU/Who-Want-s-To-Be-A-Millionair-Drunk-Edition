from classes import Box
from controls import *
from colors import *
import pygame
from layout import *

def mouse_position() -> tuple[str, tuple[int,int]]:
    """
    This function returns the position of the cursor mouse,
    as well as the event that is happening at all time.
    """
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            return (pygame.MOUSEBUTTONDOWN, pygame.mouse.get_pos())
        if event.type == pygame.QUIT:
            return (pygame.QUIT, pygame.mouse.get_pos())
    return (None, pygame.mouse.get_pos())
