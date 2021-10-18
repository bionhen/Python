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
balls = []


# Задает кортеж кортежей, с случайными параметрами
# color - цвет i-го шарика
# x - координата i-го шарика
# y - координата i-го шарика
for i in range(randint(6, 12)):
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    balls.append([color, x, y, r])
l = len(balls)


# задает кортеж кортежей из двух значений
# vx - скорость по x
# vy - скорость по y
v = []
for i in range(l):
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    v.append([vx, vy])

# функция, рисующая шарик цветом color, с центром в точке x, y, с радиусом r
def new_ball(color, x, y, r):
    circle(screen, color, (x, y), r)


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
              if (balls[i][1]-w)**2+(balls[i][2]-z)**2 < balls[i][3]**2:
                 score += 1
                 balls.pop(i)
                 v.pop(i)
                 x = randint(100, 700)
                 y = randint(100, 500)
                 r = randint(30, 50)*2**(0.005*score)
                 color = COLORS[randint(0, 5)]
                 balls.append([color, x, y, r])
                 vx = randint(-5-score, 5+score)
                 vy = randint(-5-score, 5+score)
                 v.append([vx, vy])
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