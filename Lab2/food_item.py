

class FruitItem:
    def __init__(self, name, price, retail_price, units_left):
        """ Constructor """
        self.__name = name
        self.__cost_price_per_unit = price
        self.__retail_price_per_unit = retail_price
        self.__units_left = units_left
        self.__units_sold = 0

    def set_name(self, name):
        """ Setter for name """
        self.__name = name

    def set_units_left(self, amount):
        """ Setter for units left """
        self.__units_left = amount

    def sell_one(self):
        """ Sell method """
        self.__units_sold += 1
        self.__units_left -= 1

    def print_info(self):
        """ Method for displaying info """
        print(f"name = {self.__name}")
        print(f"cost = {self.__cost_price_per_unit:.2f}$")
        print(f"retail = {self.__retail_price_per_unit:.2f}$")
        print(f"profit = {(self.__retail_price_per_unit - self.__cost_price_per_unit) * self.__units_sold:.2f}$")
        print(f"left = {self.__units_left}")
        print(f"sold = {self.__units_sold}")
