import pygame
from pygame.draw import *

pygame.init()
color=(255, 255, 255)
FPS = 30
screen = pygame.display.set_mode((1500, 800))
screen.fill(color)
x = 100; y = 100
a = 1
N = 10
def car[a, x, y]:
      polygon(screen, (0, 0, 255), [(x, y), (x + 100 * a, y), (x + a * 100, y + 20 * a), (x + a * 180, y + 20 * a),
(x + a * 180, y + 80 * a), (x - 40 * a, y + 80 * a), (x - 40 * a, y + 20 * a)], (x, y + 20 * a))
      polygon(screen, (0, 0, 255), [(x+5*a, y+5*a), (x+45*a, y+5*a), ()])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
