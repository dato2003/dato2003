from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        return "car is started"

    @abstractmethod
    def stop_engine(self):
        return "car is stopped"

class Car(Vehicle):
    def __init__(self,max_speed,corrent_speed):
        self.max_speed = max_speed
        self.corrent_speed = corrent_speed
    def start_engine(self):
        return "car is started"
    def stop_engine(self):
        return super().stop_engine()

class Sport_car(Car):
    def start_engine(self):
        return "car is started" ,self.max_speed
    def stop_engine(self):
        self.corrent_speed=0
        return super().stop_engine(), self.corrent_speed


mersedec = Car(40,20)
print(mersedec.stop_engine())
print(mersedec.start_engine())
Ferrary = Sport_car(300,110)
print(Ferrary.start_engine())  
print(Ferrary.stop_engine())  