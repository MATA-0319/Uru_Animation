from pico2d import *
import math
import random


running = True


class ZZZ:
    def __init__(self):
        self.image = load_image('zzz.png')
        self.ex, self.ey = 0, 0
        self.rot, self.num = 0, 0

    def update(self):
        self.ex = random.randint(0, 20)
        self.ey = random.randint(0, 20)
        self.rot = random.randint(0, 10)


class WWW:
    def __init__(self):
        self.image = load_image('www.png')
        self.ex, self.ey = 0, 0
        self.rot, self.num = 0, 0

    def update(self):
        self.ex = random.randint(0, 20)
        self.ey = random.randint(0, 20)
        self.rot = random.randint(0, 10)


class LOL:
    def __init__(self):
        self.image = load_image('lol.png')
        self.ex, self.ey = 0, 0
        self.rot, self.num = 0, 0

    def update(self):
        self.ex = random.randint(0, 20)
        self.ey = random.randint(0, 20)
        self.rot = random.randint(0, 10)


class Uru:
    def __init__(self):
        self.image = load_image('uru.png')
        self.rot, self.num = 0, 0

    def update(self):
        self.rot = math.sin(self.num) / 6
        self.num += 0.3


def handle_events():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


def draw_object():
    bg.draw(750, 500, 1500, 1000)
    zzz.image.rotate_draw(math.radians(zzz.rot - 5), 250 + zzz.ex, 850 + zzz.ey, 900, 900)
    www.image.rotate_draw(math.radians(www.rot - 5), 1200 +www.ex, 800 + www.ey, 900, 900)
    lol.image.rotate_draw(math.radians(lol.rot - 5), 200 + lol.ex, 150 + lol.ey, 900, 900)
    uru.image.rotate_draw(uru.rot, 750, 250, 1000, 1500)
    logo.draw(1450, 50, 200, 200)


def update_object():
    uru.update()
    zzz.update()
    www.update()
    lol.update()


open_canvas(1500, 1000)
bg = load_image('bg.png')
logo = load_image('logo.png')
zzz = ZZZ()
www = WWW()
lol = LOL()
uru = Uru()


while running:
    clear_canvas()

    draw_object()
    update_object()
    handle_events()
    update_canvas()   

    delay(0.01)

close_canvas()
