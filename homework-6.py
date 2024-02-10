#blood_pressure
class Heart:
    def usage (self,state):
        self.blood_pressure = 180
        if state/self.blood_pressure*100 > 70:
            return "high blood pressure"
        else:
            return "feeling good"
#Brain energy
class Brain:
    def usage (self,state):
        self.Brain_energy = 100
        if state/self.Brain_energy*100 > 90:
            return "tired"
        else:
            return "rested"
#person speed
class Leg:
    def usage (self,moving_speed):
        self.moving_speed = moving_speed
    @property
    def get (self):
        if self.moving_speed > 10:
            return "running"
        else:
            return "walking"
        
class person:
    def __init__(self):
        self.Heart_state = Heart()
        self.Brain_state = Brain()
        self.moving_speed = None

dato = person()
print(dato.Heart_state.usage(150))
print("the Brain is",dato.Brain_state.usage(90.1))

dato.moving_speed = Leg()
dato.moving_speed.usage(11)
print("person is ",dato.moving_speed.get)