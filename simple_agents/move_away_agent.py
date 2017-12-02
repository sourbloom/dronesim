#!/usr/bin/env python2

import dronesim

class MoveAwayDrone(dronesim.Drone):
    # self.x_accel float -1 <-> +1
    # self.y_accel float -1 <-> +1
    # self.z_accel float -1 <-> +1
    #self.label  text on drone
    def user_init(self):
        """

        :return:
        """
        self.label = "XD"
        pass

    def user_draw(self):
        """
        
        :return: 
        """
        pass

    def user_update(self):
        """

        :return:
        """
        pass

    def user_every_second(self):
        """

        :return:
        """
        pass
