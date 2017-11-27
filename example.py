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
        self.label = self.z

    def user_every_second(self):
        self.target_x += random.randrange(-50, 50)
        self.target_y += random.randrange(-50, 50)
        self.target_z = random.randrange(50, 300)

drones = []
for i in range(20):
    drones.append(
        AlyDrone(
            random.randrange(200, 500),
            random.randrange(200, 500)
        )
    )

dronesim.run(drones)
