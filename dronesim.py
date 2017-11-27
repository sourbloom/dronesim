#!/usr/bin/env python2

import pygame
from pygame.locals import *

import random
import sys
import math
import time

FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600

DRONE_RADIUS = 15
DRONE_SPEED = 2

PERSPECTIVE_DIVIDER = 1.5

GRASS_COLOR = (10,100,20)
SHADOW_COLOR = (10/2,100/2,20/2)
LINE_COLOR = (10,100,20)

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def drone_distance(d1, d2):
    return distance(d1.x, d1.y, d1.z, d2.x, d2.y, d2.z)

def step_twords(val, target, step=1):
    if abs(val - target) <= step:
        return val
    elif val < target:
        return val + step
    elif val > target:
        return val - step

class Radio:
    def __init__(self, on_message):
        self.on_message = on_message

    def transmit(self, message):
        pass

class Drone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0
        self.color = (
            random.randrange(80, 250),
            random.randrange(80, 250),
            random.randrange(80, 250)
        )
        self.target_x = x
        self.target_y = y
        self.target_z = 100
        self.label = 'HI'
        self.counter = random.randrange(FPS)
        self.draw_shadow_line = False
        self.user_init()

    def draw_drone(self):
        hover_offset = (math.sin(pygame.time.get_ticks() / 200.0) * 10) - 10
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, int(self.y - self.z + hover_offset)),
            DRONE_RADIUS
        )
        font_w, font_h = FONT.size(str(self.label))
        screen.blit(
            FONT.render(str(self.label), True, (0, 0, 0)),
            (
                self.x - (font_w / 2),
                self.y - (font_h / 2) - self.z + hover_offset
            )
        )
        self.user_draw()

    def draw_shadow(self):
        if self.draw_shadow_line:
            pygame.draw.line(
                screen,
                SHADOW_COLOR,
                (self.x, self.y),
                (self.x, self.y - self.z),
            )
        pygame.draw.circle(
            screen,
            SHADOW_COLOR,
            (self.x, self.y),
            DRONE_RADIUS - min(int(self.z / 30), DRONE_RADIUS / 2)
        )

    def update(self):
        self.counter += 1
        while self.counter >= FPS:
            self. user_every_second()
            self.counter -= FPS

        # move towards the target
        self.x = step_twords(self.x, self.target_x, DRONE_SPEED)
        self.y = step_twords(self.y, self.target_y, DRONE_SPEED)
        self.z = step_twords(self.z, self.target_z, DRONE_SPEED)

        # don't go off screen or below the ground
        if self.x < 10                  : self.x = 10
        elif self.x > SCREEN_WIDTH - 10 : self.x = SCREEN_WIDTH - 10
        if self.y < 10                  : self.y = 10
        elif self.y > SCREEN_WIDTH - 10 : self.y = SCREEN_WIDTH - 10
        if self.z > 500                 : self.z = 500
        elif self.z < 10                : self.z = 10
        self.user_update()

    def user_init(self):
        pass

    def user_draw(self):
        pass

    def user_update(self):
        # you fill this in!
        pass

    def user_every_second(self):
        pass

def handle_events():
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_q or event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def draw(drones):
    screen.fill(GRASS_COLOR)
    for d in drones:
        d.draw_shadow()
    for d in drones:
        d.draw_drone()
    pygame.display.update()

def update(drones):
    for d in drones: d.update()

pygame.init()

FONT = pygame.font.Font(None, 20)

clock = pygame.time.Clock()

def run(drones):
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    while True:
        handle_events()
        update(drones)
        draw(drones)
        clock.tick(FPS)