import pygame
import color

pygame.init()

WIDTH, HEIGHT = 500, 500

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Draw circle")

FPS = 60

def draw_window():
    WIN.fill(color.BLUE)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

main()