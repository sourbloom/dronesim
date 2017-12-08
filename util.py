#!/usr/bin/env python2
import math
import pygame

pygame.init()
FONT = pygame.font.Font(None, 20)


def clamp_minmax(val, minmax):
    return max(min(val, minmax), -minmax)


def clamp(val, minimum, maximum):
    return max(min(val, maximum), minimum)


def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2-x1)**2.0 + (y2-y1)**2.0 + (z2-z1)**2.0)


def drone_distance(d1, d2):
    return distance(d1.x, d1.y, d1.z, d2.x, d2.y, d2.z)


def step_towards(val, target, step=1):
    if abs(val - target) <= step:
        return val
    elif val < target:
        return val + step
    elif val > target:
        return val - step
