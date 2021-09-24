import time


class Vehicle:
    def __init__(self, model, color, max_speed, condition):
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.condition = condition

    def to_go(self, km, av_speed):
        sleep_time = (km / av_speed) * 60
        for check in range(1, km + 1):
            time.sleep(sleep_time/km)
            if check <= km:
                print(f'{check} kilometre(s) have been driven')
        return f'{self.model.title()} is on place'

    def speed_check(self, expectation=100):
        if self.max_speed > expectation:
            return f'Max speed is higher then expected {expectation} by {self.max_speed - expectation} points!'
        else:
            return f'Expectation is higher then max speed {self.max_speed} by {expectation - self.max_speed} points!'


class Car(Vehicle):
    pass


class Truck(Vehicle):
    def __init__(self, model, color, max_speed, condition, material):
        Vehicle.__init__(self, model, color, max_speed, condition)
        self.material = material

    def capacity(self, length, width, height):
        truck_capacity = 2 * (length * width + length * height + width * height)
        return f'Capacity is {truck_capacity} centimetres^2'

    def appointment(self, city):
        return f'{self.color.title()} truck {self.model} was appointed to the city {city} to deliver ' \
               f'{self.material.lower()}.'


my_car = Car('BMW', 'Red', 200, 'Factory new')
bob_car = Car('Ford', 'Grey', 90, 'Good')
bill_truck = Truck('Man', 'Black', 120, 'Old', 'Furniture')


print(bill_truck.appointment('Vienna'))
print(bill_truck.capacity(6, 4, 7))
print(my_car.speed_check(100))
print(bob_car.speed_check(100))
print(my_car.to_go(60, 100))
