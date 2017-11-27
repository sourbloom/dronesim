#!/usr/bin/env python2

# to run this script:
#   sudo pip install pygame
#   python2 example.py

import dronesim
import random

class AlyDrone(dronesim.Drone):
    def user_init(self):
        # self.draw_shadow_line = True
        pass

    def user_update(self):
        self.label = int(self.z)

    def user_every_second(self):
        self.x_accel = random.random() * 2 - 1
        self.y_accel = random.random() * 2 - 1
        self.z_accel = random.random() * 2 - 1

drones = []
for i in range(10):
    drones.append(
        AlyDrone(
            random.randrange(200, 500),
            random.randrange(200, 500)
        )
    )

dronesim.run(drones)
