import turtle as tt

print('''This program takes in your inputs and turn them into a star.
You can choose the length of a line of a star, the drawing speed, its color and its drawing mode and parameters.
Simply type in 'sp' and specify the point angle of the star's tentacles or hands. Or, type in 'sb' to draw with 
the base polygon's angle instead. Or just type sn in the mode  and specify the side number in the parameters
to draw with the side number of the base polygon instead. This program only works with odd numbered base polygons
for now''')

class create_fractal_star:
    def __init__(self, side_length, parameter, mode, speed, color1, color2):
        self.color1 = color1
        self.color2 = color2
        self.speed = speed
        self.parameter = parameter
        self.side_length = side_length
        self.mode = mode

        self.angle_by_side_number = ((360 / self.parameter)*2)
        self.angle_by_point_angle = (180 - self.parameter) 
        self.side_number_by_point_angle = int(360 / (self.parameter * 2))
        self.angle_by_base_polygon_angle = (180 - self.parameter) * 2
        self.side_number_by_base_polygon_angle = int(360 / ((180 - self.parameter) / 2))

        self.center_star()
        if self.mode == 'sp':
            self.side_mode_by_point_angle(self.side_length)
        elif self.mode == 'sb':
            self.side_mode_by_base_polygon_angle(self.side_length)
        elif self.mode == 'sn': 
            self.angle_mode_by_side_number(self.side_length)
        self.done()
        

    def side_mode_by_point_angle(self, side_length):
        tt.speed(self.speed)
        tt.color(self.color1, self.color2)
        if side_length <= 10:
            return
        else:
            tt.begin_fill()
            for i in range(self.side_number_by_point_angle):
                tt.forward(side_length)
                self.side_mode_by_point_angle(side_length / ((3 / 5) * self.parameter))
                tt.right(self.angle_by_point_angle)
            tt.end_fill()

    def side_mode_by_base_polygon_angle(self, side_length):
        tt.speed(self.speed)
        tt.color(self.color1, self.color2)
        if side_length <= 10:
            return
        else:
            tt.begin_fill()
            for i in range(self.side_number_by_base_polygon_angle):
                tt.forward(side_length)
                self.side_mode_by_base_polygon_angle(side_length / ((3 / 5) * self.parameter))
                tt.right(self.angle_by_base_polygon_angle)
            tt.end_fill()

    def angle_mode_by_side_number(self, side_length):
        tt.speed(self.speed)
        tt.color(self.color1, self.color2)
        if side_length <= 10:
            return
        else:
            tt.begin_fill()
            for i in range(self.parameter):
                tt.forward(side_length)
                self.angle_mode_by_side_number(side_length / ((3 / 5) * self.parameter))
                tt.right(self.angle_by_side_number)
            tt.end_fill()

    def center_star(self):
        tt.penup()
        tt.goto(-self.side_length / 2, self.side_length / 2.5)
        tt.pendown()

    def done(self):
        tt.done()

s_l = int(input('Side length: '))
mo = input('Mode: ')
if mo == 'sp':
    pm = int(input('What is the angle of one of the hands of the star: '))
elif mo == 'sb':
    pm = int(input('What is the angle of the base polygon for the star: '))
elif mo == 'sn':
    pm = int(input('What is the number of sides on your base polygon?'))
spd = int(input('Speed: '))
clr1 = input('Foreground color: ')
clr2 = input('Fill color: ')

pegasus = tt.Turtle()
pegasus = create_fractal_star(s_l, pm, mo, spd, clr1, clr2)