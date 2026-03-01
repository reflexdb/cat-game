import pygame

# Window settings
WIDTH = 800
HEIGHT = 600
FPS = 60
TITLE = "Cat Adventure"

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)       # Grass background
BROWN = (139, 69, 19)       # Cat tree
BLUE = (65, 105, 225)       # Puddle
RED = (220, 20, 60)         # Treats
YELLOW = (255, 215, 0)      # Toys/Balls
GRAY = (128, 128, 128)      # Dogs
ORANGE = (255, 140, 0)      # Cat

# Game entity settings
PLAYER_SPEED = 5
PLAYER_SIZE = 32

# Difficulty Configurations
DIFFICULTIES = {
    "EASY": {
        "ENEMY_SPEED": 2,
        "PUDDLE_COUNT": 3,
        "DOG_COUNT": 2
    },
    "MEDIUM": {
        "ENEMY_SPEED": 4,
        "PUDDLE_COUNT": 5,
        "DOG_COUNT": 4
    },
    "HARD": {
        "ENEMY_SPEED": 6,
        "PUDDLE_COUNT": 8,
        "DOG_COUNT": 6
    }
}
ENEMY_SIZE = 40
ITEM_SIZE = 20
PUDDLE_SIZE = 60
GOAL_SIZE = 80

# Game logic settings
LEVEL_TIME = 30 # Seconds
POINTS_PER_ITEM = 100
