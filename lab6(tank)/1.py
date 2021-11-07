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
    def __init__(self, screen: pygame.Surface, x, y, r, vx, vy, color, g):
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
        self.g = g
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
        if self.x - self.r <= 0:
            self.vx = -self.vx/1.1
            self.vy = self.vy/1.1
            self.x += 10
        if self.x + self.r >= 800:
            self.vx = -self.vx / 1.1
            self.vy = self.vy / 1.1
            self.x -= 10
        if self.y - self.r <= 0:
            self.vy = -self.vy / 1.1
            self.vx = self.vx / 1.1
            self.y += 10
        if self.y + self.r >= 600:
            self.vy = -self.vy / 1.1
            self.vx = self.vx / 1.1
            self.y -= 10
        if self.x <= 0 or self.x >= 800 or self.y <= 0 or self.y >= 600:
            self.vx = 0
            self.vy = 0
            self.g = 0

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
    def __init__(self, screen, x2, y2):
        self.screen = screen
        self.surface = surf
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREEN
        self.x2 = x2
        self.y2 = y2
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
        new_ball = Ball(self.screen, 100, 580, 20, 10, 10 * math.tan(self.an), RED, g)
        self.an = math.atan2((-y_mouse + self.y2), (x_mouse - self.x2))
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

    def draw1(self, x2, y2):
        (x_mouse, y_mouse) = pygame.mouse.get_pos()
        self.x2 = x2
        self.y2 = y2
        self.an = math.atan2((-y_mouse + self.y2), (x_mouse - self.x2))
        length_up = self.length + self.f2_power
        width_half = self.width / 2
        pygame.draw.polygon(self.screen, self.color,
                            ((self.x2 - width_half * math.sin(self.an),
                              self.y2 - width_half * math.cos(self.an)),
                             (self.x2 + width_half * math.sin(self.an),
                              self.y2 + width_half * math.cos(self.an)),
                             (self.x2 + width_half * math.sin(self.an) + length_up * math.cos(self.an),
                              self.y2 + width_half * math.cos(self.an) - length_up * math.sin(self.an)),
                             (self.x2 - width_half * math.sin(self.an) + length_up * math.cos(self.an),
                              self.y2 - width_half * math.cos(self.an) - length_up * math.sin(self.an))))

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
    def __init__(self, screen, x, y, r, vx, vy, color, g):
     super().__init__(screen, x, y, r, vx, vy, color, g)
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

    def draw(self):
        pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )

    def collision(self, obj, p, q):
        if (self.x-obj.x)**2 + (self.y-obj.y)**2 <= (self.r + obj.r)**2:
            p = obj.vx
            q = obj.vy
            obj.vx = self.vx
            obj.vy = self.vy
            self.vx = p
            self.vy = q
            self.x -= (obj.x-self.x)/100


class Bullet(Ball):
    def __init__(self, screen, x, y, r, vx, vy, color, g):
     super().__init__(screen, x, y, r, vx, vy, color, g)
     self.screen = screen
    def draw(self):
        pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )

class Bomb(Ball):
    def __init__(self, screen, x, y, r, vx, vy, color, g):
     super().__init__(screen, x, y, r, vx, vy, color,g)
     self.screen = screen

    def draw(self):
        pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )


class Tank(Gun):
    def __init__(self, screen, x, vx, health):
        super().__init__(self, x, y)
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = vx
        self.health = health

    def draw(self):
        pygame.draw.rect(self.screen, BLACK, (self.x, 550, 50, 20))
        pygame.draw.rect(self.screen, BLACK, (self.x+10, 520, 30, 30))
        Tank.draw1(self, self.x + 25, 535)

    def move(self, d):
        if d == 1:
            self.x += self.vx

        elif d == -1:
             self.x += -self.vx

    def hit(self, obj):
        if obj.x > self.x and obj.x < self.x + 50 and obj.y<570 and obj.y > 550:
            self.health -= 10


screen = pygame.display.set_mode((WIDTH, HEIGHT))


points = 0

Targets = []
for i in range(randint(5, 7)):
    x = randint(100+100*2*i, 200+100*2*i)
    y = 100*i
    r = randint(30, 50)
    vx = randint(-10, 10)
    vy = 0
    COLOR = GAME_COLORS[randint(0, 5)]
    g = 0
    my_ball = Target(screen, x, y, r, vx, vy, COLOR, g)
    Targets.append(my_ball)
l = len(Targets)
bullet = 0
s = 0
score = 0
flag1 = flag2 = False
Bullets1 = []
Bullets2 = []
clock = pygame.time.Clock()
tank1 = Tank(screen, 300, 20, 100)
tank2 = Tank(screen, 500, 20, 100)
finished = False
fla = fld = False
fl_left = fl_right = False
Bombs = []


