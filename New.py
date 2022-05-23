class Car:
    def __init__(self, current_speed):
        self.max_speed = 150
        self.current_speed = current_speed
    def get_this(self):
        return self.current_speed
    def set_accelerate(self, accelerate):
        if accelerate > self.max_speed:
            accelerate = self.max_speed - self.current_speed
            self.current_speed = self.current_speed + accelerate
        else:
            self.current_speed = self.current_speed + accelerate
    def set_brake(self, breake):
        if breake > 0:
            breake = 0
            self.current_break = breake
        else:
            self.current_break = breake

    def __repr__(self):
        print(f"the car's speed is {self.current_speed}, if I accelerate it will be {self.set_accelerate},if I  breake it will be {self.set_brake}")
    


new_car = Car(50)
new_car.set_brake(3)
new_car.set_accelerate(30)
print(new_car)

