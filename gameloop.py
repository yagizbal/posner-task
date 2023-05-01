import pygame
import sys
import math
import posner


pygame.init()

screen_x = 800
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('screen')
FPSCLOCK = pygame.time.Clock()

num_squares = 10 
radius = 200  
square_size = 60

center_x = screen_x // 2
center_y = screen_y // 2

def draw_square(angle, color=(255, 0, 0)):
    x = center_x + radius * math.cos(math.radians(angle)) - square_size // 2
    y = center_y + radius * math.sin(math.radians(angle)) - square_size // 2
    pygame.draw.rect(screen, color, pygame.Rect(x, y, square_size, square_size))

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0)) 
    for i in range(num_squares):
        angle = 360 / num_squares * i
        draw_square(angle)

    FPSCLOCK.tick(60)
    pygame.display.flip()
    pygame.event.pump()