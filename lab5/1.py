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

WIDTH = 1000
HEIGHT = 800

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
        if self.x - self.r <= 0 or self.x +self.r >= 800:
            self.vx = -self.vx/1.2
            self.vy = self.vy/1.1
        if self.y - self.r <= 0 or self.y +self.r >= 600:
            self.vy = -self.vy/1.2
            self.vx = self.vx / 1.1
        if self.x <= 0 or self.x >= 800 or self.y <= 0 or self.y >= 600:
            self.vx = 0
            self.vy = 0
            self.g=0
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
        self.x = x
        self.y = y
        self.length = 30
        self.width = 5
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        (x_mouse, y_mouse) = pygame.mouse.get_pos()
        new_ball = Ball(self.screen, 100, 580, 20, 10, 10 * math.tan(self.an), RED)
        self.an = math.atan2((-y_mouse + self.y), (x_mouse - self.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.f2_on = 0
        self.f2_power = 10
        self.length = 30
        self.width = 5

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-400) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREEN

    def draw(self):
        (x_mouse, y_mouse) = pygame.mouse.get_pos()
        self.x = 0
        self.y = 450
        self.an = math.atan2((-y_mouse + self.y), (x_mouse - self.x))
        length_up = self.length + self.f2_power
        width_half = self.width / 2
        pygame.draw.polygon(self.screen, self.color,
                            ((self.x - width_half * math.sin(self.an),
                              self.y - width_half * math.cos(self.an)),
                             (self.x + width_half * math.sin(self.an),
                              self.y + width_half * math.cos(self.an)),
                             (self.x + width_half * math.sin(self.an) + length_up * math.cos(self.an),
                              self.y + width_half * math.cos(self.an) - length_up * math.sin(self.an)),
                             (self.x - width_half * math.sin(self.an) + length_up * math.cos(self.an),
                              self.y - width_half * math.cos(self.an) - length_up * math.sin(self.an))))

    def power_up(self):
        global POWER
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                POWER = self.f2_power
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
s = 0
score = 0
Bullets = []
clock = pygame.time.Clock()
gun = Gun(screen, surf)
finished = False

while not finished:
    screen.fill(WHITE)
    f1 = pygame.font.Font(None, 50)
    text1 = f1.render(str(score), True, (180, 0, 0))
    text2 = f1.render('score:', True, (180, 0, 0))
    screen.blit(text1, (120, 50))
    screen.blit(text2, (10, 50))
    x1, y1 = pygame.mouse.get_pos()
    gun.draw()
    for i in range(l):
        Ball.draw(Targets[i])
        Ball.move(Targets[i])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
            (x_mouse, y_mouse) = pygame.mouse.get_pos()
            angle = math.atan2((-y_mouse + 450), (x_mouse - 20))
            new_ball1 = Ball(screen, 20, 450, 20, POWER/2.5 * math.cos(angle),  POWER/2.5 * math.sin(angle), GAME_COLORS[randint(0, 5)])
            Bullets.append(new_ball1)
            s = len(Bullets)
    for i in range(s):
        Ball.draw(Bullets[i])
        Ball.move(Bullets[i])
        for i in range(l):
           for j in range(s):
            if Targets[i].hittest(Bullets[j]) == True:
                Targets.pop(i)
                score += 1
                x = randint(100, 700)
                y = randint(100, 500)
                r = randint(30, 50)
                vx = randint(-2, 2)
                vy = randint(-10, 10)
                COLOR = GAME_COLORS[randint(0, 5)]
                my_ball = Target(screen, x, y, r, vx, vy, COLOR, points)
                Targets.append(my_ball)

    gun.power_up()
    for i in range(s):
        if Bullets[i].vx == 0:
            Bullets.pop(i)
    for i in range(l):
        if Targets[i].vx == 0:
            Targets.pop(i)
            score += 1
            x = randint(100, 700)
            y = randint(100, 500)
            r = randint(30, 50)
            vx = randint(-2, 2)
            vy = randint(-10, 10)
            COLOR = GAME_COLORS[randint(0, 5)]
            my_ball = Target(screen, x, y, r, vx, vy, COLOR, points)
            Targets.append(my_ball)
    pygame.display.update()

    clock.tick(FPS)
pygame.quit()