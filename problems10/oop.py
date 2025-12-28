# # class Car:
# #     def __init__(self,brand,model):
# #         self.brand=brand
# #         self.model=model

# # my_car=Car("Toyota","Innova")
# # print(my_car.brand,my_car.model)

# #Question 2 Add a method to the car class that displays full name of the car(brand and model)

class Car:
    total_car=0
    
    def __init__(self,brand,model):
        self.brand=brand
        self.__model=model
        Car.total_car+=1
         
    def full_name(self):
        return f"{self.brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or disel"
    
    @staticmethod
    def general_desccription():
        return "CARS AND MACHINES"
    @property
    def model(self):
        return self.__model

mycar=Car("Abc","Pqr")
# print(mycar.full_name())

# print(mycar.model)

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    
    def fuel_type(self):
        return "Electricity"
myEcar=ElectricCar("Tesla","Model S","85kWH")
print(isinstance(myEcar,Car))
print(isinstance(myEcar,ElectricCar))

# print(myEcar.fuel_type())

# print(Car.total_car)
class Battery:
    def battery_info(self):
        return "Lithium Ion battery"
        

class Engine:
    def engine_info(self):
        return "This is engine"

class EV(Battery,Engine,Car):
    pass

my_ev_car=EV("Tesla","Model Y")
print(my_ev_car.engine_info())
print(my_ev_car.battery_info())