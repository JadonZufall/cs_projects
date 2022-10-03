from food_item import FruitItem


def main():
    """ Main function of the program. """

    """ Item # 1 code """
    fruit_item = FruitItem(name="Apple", price=1.0, retail_price=1.3, units_left=25)
    for i in range(0, 5):
        fruit_item.sell_one()
    fruit_item.set_name(name="Gala Apple")
    fruit_item.print_info()

    print("\n")

    """ Item # 2 code """
    other_item = FruitItem(name="Banana", price=0.5, retail_price=0.7, units_left=38)
    for i in range(0, 3):
        other_item.sell_one()
    other_item.set_units_left(amount=50)
    other_item.print_info()


if __name__ == "__main__":
    main()
