import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Circle")


WHITE = (255, 255, 255)
BLUE = (0, 100, 255)


x, y = WIDTH // 2, HEIGHT // 2
radius = 30
speed = 5

clock = pygame.time.Clock()


while True:
    screen.fill(WHITE)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    
    pygame.draw.circle(screen, BLUE, (x, y), radius)


    pygame.display.flip()
    clock.tick(60)
