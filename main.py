import sys
import pygame
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 74)

# Load screen assets
try:
    title_img = pygame.image.load("assets/title.png").convert()
    title_img = pygame.transform.scale(title_img, (WIDTH, HEIGHT))
except FileNotFoundError:
    title_img = None

try:
    win_img = pygame.image.load("assets/win.png").convert()
    win_img = pygame.transform.scale(win_img, (WIDTH, HEIGHT))
except FileNotFoundError:
    win_img = None

try:
    lose_img = pygame.image.load("assets/lose.png").convert()
    lose_img = pygame.transform.scale(lose_img, (WIDTH, HEIGHT))
except FileNotFoundError:
    lose_img = None

def draw_text(text, font_obj, color, surface, x, y):
    textobj = font_obj.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main():
    state = "START"
    difficulties = list(DIFFICULTIES.keys())
    diff_index = 1
    level = None
    
    while True:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if state == "START":
                    if event.key == pygame.K_UP:
                        diff_index = (diff_index - 1) % len(difficulties)
                    elif event.key == pygame.K_DOWN:
                        diff_index = (diff_index + 1) % len(difficulties)
                        
                if state in ["START", "LEVEL_COMPLETE"]:
                   if event.key == pygame.K_SPACE:
                       state = "PLAYING"
                       selected_diff = difficulties[diff_index]
                       level = Level(selected_diff) # Start level
                elif state == "GAME_OVER":
                   if event.key == pygame.K_SPACE:
                       state = "START"
        
        if state == "START":
            if title_img:
                screen.blit(title_img, (0, 0))
            else:
                screen.fill(BLACK)
                draw_text("Cat Adventure", font, WHITE, screen, WIDTH // 2, HEIGHT // 3)
            
            # Draw Difficulty selection
            # Adding a slight background to make text readable over the image
            s = pygame.Surface((400, 200))
            s.set_alpha(128)
            s.fill(BLACK)
            screen.blit(s, (WIDTH // 2 - 200, HEIGHT // 2 - 20))
            
            draw_text("Select Difficulty (UP/DOWN):", pygame.font.Font(None, 36), WHITE, screen, WIDTH // 2, HEIGHT // 2)
            
            for i, diff in enumerate(difficulties):
                color = YELLOW if i == diff_index else WHITE
                draw_text(diff, pygame.font.Font(None, 48), color, screen, WIDTH // 2, HEIGHT // 2 + 50 + (i * 40))
                
            draw_text("Press SPACE to Start", pygame.font.Font(None, 36), GREEN, screen, WIDTH // 2, HEIGHT - 50)
            pygame.display.flip()

        elif state == "PLAYING":
            state = level.run(screen)
            pygame.display.flip()
            
        elif state == "GAME_OVER":
            if lose_img:
                screen.blit(lose_img, (0, 0))
            else:
                screen.fill(BLACK)
                draw_text("Game Over!", font, RED, screen, WIDTH // 2, HEIGHT // 3)
            
            s = pygame.Surface((400, 50))
            s.set_alpha(128)
            s.fill(BLACK)
            screen.blit(s, (WIDTH // 2 - 200, HEIGHT - 125))
            
            draw_text("Press SPACE for Title", pygame.font.Font(None, 36), WHITE, screen, WIDTH // 2, HEIGHT - 100)
            pygame.display.flip()
            
        elif state == "LEVEL_COMPLETE":
            if win_img:
                screen.blit(win_img, (0, 0))
            else:
                screen.fill(BLACK)
                draw_text("Level Complete!", font, GREEN, screen, WIDTH // 2, HEIGHT // 3)
                
            s = pygame.Surface((400, 100))
            s.set_alpha(128)
            s.fill(BLACK)
            screen.blit(s, (WIDTH // 2 - 200, HEIGHT - 175))
            
            draw_text(f"Final Score: {level.score}", pygame.font.Font(None, 48), WHITE, screen, WIDTH // 2, HEIGHT - 150)
            draw_text("Press SPACE to Play Again", pygame.font.Font(None, 36), WHITE, screen, WIDTH // 2, HEIGHT - 100)
            pygame.display.flip()

if __name__ == "__main__":
    main()
