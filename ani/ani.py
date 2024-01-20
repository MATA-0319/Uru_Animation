
from pico2d import *
import math
import random


running = True
start = False
scene = 1
size = 0
acc = 0
shake_range = 100
shake_range2 = 200
timer = 0
timer2 = 0


def handle_events():
    global running, start, scene
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            if event.key == SDLK_SPACE:
                start = True
            if event.key == SDLK_RIGHT:
                scene += 1
            if event.key == SDLK_LEFT:
                scene -= 1


open_canvas(1500, 1000)
img1 = load_image('1.png')
img2 = load_image('2.png')
img3 = load_image('3.png')
b1 = load_image('bubble1.png')
b2 = load_image('bubble2.png')
bg = load_image('bg.png')


def animation():
    global size, scene, acc, shake_range, shake_range2, sx, sy, sr, timer, timer2

    timer += 1
    if timer > 200 and scene == 1:
        timer  = 0
        scene += 1


    if scene == 1:
        img1.draw(750, 500, 1500, 1167)
        b1.draw(500, 400, 1000, 800)

    if scene == 2:
        img2.draw(750, 500, 1500 + size, 1167 + size * 3 / 4 )
        size += acc
        acc += 100
        if size > 7000:
            scene += 1
            size = 7000

    if scene == 3:
        size = 0
        acc = 0
        if shake_range > 0:
            sx = random.randint(0, shake_range)
            sy = random.randint(0, shake_range)
            sr = random.randint(0, shake_range2)
            shake_range -= 1
            shake_range2 -= 2
            if shake_range < 0:
                shake_range = 0
                sx = 0
                sy = 0
                sr = 0

        bg.draw(750, 500)
        img3.rotate_draw(math.radians(sr) / 10, 750 + sx, 500 + sy, 1700, 1317)

        if shake_range == 0:
            timer2 += 1
            if timer2 > 50:
                b2.draw(1000, 600, 1000, 800)





while running:
    clear_canvas()
    handle_events()
    if start:
        animation()
    update_canvas()   

    delay(0.01)

close_canvas()