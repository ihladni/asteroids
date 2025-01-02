import pygame # https://www.pygame.org/docs/ref/pygame.html
from constants import *

def main():
    print ("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Clock
    clock = pygame.time.Clock()
    dt = 0

    #############################################
    while True:
        # Event and Player handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Render
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()

        # Time 
        dt = clock.tick(60) / 1000
    #############################################

if __name__ == "__main__":
    main()