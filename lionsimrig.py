# this class will feature all aspects of rig, geometry, motion control, rig limits, height and length


class LionSimrig:
    # position of rig in relation to center of gravity (default unit inches)
    rig_position = {0, 0, 0}  # position_x, position_y, position z

    # current position of rig in relation to center of gravity (default unit radians)
    rig_rotation = {0, 0, 0}  # rot_x,rot_y,rot_z

    # general kinematic constants
    rig_COR = {0, 0, 0}

    # rig_style
    # 1 - "3DOF"
    # 2 - "3DOF + Horizontal Surge"
    # 3 - "3DOF + Traction Loss"
    # 4 - "3DOF + Horizontal Surge + Traction Loss"

    num_actuators = 3

    def __init__(self, style):
        # create the rif actuators()
        self.ax1 = LionActuator(1)
        self.ax2 = LionActuator(2)
        self.ax3 = LionActuator(3)

        # tracking of actuator height and position
        self.rig_style = style   # how to perform the math
        pass

    def determine_kinematic_constants(self):  # function to determine rig setup
        self.determine_center_rotation()

    def determine_center_rotation(self):  # center of rotation
        if self.rig_style == 1:
            self.rig_COR[0] = abs(self.ax3.location_X - self.ax2.location_X) / 2.0
            self.rig_COR[1] = abs(self.ax3.location_Y - self.ax1.location_Y) / 2.0


class LionActuator:
    def __init__(self, spot):
        self.location_spot = spot  # position of the actuator in the rig, (1,2,3,4,5,6,7,8)
        self.travel_available = 100  # available travel distance of actuator, (unit mm)
        self.location_X = 1  # X coordinate of actuator location
        self.location_Y = 1  # Y coordinate of actuator location

        self.position_Z = 0  # current position of stroke of actuator
        self.park_position = 0


if __name__ == '__main__':
    print("this is just to test lionsimrig")

    rig = LionSimrig(1)

    print(rig.ax1.location_X)
