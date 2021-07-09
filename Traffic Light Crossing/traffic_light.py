class Traffic_Light:
    def __init__(self, direction):
        self.direction = direction
        self.number_of_traffic = 0
        self.total_rotation_completed = 0
        self.red_light_timer = 0
        self.green_light_timer = 0
        self.status = None


