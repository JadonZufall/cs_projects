

def main() -> None:
    starting_price = {
        "Honda Civic": 22550,
        "Toyota Corolla": 20425,
        "Honda Accord": 26520,
        "Toyota Camry": 25945
    }
    adverage_mpg = {
        "Honda Civic": 35,
        "Toyota Corolla": 33,
        "Honda Accord": 33,
        "Toyota Camry": 32
    }
    city_range = {
        "Honda Civic": 384,
        "Toyota Corolla": 396,
        "Honda Accord": 444,
        "Toyota Camry": 442
    }
    highway_range = {
        "Honda Civic": 496,
        "Toyota Corolla": 502,
        "Honda Accord": 562,
        "Toyota Camry": 616
    }
    car_name = input("Enter car name... ")
    print(f"Starting Price = {starting_price[car_name]}$")
    print(f"Adv MPH = {adverage_mpg[car_name]}mpg")
    print(f"City Range = {city_range[car_name]} miles")
    print(f"Highway Range = {highway_range[car_name]} miles")


if __name__ == "__main__":
    main()
