class Sensor:
    def __init__(self, sensor_id, car_park_id, is_active = False):
        self.id = sensor_id
        self.car_park_id = car_park_id
        self.is_active = is_active

class EntrySensor(Sensor):
    pass

class ExitSensor(Sensor):
    pass