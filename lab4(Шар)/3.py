import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
score = 0
class Ball:
    def __init__(self, x, y, Vx, Vy, r, COLOR, wallx, wally, cball):
     self.x = x
     self.y = y
     self.r = r

    def move(self):
       self.x += self.Vx
       self.y += self.Vy

    def collision_wal(self):

      if self.x < 0+self.r or self.x > 1200-self.r:
        self.Vy = -self.Vy
      if self.y < 0+self.r or self.y > 900 -self.r:
        self.Vy = -self.Vy

    def collision_ball(self):
      if self.cball > 0:
         self.Vx = -self.Vx
         self.Vy = -self.Vy
balls = []
for i in range(randint(6, 12)):
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    Vx = randint(-10, 10)
    Vy = randint(-10, 10)
    COLOR = COLORS[randint(0, 5)]
    wallx = 0
    wally = 0
    cball = 0
    my_ball = Ball(x, y, Vx, Vy, r, COLOR, wallx, wally, cbal)
    balls.append(my_ball)
def new_ball(color, x, y, r):
    circle(screen, color, (x, y), r)

l = len(balls)


def click(event):
    print(x, y, r)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:

    f1 = pygame.font.Font(None, 50)
    text1 = f1.render(str(score), True, (180, 0, 0))
    text2 = f1.render('score:', True, (180, 0, 0))
    screen.blit(text1, (120, 50))
    screen.blit(text2, (10, 50))
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            w, z = event.pos
            print(w, z)
            for i in range(l):
              if
            print('score:', score)

    for i in range(l):
      color, x, y, r = balls[i]
      new_ball(color, x, y, r)
    for i in range(l):
       balls[i][1] += v[i][0]
       balls[i][2] += v[i][1]
       if balls[i][1] - balls[i][3] < 0 or balls[i][1] + balls[i][3] > 1200:
          v[i][0] = -v[i][0]
       if balls[i][2] - balls[i][3] < 0 or balls[i][2] + balls[i][3]> 900:
          v[i][1] = -v[i][1]
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()