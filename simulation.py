#!/usr/bin/env python2
import pygame
from pygame.locals import *
import sys

import config
import util


class Simulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), 0, 32)
        self.clock = pygame.time.Clock()
        pass

    def handle_events(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_q or event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def draw(self, drones):
        self.screen.fill(config.GRASS_COLOR)
        for d in drones:
            d.draw_shadow(self.screen)
        for d in drones:
            d.draw_drone(self.screen)
        pygame.display.update()

    def update(self, drones):
        for d in drones:
            d.update()
        return

    def run(self, drones):
        while True:
            self.handle_events()
            self.update(drones)
            self.draw(drones)
            self.clock.tick(config.FPS)
