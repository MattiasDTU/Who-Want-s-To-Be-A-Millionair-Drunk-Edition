from PIL import Image
import pygame
from colors import *
from classes import Box

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

def sound_image(screen: pygame.Surface, box: Box, sound_on: bool, hover: bool = False ) -> None:
    """
    This function will draw the sound image on the screen
    """
    sound_on_image = "images//sound_on.png"
    sound_off_image = "images//sound_off.png"
    sound = pygame.image.load(sound_on_image) if sound_on else pygame.image.load(sound_off_image)
    sound = pygame.transform.scale(sound, (box.width, box.height))
    screen.blit(sound, (box.x, box.y))