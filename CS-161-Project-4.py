#Joshua Isakson
#6/5/2021


class Car: 
    def __init__ (self, color, speed, brand, model):
        self.brand = brand 
        self.color = color 
        self.speed = speed 
        self.model = model




s = Car(1,2,3,4)

print(s.brand)
print(s.model)
print(s.speed)
print(s.color)