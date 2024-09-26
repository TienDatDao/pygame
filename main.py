import pygame

WIDTH, HEIGHT = 500, 500

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Draw circle")

WHITE = (255,255,255)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        WIN.fill(WHITE)
        pygame.display.update()

    pygame.quit()

main()