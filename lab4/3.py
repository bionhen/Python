import pygame
from pygame.draw import *

pygame.init()
color=(255, 255, 255)
FPS = 30
screen = pygame.display.set_mode((1500, 800))
screen.fill(color)
N = 10
def car(a, x, y):
      ellipse(screen, (1, 1, 1), (x-50*a, y+65*abs(a), 30*abs(a), 10*abs(a)))
      polygon(screen, (0, 0, 255), [(x, y), (x+100*a, y), (x+a*100, y+40*abs(a)), (x+a*180, y+40*abs(a)),
      (x+a*180, y+80*abs(a)), (x-40*a, y+80*abs(a)), (x-40*a, y+40*abs(a)), (x, y+40*abs(a))])
      polygon(screen, (255, 255, 255), [(x+10*a, y+10*abs(a)), (x+45*a, y+10*abs(a)), (x+45*a, y+40*abs(a)), (x+10*a, y+40*abs(a))])
      polygon(screen, (255, 255, 255), [(x+65*a, y+10*abs(a)), (x+90*a, y+10*abs(a)), (x+90*a, y+40*abs(a)), (x+65*a, y+40*abs(a))])
      ellipse(screen, (1, 1, 1), (x-10*a, y+65*abs(a), 40*abs(a), 30*abs(a)))
      ellipse(screen, (1, 1, 1), (x+130*a, y+65*abs(a), 40*abs(a), 30*abs(a)))
car(-1, 700, 400)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
