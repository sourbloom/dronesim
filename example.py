#!/usr/bin/env python2

# to run this script:
#   sudo pip install pygame
#   python2 example.py

import dronesim
import random


class RadioDrone(dronesim.drone.Drone):
    def send(self):
        for d in drones:
            if d != self:
                d.receive(dronesim.util.drone_distance(self, d))

    def receive(self, distance):
        pass


class SendDrone(RadioDrone):
    def user_init(self):
        self.label = 'BEACON'
        self.delay = 0

    def user_update(self):
        if self.label == ':O':
            self.delay += 1
            if self.delay >= 15:
                self.delay = 0
                self.label = ':|'

    def user_every_second(self):
        self.send()
        self.label = ':O'


class ListenDrone(RadioDrone):
    def user_init(self):
        self.label = '?'
        self.last_dist = 9999

    def receive(self, distance):
        if distance <= 70:
            self.x_accel = 0
            self.y_accel = 0
            self.z_accel = 0
            self.label = ':)'
        else:
            self.label = int(distance)
            if distance >= self.last_dist:
                self.x_accel = (random.random() * 2 - 1) * 0.3
                self.y_accel = (random.random() * 2 - 1) * 0.3
                self.z_accel = (random.random() * 2 - 1) * 0.3
        self.last_dist = distance


if __name__ == "__main__":
    drones = []

    drones.append(
        SendDrone(
            dronesim.config.SCREEN_WIDTH / 2,
            dronesim.config.SCREEN_HEIGHT / 2,
            100
        )
    )

    for i in range(12):
        drones.append(
            ListenDrone(
                random.randrange(0, dronesim.config.SCREEN_WIDTH),
                random.randrange(0, dronesim.config.SCREEN_HEIGHT),
                100
            )
        )

    sim = dronesim.simulation.Simulation()
    sim.run(drones)
