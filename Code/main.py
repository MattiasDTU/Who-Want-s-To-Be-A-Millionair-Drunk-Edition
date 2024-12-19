from screen import initialize_screen
from menu import menu
from excel import GAMES
import pygame

# ----- Program Constants ----- #
TEST_MODE = False       # Flag to run in test mode
FRAME_RATE = 60        # Frames per second
# ----- Screen Constants ----- #µ

pygame.init()
CLOCK = pygame.time.Clock()

RUNNING = True         # Main game loop flag

def main():
    """
    Main game loop function.
    Handles screen updates and quitting the game.
    """
    global RUNNING
    screen, (width, height) = initialize_screen(test_mode=TEST_MODE)
    
    while RUNNING:
        RUNNING = menu(screen, width, height, GAMES)


        # Update screen and control frame rate
        pygame.display.flip()
        CLOCK.tick(FRAME_RATE)

    pygame.quit()


if __name__ == "__main__":
    main()