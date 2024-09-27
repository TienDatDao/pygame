import pygame
import color
import numpy as np

pygame.init()

WIDTH, HEIGHT = 1000, 1000
BLOCK = 10
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Draw circle")
FPS = 60
R = int(input())

arr_check = [[0 for _ in range(int(WIDTH/BLOCK))] for _ in range(int(HEIGHT/BLOCK))]

def calculate():
    CENTER_X = int(WIDTH/BLOCK/2)
    CENTER_Y = int(HEIGHT/BLOCK/2)
    for i in range(0, int(WIDTH/BLOCK)):
        for j in range(0, int(HEIGHT/BLOCK)):
            x = abs(CENTER_X-i)
            y = abs(CENTER_Y-j)
            if x*x+y*y <= R*R:
                arr_check[i][j] = 1


    #arr_check[CENTER_X][CENTER_Y] = 1

def draw_window():
    WIN.fill(color.BLACK)

def draw_grid():
    for i in range(0, int(WIDTH/BLOCK)):
        for j in range(0, int(HEIGHT/BLOCK)):
            x = i*BLOCK + 1
            y = j*BLOCK + 1
            if arr_check[i][j] == 0:
                pygame.draw.rect(WIN, color.WHITE, (x, y, BLOCK-2, BLOCK-2))
            else:
                pygame.draw.rect(WIN, color.YELLOW, (x, y, BLOCK-2, BLOCK-2))

def main():
    calculate()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

        draw_grid()
        
        pygame.display.flip()

    pygame.quit()

main()
