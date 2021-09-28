import pygame
from pygame.draw import *

pygame.init()
color=(255, 255, 255)
FPS = 30
screen = pygame.display.set_mode((1500, 800))
screen.fill(color)
x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
circle(screen, (255, 255, 0), (700, 400), 100)
circle(screen, (225, 0, 0), (650, 360), 20)
circle(screen, (225, 0, 0), (750, 360), 15)
circle(screen, (1, 1, 1), (650, 360), 10)
circle(screen, (1, 1, 1), (750, 360), 7)
rect(screen, (1, 1, 1), (650, 420, 100, 20))
points = [(670, 340), (680, 330), (600, 300), (590, 310)]
polygon(screen, (1, 1, 1), [(670, 340), (680, 330), (600, 300), (590, 310)])
polygon(screen, (1, 1, 1), [(730, 340), (720, 330), (780, 300), (790, 310)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
