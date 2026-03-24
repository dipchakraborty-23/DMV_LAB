import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Circle")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# Circle properties
x, y = WIDTH // 2, HEIGHT // 2
radius = 30
speed = 5

clock = pygame.time.Clock()

# Game loop
while True:
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Draw circle
    pygame.draw.circle(screen, BLUE, (x, y), radius)

    # Update display
    pygame.display.flip()
    clock.tick(60)