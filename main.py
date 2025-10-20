from constants import SCREEN_WIDTH , SCREEN_HEIGHT , ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE,  ASTEROID_MAX_RADIUS
import pygame

def main():
    pygame.init()

    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH)) 
    print("Screen height: " + str(SCREEN_HEIGHT))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()



if __name__ == "__main__":
    main()
