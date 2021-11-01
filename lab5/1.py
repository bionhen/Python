import math
from random import randint

import pygame
pygame.init()

FPS = 30

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
score = 0
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

surf = pygame.Surface((200, 100))

class Ball:
    def __init__(self, screen: pygame.Surface, x, y, r, vx, vy, color):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали

        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.g = 10
        self.vy = vy
        self.color = color
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy += -self.g/30
        self.x += self.vx
        self.y -= self.vy
        if self.x - self.r < 0 or self.x +self.r > 800:
            self.vx = -self.vx
        if self.y - self.r < 0 or self.y +self.r > 600:
            self.vy = -self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x-self.x)**2+(obj.y-self.y)**2 <= (self.r+obj.r)**2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen, surface):
        self.screen = screen
        self.surface = surf
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREEN

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        new_ball = Ball(self.screen, 100, 580, 20, 10, 10 * math.tan(self.an), RED)
        new_ball.r = 15
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-400) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREEN

    def draw(self, screen, surface, event):
        self.screen = screen
        self.an = math.atan((event.pos[1] - 400) / (event.pos[0] - 20))
        self.surface = surface
        pygame.draw.rect(
            self.surface,
            BLACK,
            (0, 500, 80, 20))
        pygame.transform.scale(self.surface, (10 * self.f2_power, 20))
        pygame.transform.rotate(self.surface, self.an)
        self.screen.blit(self.surface, (20, 400))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREEN


class Target(Ball):
    def __init__(self, screen, x, y, r, vx, vy, color, points):
     super().__init__(screen, x, y, r, vx, vy, color)
     self.points = points
     self.screen = screen

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
           obj: Обьект, с которым проверяется столкновение.
        Returns:
        Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (self.r + obj.r) ** 2:
           return True
        else:
           return False

    def hit(self, points):
        """Попадание шарика в цель."""
        self.points = points
        self.points += 1

    def draw(self):
        pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )


class Bullet(Ball):
    def __init__(self, screen, x, y, r, vx, vy, color):
     super().__init__(screen, x, y, r, vx, vy, color)
     self.points = points
     self.screen = screen

    def draw(self):
        pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )

screen = pygame.display.set_mode((WIDTH, HEIGHT))
points = 0

Targets = []
for i in range(randint(3, 6)):
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    vx = randint(-2, 2)
    vy = randint(-10, 10)
    COLOR = GAME_COLORS[randint(0, 5)]
    my_ball = Target(screen, x, y, r, vx, vy, COLOR, points)
    Targets.append(my_ball)
l = len(Targets)
bullet = 0
clock = pygame.time.Clock()
gun = Gun(screen, surf)
finished = False

while not finished:
    screen.fill(WHITE)
    for i in range(l):
        Ball.draw(Targets[i])
        Ball.move(Targets[i])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
            gun.draw(screen, surf, event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)

        #for i in range(l):
            #if Targets[i].hittest(new_ball) == True:
                #Targets.pop(i)
                #x = randint(100, 700)
                #y = randint(100, 500)
                #r = randint(30, 50)
                #vx = randint(-2, 2)
                #vy = randint(-10, 10)
                #COLOR = GAME_COLORS[randint(0, 5)]
                #my_ball = Target(screen, x, y, r, vx, vy, COLOR, points)
                #Targets.append(my_ball)
    gun.power_up()
    pygame.display.update()

    clock.tick(FPS)
pygame.quit()