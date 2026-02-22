import pygame
from settings import *

class Cat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/cat.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += PLAYER_SPEED

        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Dog(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.image = pygame.image.load("assets/dog.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (ENEMY_SIZE, ENEMY_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dx = dx
        self.dy = dy

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Bounce off edges
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.dy *= -1

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/treat.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (ITEM_SIZE, ITEM_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Puddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/puddle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (PUDDLE_SIZE, PUDDLE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/tree.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (GOAL_SIZE, GOAL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
