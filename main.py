import pygame # https://www.pygame.org/docs/ref/pygame.html
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print ("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Clock init
    clock = pygame.time.Clock()
    dt = 0

    # Group init
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Player grouping setup (before player init)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Player init
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    #############################################
    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update. tu se radi o 0.016 jer smo na 60fps.
        for updatable_item in updatable:
            updatable_item.update(dt)
        

        #for shot in shots:
        #    shot.update(dt)  
 

        for ast in asteroids:
            for bullet in shots:
                if bullet.collided(ast):
                    bullet.kill()
                    ast.kill()    

            if player.collided(ast):
                print("Game over")
                return

        # Render
        pygame.Surface.fill(screen, (0, 0, 0))
        
        for drawable_item in drawable:
            drawable_item.draw(screen)

        #for shot in shots:
        #    shot.draw(screen)
        
        # Render - Flip
        pygame.display.flip()

        # Time 
        dt = clock.tick(60) / 1000
    #############################################

"""
Destruction

Okay so bullets are flying, but they don't do anything. Let's kill some asteroids!

There are three types of asteroids:

    Large
    Medium
    Small

When a large asteroid is destroyed, it should split into two medium asteroids. When a medium asteroid is destroyed, it should split into two small asteroids. When a small asteroid is destroyed, it should disappear.

For now, we'll just always make the asteroids disappear when they're destroyed. We will handle splitting later.
"""


if __name__ == "__main__":
    main()