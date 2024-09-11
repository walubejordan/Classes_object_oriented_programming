class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"The {self.model} is now going {self.speed} km/h")

# Creating instances of the Car class
car1 = Car("Toyota", "Red", 50)
car2 = Car("Honda", "Blue", 60)

car1.accelerate()  # Output: The Toyota is now going 60 km/h
car2.accelerate()  # Output: The Honda is now going 70 km/h