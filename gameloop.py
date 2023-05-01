import sys
import pygame
import math
import random
from posner import one_loop  


pygame.init()

screen_x = 800
screen_y = 800
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('screen')
FPSCLOCK = pygame.time.Clock()

num_squares = 12
radius = 300
square_size = 60

center_x = screen_x // 2
center_y = screen_y // 2

location_slots = num_squares
validity_effect = 0.2
delay = 60 
validity_variance = 0.1
delay_variance = 0.1
def draw_square(angle, color=(255, 0, 0)):
    x = center_x + radius * math.cos(math.radians(angle)) - square_size // 2
    y = center_y + radius * math.sin(math.radians(angle)) - square_size // 2
    pygame.draw.rect(screen, color, pygame.Rect(x, y, square_size, square_size))
    return (x, y, square_size, square_size)

def draw_arrow(x1, y1, x2, y2, color=(0, 255, 0)):
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx*dx + dy*dy)
    arrow_length_ratio = (length - square_size * 1.5) / length
    x2 = x1 + dx * arrow_length_ratio
    y2 = y1 + dy * arrow_length_ratio
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), 3)

    arrow_head_length = 15
    arrow_head_angle = 35
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    x_arrow = x2 - arrow_head_length * math.cos(math.radians(angle - arrow_head_angle))
    y_arrow = y2 - arrow_head_length * math.sin(math.radians(angle - arrow_head_angle))
    pygame.draw.line(screen, color, (x2, y2), (x_arrow, y_arrow), 3)
    x_arrow = x2 - arrow_head_length * math.cos(math.radians(angle + arrow_head_angle))
    y_arrow = y2 - arrow_head_length * math.sin(math.radians(angle + arrow_head_angle))
    pygame.draw.line(screen, color, (x2, y2), (x_arrow, y_arrow), 3)

def display_text(text, x, y, color=(255, 255, 255),size=36):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

squares = []

for i in range(num_squares):
    angle = 360 / num_squares * i
    square = draw_square(angle)
    squares.append(square)

target_square = random.choice(squares)
win_text = False
squares = []

for i in range(num_squares):
    angle = 360 / num_squares * i
    square = draw_square(angle)
    squares.append(square)

win_text = False

show_w = False
w_timer = 0

invalid, delay, location_chosen, location_slots, location_of_arrow = one_loop(num_squares, 0.2, 1000, 0.2, 0.2)
target_square = squares[location_chosen]
arrow_square = squares[location_of_arrow]

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (target_square[0] <= mouse_x <= target_square[0] + square_size and
                target_square[1] <= mouse_y <= target_square[1] + square_size):
                win_text = True
                win_text_timer = pygame.time.get_ticks() + 300  # Set the timer for 1000 milliseconds

                invalid, delay, location_chosen, location_slots, location_of_arrow = one_loop(num_squares, 0.2, 1000, 0.2, 0.2)
                target_square = squares[location_chosen]
                arrow_square = squares[location_of_arrow]
                w_timer = pygame.time.get_ticks() + delay
            else:
                win_text = False

    screen.fill((0, 0, 0))

    for square in squares:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(square[0], square[1], square_size, square_size))

    target_center_x = arrow_square[0] + square_size // 2
    target_center_y = arrow_square[1] + square_size // 2
    draw_arrow(center_x, center_y, target_center_x, target_center_y)
    
    display_text("+", center_x-15, center_y-35, color=(0, 255, 0),size=90)

    if win_text:
        display_text("Correct!", screen_x // 2 - 50, screen_y // 2 - 20)
        if pygame.time.get_ticks() > win_text_timer:
            win_text = False

    if pygame.time.get_ticks() >= w_timer:
        show_w = True
    else:
        show_w = False

    if show_w:
        w_x = target_square[0] + square_size // 2 - 15
        w_y = target_square[1] + square_size // 2 - 20
        display_text("W", w_x, w_y, color=(0, 0, 255))

    FPSCLOCK.tick(60)
    pygame.display.flip()
    pygame.event.pump()
