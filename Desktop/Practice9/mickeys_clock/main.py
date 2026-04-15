import pygame
from clock import MickeyClock

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
mc = MickeyClock(screen)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mc.draw()

    pygame.display.update()
    clock.tick(1)  # обновление каждую секунду

pygame.quit()