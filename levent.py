class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"Marka: {self.make}, Model: {self.model}, Yıl: {self.year}"

class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, 4 Çeker: {self.four_wheel_drive}"

class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Maksimum Hız: {self.max_speed} km/s"

suv = OffRoadVehicle("Toyota", "Land Cruiser", 2021, True)

sports_car = SportsCar("Ferrari", "488 Spider", 2022, 330)

print(suv.display_info())
print(sports_car.display_info())
