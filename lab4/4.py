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
      ellipse(screen, (1, 1, 1), (x-30*a, y+65*abs(a), 40*abs(a), 30*abs(a)))
      ellipse(screen, (1, 1, 1), (x+120*a, y+65*abs(a), 40*abs(a), 30*abs(a)))


def car1(a, x, y):
    ellipse(screen, (1, 1, 1), (x - 35 * a, y + 65 * abs(a), 15 * abs(a), 5 * abs(a)))
    polygon(screen, (0, 0, 255),
            [(x, y), (x + 100 * a, y), (x + a * 100, y + 40 * abs(a)), (x + a * 180, y + 40 * abs(a)),
             (x + a * 180, y + 80 * abs(a)), (x - 40 * a, y + 80 * abs(a)), (x - 40 * a, y + 40 * abs(a)),
             (x, y + 40 * abs(a))])
    polygon(screen, (255, 255, 255),
            [(x + 10 * a, y + 10 * abs(a)), (x + 45 * a, y + 10 * abs(a)), (x + 45 * a, y + 40 * abs(a)),
             (x + 10 * a, y + 40 * abs(a))])
    polygon(screen, (255, 255, 255),
            [(x + 65 * a, y + 10 * abs(a)), (x + 90 * a, y + 10 * abs(a)), (x + 90 * a, y + 40 * abs(a)),
             (x + 65 * a, y + 40 * abs(a))])
    ellipse(screen, (1, 1, 1), (x + 10 * a, y + 65 * abs(a), 40 * abs(a), 30 * abs(a)))
    ellipse(screen, (1, 1, 1), (x + 160 * a, y + 65 * abs(a), 40 * abs(a), 30 * abs(a)))


i = 0
m = 51
n = 51
k = 400
while i<200:
    m += 1
    n += 1
    k += 4
    rect(screen, (51, 51, 51), (-200, k, 1500, 800))
    i += 1
rect(screen, (50, 50, 50), (0, 0, 800, 120))
rect(screen, (204, 204, 204), (500, 20, 150, 500))
rect(screen, (102, 102, 102), (310, 70, 120, 400))    #smallcenter
rect(screen, (102, 102, 102), (450, 110, 120, 400))    #smallcenter
rect(screen, (153, 204, 204), (10, 100, 120, 400))      #smallrl
rect(screen, (153, 204, 204), (670, 90, 120, 400))  # smallrl
car(1.0, 270, 600)
car1(-1.5, 690, 660)
car(0.7, 530, 570)
car1(-0.4, 430, 520)
car1(-0.6, 200, 530)
car(0.7, 80, 600)
circle = pygame.Surface((800*2, 800*2), pygame.SRCALPHA)
ellipse(circle, (102, 153, 153, 128), (200, 150, 400, 100))
ellipse(circle, (102, 153, 153, 128), (100, -10, 500, 120))
ellipse(circle, (102, 153, 153, 128), (600, -20, 500, 120))
ellipse(circle, (200, 200, 200, 128), (20, 20, 100, 30))
ellipse(circle, (100, 100, 100, 128), (240, 40, 150, 30))
ellipse(circle, (150, 150, 150, 128), (640, 30, 120, 40))
rect(circle, (220, 220, 220, 128), (20, 150, 300, 300))
rect(circle, (220, 220, 220, 128), (500, 120, 300, 300))
rect(circle, (1, 1, 1, 158), (500, 0, 100, 100))
rect(circle, (1, 1, 1, 58), (200, 0, 100, 100))
rect(circle, (1, 1, 1, 150), (0, 0, 100, 100))
ellipse(circle, (10, 10, 10, 128), (100, 30, 120, 40))
ellipse(circle, (10, 10, 10, 128), (630, 50, 150, 60))
ellipse(circle, (10, 10, 10, 128), (430, 40, 300, 70))
i = 0
m = 51
n = 51
k = 51
r = 300
l = -500
z = 500
while i < 25:
    m += 6
    n += 6
    k += 6
    r -= 10
    l += 5
    z += 5
    i += 1
    ellipse(circle, (m, n, k, 128), (l, z, 10*r, r))
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
