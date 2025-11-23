class CarPark:
    def __init__(self, name, location, capacity, number_plates = None, displays = None):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.number_plates = number_plates or []
        self.displays = displays or []

    def __str__(self):
        return f"Car Park: {self.name}\nLocation: {self.location}\nCapacity: {self.capacity}"