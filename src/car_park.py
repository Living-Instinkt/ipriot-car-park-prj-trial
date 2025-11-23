class CarPark:
    def __init__(self, name, number_plates, capacity, displays):
        self.name = name
        self.capacity = capacity
        self.number_plates = number_plates or []
        self.displays = displays or []