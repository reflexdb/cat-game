import pygame
import random
from settings import *
from sprites import Cat, Dog, Collectible, Puddle, Goal

class Level:
    def __init__(self):
        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        self.hazards = pygame.sprite.Group()
        
        # Setup level
        self.setup()
        
        # Level states
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        
        # Timer
        self.start_ticks = pygame.time.get_ticks() 
        self.time_left = LEVEL_TIME

    def setup(self):
        # Player
        self.player = Cat(50, HEIGHT // 2)
        self.all_sprites.add(self.player)
        
        # Goal
        self.goal = Goal(WIDTH - 80, HEIGHT // 2)
        self.all_sprites.add(self.goal)
        
        # Enemies
        for _ in range(4):
            x = random.randint(150, WIDTH - 150)
            y = random.randint(50, HEIGHT - 50)
            dx = random.choice([-ENEMY_SPEED, ENEMY_SPEED])
            dy = random.choice([-ENEMY_SPEED, ENEMY_SPEED])
            dog = Dog(x, y, dx, dy)
            self.enemies.add(dog)
            self.all_sprites.add(dog)
            
        # Hazards (Puddles)
        for _ in range(5):
             x = random.randint(150, WIDTH - 150)
             y = random.randint(50, HEIGHT - 50)
             puddle = Puddle(x, y)
             self.hazards.add(puddle)
             self.all_sprites.add(puddle)
             
        # Collectibles
        for _ in range(10):
             x = random.randint(100, WIDTH - 100)
             y = random.randint(50, HEIGHT - 50)
             item = Collectible(x, y)
             self.collectibles.add(item)
             self.all_sprites.add(item)

    def run(self, surface):
        # Update sprites
        self.all_sprites.update()
        
        # Timer Logic
        seconds_passed = (pygame.time.get_ticks() - self.start_ticks) / 1000
        self.time_left = max(0, LEVEL_TIME - seconds_passed)

        # Check collisions - Collectibles
        hits = pygame.sprite.spritecollide(self.player, self.collectibles, True)
        if hits:
            self.score += POINTS_PER_ITEM * len(hits)
            
        # Check collisions - Hazards & Enemies (Game Over)
        if pygame.sprite.spritecollide(self.player, self.enemies, False) or \
           pygame.sprite.spritecollide(self.player, self.hazards, False) or \
           self.time_left <= 0:
            return "GAME_OVER"
            
        # Check collision - Goal (Win)
        if pygame.sprite.collide_rect(self.player, self.goal):
            return "LEVEL_COMPLETE"

        # Draw
        surface.fill(GREEN)
        self.all_sprites.draw(surface)
        
        # Draw HUD
        score_surface = self.font.render(f"Score: {self.score}", True, WHITE)
        time_surface = self.font.render(f"Time: {int(self.time_left)}", True, WHITE)
        surface.blit(score_surface, (10, 10))
        surface.blit(time_surface, (WIDTH - 120, 10))

        return "PLAYING"
