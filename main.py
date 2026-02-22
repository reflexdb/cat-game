import sys
import pygame
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 74)

def draw_text(text, font_obj, color, surface, x, y):
    textobj = font_obj.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main():
    state = "START"
    level = Level()
    
    while True:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if state in ["START", "GAME_OVER", "LEVEL_COMPLETE"]:
                   if event.key == pygame.K_SPACE:
                       state = "PLAYING"
                       level = Level() # Reset level
        
        if state == "START":
            screen.fill(BLACK)
            draw_text("Cat Adventure", font, WHITE, screen, WIDTH // 2, HEIGHT // 3)
            draw_text("Press SPACE to Start", pygame.font.Font(None, 36), WHITE, screen, WIDTH // 2, HEIGHT // 2)
            pygame.display.flip()

        elif state == "PLAYING":
            state = level.run(screen)
            pygame.display.flip()
            
        elif state == "GAME_OVER":
            screen.fill(BLACK)
            draw_text("Game Over!", font, RED, screen, WIDTH // 2, HEIGHT // 3)
            draw_text("Press SPACE to Restart", pygame.font.Font(None, 36), WHITE, screen, WIDTH // 2, HEIGHT // 2)
            pygame.display.flip()
            
        elif state == "LEVEL_COMPLETE":
            screen.fill(BLACK)
            draw_text("Level Complete!", font, GREEN, screen, WIDTH // 2, HEIGHT // 3)
            draw_text(f"Final Score: {level.score}", pygame.font.Font(None, 48), WHITE, screen, WIDTH // 2, HEIGHT // 2)
            draw_text("Press SPACE to Play Again", pygame.font.Font(None, 36), WHITE, screen, WIDTH // 2, HEIGHT // 1.5)
            pygame.display.flip()

if __name__ == "__main__":
    main()