while not finished:
    s1 = len(Bullets1)
    s2 = len(Bullets2)
    screen.fill(WHITE)
    if tank2.health > 0:
        Tank.draw(tank2)
    if tank1.health > 0:
        Tank.draw(tank1)
    for i in range(l):
        x = Targets[i].x
        y = Targets[i].y
        r = 10
        vx = 0
        vy = 10
        g = 10
        new_bomb = Bullet(screen, x, y, r, vx, vy, BLACK, g)
        Bombs.append(new_bomb)

    f1 = pygame.font.Font(None, 50)
    text1 = f1.render(str(score), True, (180, 0, 0))
    text2 = f1.render('score:', True, (180, 0, 0))
    screen.blit(text1, (120, 50))
    screen.blit(text2, (10, 50))
    x1, y1 = pygame.mouse.get_pos()
    for i in range(l):
        Ball.draw(Targets[i])
        Ball.move(Targets[i])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fl_left = True
            elif event.key == pygame.K_a:
                fla = True
            elif event.key == pygame.K_RIGHT:
                fl_right = True
            elif event.key == pygame.K_d:
                fld = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fl_left = False
            if event.key == pygame.K_a:
                fla = False
            elif event.key == pygame.K_RIGHT:
                fl_right = False
            elif event.key == pygame.K_d:
                fld = False
            elif event.key == pygame.K_1:
                flag1 = True
                flag2 = False
            elif event.key == pygame.K_2:
                flag2 = True
                flag1 = False
        elif event.type == pygame.MOUSEMOTION:
            if flag2:
                Tank.targetting(tank2, event)
            if flag1:
                Tank.targetting(tank1, event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if flag2:
                Tank.fire2_start(tank2, event)
            if flag1:
                Tank.fire2_start(tank1, event)
        elif event.type == pygame.MOUSEBUTTONUP:
          if flag2:
            Tank.fire2_end(tank2, event)
            (x_mouse2, y_mouse2) = pygame.mouse.get_pos()
            angle2 = math.atan2((-y_mouse2 + 535), (x_mouse2 - tank2.x+30))
            new_ball2 = Bullet(screen, tank2.x+30, 535, 10, POWER/2.5 * math.cos(angle2),  POWER/2.5 * math.sin(angle2), GAME_COLORS[randint(0, 5)], 10)
            Bullets2.append(new_ball2)
          elif flag1:
            Tank.fire2_end(tank1, event)
            (x_mouse1, y_mouse1) = pygame.mouse.get_pos()
            angle1 = math.atan2((-y_mouse1 + 535), (x_mouse1 - tank1.x + 30))
            new_ball1 = Bullet(screen, tank1.x + 30, 535, 10, POWER / 2.5 * math.cos(angle1),
                               POWER / 2.5 * math.sin(angle1), GAME_COLORS[randint(0, 5)], 10)
            Bullets1.append(new_ball1)
    if flag2:
        if fl_right == True:
            Tank.move(tank2, 1)
        elif fl_left == True:
            Tank.move(tank2, -1)
    if flag1:
        if fld == True:
            Tank.move(tank1, 1)
        elif fla == True:
            Tank.move(tank1, -1)
    for i in range(s1):
        Bullet.draw(Bullets1[i])
        Bullet.move(Bullets1[i])
        for i in range(l):
           for j in range(s1):
            if Targets[i].hittest(Bullets1[j]) == True:
                Targets.pop(i)
                score += 1
                x = randint(100 + 100 * 2 * i, 200 + 100 * 2 * i)
                y = 100*i
                r = randint(30, 50)
                vx = randint(-10, 10)
                vy = 0
                COLOR = GAME_COLORS[randint(0, 5)]
                my_ball = Target(screen, x, y, r, vx, vy, COLOR, points)
                Targets.append(my_ball)
    for i in range(s2):
        Bullet.draw(Bullets2[i])
        Bullet.move(Bullets2[i])
        for i in range(l):
           for j in range(s2):
            if Targets[i].hittest(Bullets2[j]) == True:
                Targets.pop(i)
                score += 1
                x = randint(100 + 100 * 2 * i, 200 + 100 * 2 * i)
                y = 100*i
                r = randint(30, 50)
                vx = randint(-10, 10)
                vy = 0
                COLOR = GAME_COLORS[randint(0, 5)]
                my_ball = Target(screen, x, y, r, vx, vy, COLOR, points)
                Targets.append(my_ball)
    for i in range(l):
        for j in range(i+1, l, 1):
            Target.collision(Targets[i], Targets[j], 2, 2)
    for i in range(l):
        Bombs[i].move()
        Bombs[i].draw()
        if flag1:
            Tank.hit(tank1, Bombs[i])
        if flag2:
            Tank.hit(tank2, Bombs[i])
    if flag2:
        Tank.power_up(tank2)
    if flag1:
        Tank.power_up(tank1)
    for i in range(s1-1):
        if Bullets1[i].vx == 0:
            Bullets1.pop(i)
            s = s-1
    for i in range(s2-1):
        if Bullets2[i].vx == 0:
            Bullets2.pop(i)
            s = s-1
    for i in range(l):
        if Targets[i].vx == 0:
            Targets.pop(i)
            x = randint(100, 700)
            y = randint(100, 500)
            r = randint(30, 50)
            vx = randint(-10, 10)
            vy = 0
            COLOR = GAME_COLORS[randint(0, 5)]
            my_ball = Target(screen, x, y, r, vx, vy, COLOR, 0)
            Targets.append(my_ball)
    if flag2:
        for i in range(l):
            Tank.hit(tank2, Bombs[i])
    if flag1:
        for i in range(l):
            Tank.hit(tank1, Bombs[i])
    print(tank1.health)
    pygame.display.update()

    clock.tick(FPS)
pygame.quit()