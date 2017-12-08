#!/usr/bin/env python2
import math
import pygame
import random

import config
import util


class Drone:
    def __init__(self, x, y, z):
        self._max_speed = 3
        self._drone_size = 15
        self.x = x
        self.y = y
        self.z = z
        self.color = (
            random.randrange(80, 250),
            random.randrange(80, 250),
            random.randrange(80, 250)
        )
        self.x_accel = 0
        self.y_accel = 0
        self.z_accel = 0
        self.label = 'HI'
        self.counter = random.randrange(config.FPS)
        self.draw_shadow_line = False
        self.user_init()

    def draw_drone(self, screen):
        hover_offset = (math.sin(pygame.time.get_ticks() / 200.0) * 5) - 5
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y - self.z + hover_offset)),
            self._drone_size
        )
        font_w, font_h = util.FONT.size(str(self.label))
        screen.blit(
            util.FONT.render(str(self.label), True, (0, 0, 0)),
            (
                self.x - (font_w / 2),
                self.y - (font_h / 2) - self.z + hover_offset
            )
        )
        self.user_draw()

    def draw_shadow(self, screen):
        if self.draw_shadow_line:
            pygame.draw.line(
                screen,
                config.SHADOW_COLOR,
                (int(self.x), int(self.y)),
                (int(self.x), int(self.y - self.z)),
            )
        pygame.draw.circle(
            screen,
            config.SHADOW_COLOR,
            (int(self.x), int(self.y)),
            self._drone_size - min(int(self.z / 30), self._drone_size / 2)
        )

    def update(self):
        self.counter += 1
        while self.counter >= config.FPS:
            self. user_every_second()
            self.counter -= config.FPS

        # move towards the target
        self.x += util.clamp_minmax(0.0 + self.x_accel, 1.0) * self._max_speed
        self.y += util.clamp_minmax(0.0 + self.y_accel, 1.0) * self._max_speed
        self.z += util.clamp_minmax(0.0 + self.z_accel, 1.0) * self._max_speed

        # don't go off screen or below the ground
        self.x = util.clamp(self.x, 10, config.SCREEN_WIDTH - 10)
        self.y = util.clamp(self.y, 10, config.SCREEN_HEIGHT - 10)
        self.z = util.clamp(self.z, 10, config.WORLD_HEIGHT)
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
