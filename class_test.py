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


class Capacity:
    def capacity(self, length, width, height):
        truck_capacity = 2 * (length * width + length * height + width * height)
        return f'Capacity is {truck_capacity/10000} meters^2'


class Appointment:
    def appointment(self, city):
        return f'{self.color.title()} truck {self.model} was appointed to the city {city} to deliver ' \
               f'{self.material.lower()}.'



class Truck(Vehicle, Capacity, Appointment):
    def __init__(self, model, color, max_speed, condition, material):
        Vehicle.__init__(self, model, color, max_speed, condition)
        self.material = material


bill_truck = Truck('MAN', 'Black', 135, 'Bad', 'Fruits')

print(bill_truck.capacity(100, 100, 200))

print(bill_truck.speed_check(130))

