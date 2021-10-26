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

""" Задает класс Ball с методами:
 движения move
 столкновения со стеной collision_wall
 столкновения с другим шариком collision_ball
"""


class Ball:
    def __init__(self, x, y, vx, vy, vx1, vy1, r, COLOR, count):
     self.x = x
     self.y = y
     self.r = r
     self.count = count
     self.vx = vx
     self.vy = vy
     self.COLOR = COLOR
     self.vx1 = vx1
     self.vy1 = vy1

    def move(self):
       self.x += self.vx
       self.y += self.vy

    def collision_wall(self):

      if self.x < 0+self.r or self.x > 1200-self.r:
        self.vx = -self.vx
      if self.y < 0+self.r or self.y > 900 -self.r:
        self.vy = -self.vy

    def collision_ball(self):
      if self.count > 0:
         self.vx = self.vx1
         self.vy = self.vy1


class Rect:
    def __init__(self, x, y, vx, vy, ax, ay, a, b, COLOR):
     self.x = x
     self.y = y
     self.a = a
     self.b = b
     self.vx = vx
     self.vy = vy
     self.COLOR = COLOR
     self.ax = ax
     self.ay = ay

    def move(self):
       self.x += self.vx
       self.y += self.vy
       self.vx += self.ax
       self.vy += self.ay


    def collision_wall(self):

      if self.x < 0 or self.x > 1200-self.a:
        self.vx = -self.vx
      if self.y < 0 or self.y > 900 -self.b:
        self.vy = -self.vy



""" 
Создает кортеж balls из элементов Ball с рандомной длиной
"""

balls = []
for i in range(randint(6, 12)):
    x = randint(100+100*i, 200+100*i)
    y = randint(100, 500)
    r = randint(30, 50)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    COLOR = COLORS[randint(0, 5)]
    count = 0
    my_ball = Ball(x, y, vx, vy, 0, 0, r, COLOR, count)
    balls.append(my_ball)


rects = []
for i in range(randint(6, 12)):
    x = randint(100+100*i, 200+100*i)
    y = randint(100, 500)
    a = randint(20, 40)
    b = randint(10, 25)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    ax = randint(-1, 1)
    ay = randint(-1, 1)
    COLOR = COLORS[randint(0, 5)]
    my_rect = Rect(x, y, vx, vy, ax, ay, a, b, COLOR)
    rects.append(my_rect)


def new_ball(color, x, y, r):
    circle(screen, color, (x, y), r)


def new_rect(color, x, y, a, b):
    rect(screen, color, (x, y, a, b))

l = len(balls)
s = len(rects)


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
               if (balls[i].x-w)**2 + (balls[i].y-z)**2 < balls[i].r**2:
                score += 1
                balls.pop(i)
                x = randint(100, 700)
                y = randint(100, 500)
                r = randint(30, 50)
                vx = randint(-10, 10)
                vy = randint(-10, 10)
                COLOR = COLORS[randint(0, 5)]
                count = 0
                my_ball = Ball(x, y, vx, vy, 0, 0, r, COLOR, count)
                balls.append(my_ball)
            for i in range(s):
                if w - rects[i].x > 0 and w - rects[i].x < rects[i].a and z - rects[i].y > 0 and z - rects[i].y < rects[i].b:
                   rects.pop(i)
                   x = randint(100 + 100 * i, 200 + 100 * i)
                   y = randint(100, 500)
                   a = randint(20, 40)
                   b = randint(10, 25)
                   vx = randint(-10, 10)
                   vy = randint(-10, 10)
                   ax = randint(-1, 1)
                   ay = randint(-1, 1)
                   COLOR = COLORS[randint(0, 5)]
                   my_rect = Rect(x, y, vx, vy, ax, ay, a, b, COLOR)
                   rects.append(my_rect)
                   score += 1
            print('score:', score)
    for i in range(0, l, 1):
        for j in range(i+1, l, 1):
            if (balls[j].x-balls[i].x)**2+(balls[j].y-balls[i].y)**2 <= (balls[j].r+balls[i].r)**2:
                balls[j].count = 1
                balls[i].count = 1
                balls[i].vx1 = balls[j].vx
                balls[i].vy1 = balls[j].vx
                balls[j].vx1 = balls[i].vx
                balls[j].vy1 = balls[i].vy
                Ball.collision_ball(balls[i])
                Ball.collision_ball(balls[j])
    for i in range(0, l, 1):
        for j in range(i+1, l, 1):
            if (balls[j].x-balls[i].x)**2+(balls[j].y-balls[i].y)**2 < (balls[j].r+balls[i].r)**2:
                balls.pop(i)
                x = randint(100, 700)
                y = randint(100, 500)
                r = randint(30, 50)
                vx = randint(-10, 10)
                vy = randint(-10, 10)
                COLOR = COLORS[randint(0, 5)]
                count = 0
                my_ball = Ball(x, y, vx, vy, 0, 0, r, COLOR, count)
                balls.append(my_ball)
                balls.append(my_ball)


    for i in range(l):
        Ball.move(balls[i])
    for i in range(s):
        Rect.move(rects[i])
    for i in range(s):
        color = rects[i].COLOR
        x = rects[i].x
        y = rects[i].y
        a = rects[i].a
        b = rects[i].b
        new_rect(color, x, y, a, b)

    for i in range(l):
      color = balls[i].COLOR
      x = balls[i].x
      y = balls[i].y
      r = balls[i].r
      new_ball(color, x, y, r)
    for i in range(l):
        Ball.collision_wall(balls[i])
    for i in range(s):
        Rect.collision_wall(rects[i])
    for i in range(0, l, 1):
        balls[i].count = 0
        balls[i].vx1 = 0
        balls[i].vy1 = 0
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()