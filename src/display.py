class Display:
    def __init__(self, display_id, car_park_name, message = "", is_on = False):
        self.display_id = display_id
        self.car_park_name = car_park_name
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return f"Welcome to {self.car_park_name}!\nDisplay({self.display_id}):{self.message}"