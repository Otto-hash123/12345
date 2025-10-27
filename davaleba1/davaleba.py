class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.brand} {self.model} ({self.year}) - მანქანა მუშა მდგომარეობაშია.")

    def info(self):
        print(f"ეს არის {self.year} წლის {self.brand} {self.model}.")



class SportsCar(Car):
    def __init__(self, brand, model, year, top_speed):
        super().__init__(brand, model, year)
        self.top_speed = top_speed

    def drive(self):
        print(f"გზაზე მიქრის {self.brand} {self.model} მისი სიჩქარეა {self.top_speed} km/h 🏎️💨")



class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def drive(self):
        print(f"{self.brand} {self.model} მოძრაობს ელექტრონულად 🔋")



class LuxuryCar(Car):
    def __init__(self, brand, model, year, features):
        super().__init__(brand, model, year)
        self.features = features

    def drive(self):
        print(f"{self.brand} {self.model} გთავაზობთ კომფორტულ მგზავრობას 🚘✨")
        print(f"მახასიათებლები: {self.features}")



class HybridCar(Car):
    def __init__(self, brand, model, year, battery_capacity, fuel_type):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        self.fuel_type = fuel_type

    def drive(self):
        print(f"{self.brand} {self.model} მუშაობს როგორც ელექტრონულად ⚡, ისე {self.fuel_type}-ზე ⛽")



if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2020)
    car1.drive()
    car1.info()

    sport = SportsCar("Ferrari", "F8", 2022, 340)
    sport.drive()

    tesla = ElectricCar("Tesla", "Model S", 2023, "100 kWh")
    tesla.drive()

    mercedes = LuxuryCar("Mercedes", "S-Class", 2021, "სავარძლის გათბობა, მასაჟორი, დისტანციური დაქოქვა")
    mercedes.drive()

    prius = HybridCar("Toyota", "Prius", 2024, "50 kWh", "ბენზინი")
    prius.drive()
