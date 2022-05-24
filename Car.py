class Car:
    def __init__(self, current_speed):
        self.max_speed = 150
        self.current_speed = current_speed
    def __repr__(self):
         return f"the curent speed is {self.current_speed}"
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
           self.current_speed = breake
        else:
            self.current_speed = breake

new_car = Car(50)
print(new_car)
new_car.set_accelerate(40)
print(new_car)
new_car.set_brake(3)
print(new_car)




