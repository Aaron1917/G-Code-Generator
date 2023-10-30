class BOTCNC:

    def __init__(self):
        self.gcode = ""
        # Bot Config
        self.limit_x = 610
        self.limit_y = 450
        self.limit_z = 280
        self.vel_max_x = 500
        self.vel_max_y = 500
        self.vel_max_z = 500
        self.acc_max_x = 5
        self.acc_max_y = 5
        self.acc_max_z = 5

        # Code Config
        self.units = 1  # 0 IN | 1 mm
        self.type_coordinates = 0  # 0 absolutas | 1 incrementales
        self.shape = 0  # 0 Marco Real | 1 Tres Bolillo

        self.length_x = -590  # X mm
        self.length_y = -420  # Y mm 400
        self.initial_point = (-50, -20)

        self.distance = -50
        self.move_speed = 1000
        self.move_speed = 1400

        self.retraction = 10
        self.retraction_speed = 800

        self.seeding_z = -295  # -255 - 275
        self.seeder_coordinates = (-50, -480, -236) # -190 -210

    def initial_config(self):
        self.gcode += "G21\n" if self.units else "G20\n"
        self.gcode += "G91\n" if self.type_coordinates else "G90\n"
        self.gcode += "M5\nM9\n"

    def end_gcode(self):
        self.gcode += "M5\nM9\nM2"

    #def update_vel(self):
       # return f"$110={}"

    def marco_real(self):
        for x in range(self.initial_point[0], self.initial_point[0] + self.length_x, self.distance):
             for y in range(self.length_y, self.initial_point[1] - self.distance, -self.distance):
                print(y)
                self.gcode += f"G1 X{x} Y{self.seeder_coordinates[1]} F{self.move_speed}\n"
                self.gcode += f"G1 Z{self.seeder_coordinates[2]} F{self.retraction_speed}\nM8\n"
                self.gcode += f"G1 Z{self.seeder_coordinates[2] + self.retraction} F{self.move_speed}\n"
                self.gcode += f"G1 X{x} Y{y} F{self.move_speed}\n"
                self.gcode += f"G1 Z{self.seeding_z} F{self.move_speed}\nM9\n"
                self.gcode += f"G1 Z{self.seeder_coordinates[2] + self.retraction} F{self.move_speed}\n"