import pygame
from ball import Ball

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()
ball = Ball()

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        ball.move(0, -20)
    if keys[pygame.K_DOWN]:
        ball.move(0, 20)
    if keys[pygame.K_LEFT]:
        ball.move(-20, 0)
    if keys[pygame.K_RIGHT]:
        ball.move(20, 0)

    ball.draw(screen)

    pygame.display.update()
    clock.tick(10)

pygame.quit()