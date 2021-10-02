import pygame
from pygame.draw import *

pygame.init()
color=(200, 200, 200)
FPS = 30
screen = pygame.display.set_mode((800, 800))
screen.fill(color)
N = 10


def car(a, x, y):
      ellipse(screen, (1, 1, 1), (x-50*a, y+65*abs(a), 15*abs(a), 5*abs(a)))
      polygon(screen, (0, 0, 255), [(x, y), (x+100*a, y), (x+a*100, y+40*abs(a)), (x+a*180, y+40*abs(a)),
      (x+a*180, y+80*abs(a)), (x-40*a, y+80*abs(a)), (x-40*a, y+40*abs(a)), (x, y+40*abs(a))])
      polygon(screen, (255, 255, 255), [(x+10*a, y+10*abs(a)), (x+45*a, y+10*abs(a)), (x+45*a, y+40*abs(a)), (x+10*a, y+40*abs(a))])
      polygon(screen, (255, 255, 255), [(x+65*a, y+10*abs(a)), (x+90*a, y+10*abs(a)), (x+90*a, y+40*abs(a)), (x+65*a, y+40*abs(a))])
      ellipse(screen, (1, 1, 1), (x-10*a, y+65*abs(a), 40*abs(a), 30*abs(a)))
      ellipse(screen, (1, 1, 1), (x+120*a, y+65*abs(a), 40*abs(a), 30*abs(a)))


rect(screen, (51, 51, 51), (-200, 400, 1500, 800))
rect(screen, (204, 204, 204), (500, 20, 150, 500))
ellipse(screen, (153, 204, 204), (-200, 600, 2000, 800))
rect(screen, (102, 153, 102), (600, 70, 150, 500))
rect(screen, (102, 102, 102), (10, 0, 150, 500))
rect(screen, (153, 153, 102), (200, 0, 150, 500))
rect(screen, (153, 204, 204), (100, 50, 150, 500))
car(1.2, 300, 600)
circle = pygame.Surface((800*2, 800*2), pygame.SRCALPHA)
ellipse(circle, (102, 153, 153, 128), (100, 620, 100, 50))
ellipse(circle, (102, 153, 153, 128), (50, 500, 120, 70))
ellipse(circle, (102, 153, 153, 128), (-20, 380, 150, 100))
ellipse(circle, (102, 153, 153, 128), (200, 150, 400, 100))
ellipse(circle, (102, 153, 153, 128), (100, -10, 500, 120))
ellipse(circle, (102, 153, 153, 128), (600, -20, 500, 120))
screen.blit(circle, (0, 0))



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
