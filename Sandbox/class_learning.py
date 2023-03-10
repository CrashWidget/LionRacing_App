class Example:
    "a basic example of a class"

    def b(self):
        return "this is an example class"


class Square:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


class PartsColor:
    #     creates a class
    def __init__(self):
        self.hood = "Blue"
        self.wheels = "Red"
        self.doors = "Green"


e = PartsColor()
print(e.hood)

r = Square(20, 2000)

print("rectangle area %d" % (r.area()))

c = Example()

print(c.b())


class TrafficLight:
    traffic_light_model = 'This is the always used model'

    def __init__(self, color):
        self.color = color

    def action(self):
        if self.color == "red":
            print('Stop and Wait')
        elif self.color == 'yellow':
            print('Prepare to stop')
        elif self.color == ('green'):
            print("GO")
        else:
            print('Stop Drinking')


yellow = TrafficLight('yellow')
green = TrafficLight('green')

yellow.action()

yellow.nextcolor = 'red'

print(yellow.nextcolor)

print(green.color)
print(green.traffic_light_model)
print(yellow.traffic_light_model)

# create class objects in a loop

for c in ['red', 'yellow', 'green']:
    c = TrafficLight(c)
    print(c.color)
