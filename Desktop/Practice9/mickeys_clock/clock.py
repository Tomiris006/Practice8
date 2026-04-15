import pygame
import datetime

class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (300, 300)

        # оригинальная картинка
        self.hand_img = pygame.image.load("images/mickey_hand.png")
        self.hand_img = pygame.transform.scale(self.hand_img, (150, 30))

    def draw(self):
        now = datetime.datetime.now()

        seconds = now.second
        minutes = now.minute

        # углы
        sec_angle = -seconds * 6
        min_angle = -minutes * 6

        # ВАЖНО: создаём 2 разные руки
        sec_hand = pygame.transform.rotate(self.hand_img, sec_angle)
        min_hand = pygame.transform.rotate(self.hand_img, min_angle)

        # позиции
        sec_rect = sec_hand.get_rect(center=self.center)
        min_rect = min_hand.get_rect(center=self.center)

        # рисуем ОБЕ
        self.screen.blit(min_hand, min_rect)
        self.screen.blit(sec_hand, sec_rect)