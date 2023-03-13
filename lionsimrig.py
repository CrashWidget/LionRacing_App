# this class will feature all aspects of rig, geometry, motion control, rig limits, height and length

class LionSimRig:
    # position of rig in relation to center of gravity (default unit inches)
    rig_position = [0, 0, 0]  # position_x, position_y, position z

    # current position of rig in relation to center of gravity (default unit radians)
    rig_rotation = [0, 0, 0]  # rot_x,rot_y,rot_z

    # general kinematic constants
    rig_COR = [0, 0, 0]

    # general rig smoothing charaters
    rig_filter = [0, 0, 0]  # wash rate, smooth rate, telemetry ignore limit (delta change)

    # rig_style
    # 1 - "3DOF"
    # 2 - "3DOF + Horizontal Surge"
    # 3 - "3DOF + Traction Loss"
    # 4 - "3DOF + Horizontal Surge + Traction Loss"

    num_actuators = 3

    def __init__(self, style):
        # create the rif actuators()
        self.ax1 = LionActuator(1, 0, 50)
        self.ax2 = LionActuator(2, -300, -2000)
        self.ax3 = LionActuator(3, 300, -2000)

        # TODO: make sure actuators are not doubled up in position

        self.rig_style = style  # how to perform the math

        # during rig setup perform the below actions
        self.determine_center_rotation()

    # check if things are duplicated
    def has_duplicates(self, iterable):
        seen = []  # create empty list for storing items that have been exposed
        for x in iterable:
            if x in seen:
                return True
            seen.append(x)
        return False

    def determine_kinematic_constants(self):  # function to determine rig setup
        self.determine_center_rotation()

    def determine_center_rotation(self):  # center of rotation
        if self.rig_style == 1:
            self.rig_COR[0] = abs(self.ax3.location_X - self.ax2.location_X) / 2.0
            self.rig_COR[1] = abs(self.ax3.location_Y - self.ax1.location_Y) / 2.0

    # calculate actuator positioning based on given telemerty input
    # pitch = radians
    # roll = radians
    # heave = mm/s^2
    # hor_surge = mm/s^2
    # long_surge = mm/s^2
    def calculate_pose(self, pitch, roll, heave, hor_surge, long_surge):
        # if the rig style is a DOF system use this function
        if self.rig_style == 1:
            pass
    # TODO: calculate actuators based on input pitch

    # TODO: calculate actuators based on input roll

    # TODO: calculate actuators based on input heave

    # TODO: calculate actuators based on input hor_surge

    # TODO: calculate actuators based on input long_surge



    def plot_rig(self):
        # TODO: create output function to plot 3D rig, movement and setup
        pass


class LionActuator:
    def __init__(self, spot, x, y, travel=100, lower_limit=0, upper_limit=75, park_position=0):
        self.location_spot = spot  # position of the actuator in the rig, (1,2,3,4,5,6,7,8)
        self.travel_available = 100  # available travel distance of actuator, (unit mm)
        self.lower_limit = 0
        self.upper_imit = self.travel_available

        self.location_X = x  # X coordinate of actuator location
        self.location_Y = y  # Y coordinate of actuator location

        self.position_Z = 0  # current position of stroke of actuator
        self.park_position = park_position


# class to connect and associate output with thanos controller
class LionThanosConnect:
    def __init__(self, com_port):
        self.com_port = None  # which come port should the serial connection be connected to
        self.baud_rate = None  # what baud rate is required by thanos
        self.is_connected = None  # flag to determine if thanos is connected
        self.str_tick_out = "X"  # string to hold output data to go to thanos

    def connect(self):
        # TODO: implement thanos connection device
        self.is_connected = True  # if connection was successful
        pass

    def disconnect(self):
        pass


if __name__ == '__main__':
    print("this is just to test lionsimrig")

    rig = LionSimRig(1)

    print("Center of Rotation", LionSimRig.rig_COR)
