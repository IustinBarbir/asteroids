from constants import SCREEN_WIDTH , SCREEN_HEIGHT , ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE,  ASTEROID_MAX_RADIUS
import pygame
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from circleshape import CircleShape
from shot import Shot
import sys

def draw_text(surface, text, size, x, y, color="white"):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, rect)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0
    score = 0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable= pygame.sprite.Group()
    drawable= pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    game_over = False

    while(True):
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("score = " + str(score))
                return
            if game_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    main()   
                    return
                
        if game_over:
            screen.fill("black")
            draw_text(screen, "GAME OVER", 72, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60)
            draw_text(screen, f"Score: {score}", 48, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text(screen, "Press SPACE to play again", 32, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)

            pygame.display.flip()
            continue
            
        screen.fill("black")

        updatable.update(dt)

        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                print("score = " + str(score))
                game_over = True
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    score += 1
        
        for obj in drawable:
            obj.draw(screen)

        draw_text(screen, f"Score: {score}", 32, 80, 30)
        
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
