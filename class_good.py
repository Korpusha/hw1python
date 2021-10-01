"""Realization of buying the products"""


class Goods:
    def __init__(self, price, name, unit_of_measurement, category):
        self.price = price
        self.category = category
        self.name = name
        self.unit_of_measurement = unit_of_measurement

    def is_eatable(self):
        """
        Checks the product on it`s edibility.
        Allowed only categories to check: 'supply', 'household chemistry', 'alcohol'
        Also used to help method totally_eatable in class Basket

        """
        allowed_category = ('supply', 'household chemistry', 'alcohol')
        if self.category in allowed_category and self.category != 'household chemistry':
            return True
        return False

    def price_total(self):
        """
        Spot the price of the product depended upon its units.
        If kg, then it`s default price
        If 'by number', then it multiplies the price with its number
        Also used to help method total in class Basket

        """
        not_allowed_units = ('kg', 'kilogrammes', 'kilo', 'kilogram', 'kilogramme')
        for i in self.unit_of_measurement.split():
            if i in not_allowed_units:
                return self.price
        if self.unit_of_measurement not in not_allowed_units:
            our_num = int("".join(filter(str.isdigit, self.unit_of_measurement)))  # gets number out of string
            return self.price * our_num


class Basket(Goods):
    def __init__(self, what_in):
        self.what_in = what_in

    def total(self):
        """Same as price_total method, but sums them all together"""
        total_sum = [Goods.price_total(i) for i in self.what_in]
        return sum(total_sum)

    def totally_eatable(self):
        """Same as is_eatable method, but if at least one uneatable found - returns 'Uneatable'"""
        totally_eatable = [Goods.is_eatable(i) for i in self.what_in]
        if False in totally_eatable:
            return 'Uneatable'
        return 'Eatable'


first_good = Goods(5, 'juice', '3 things', 'supply')
second_good = Goods(15, 'ham', '2 things', 'supply')
third_good = Goods(50, 'whiskey', '1 thing', 'alcohol')
fourth_good = Goods(25, 'shampoo', '2 things', 'household chemistry')
fifth_good = Goods(30, 'buckwheat', '2 kilo', 'supply')
my_basket = Basket((first_good, second_good, third_good, fourth_good, fifth_good))

print(fourth_good.is_eatable())  # False
print(my_basket.total())  # 175
print(my_basket.totally_eatable())  # Uneatable
