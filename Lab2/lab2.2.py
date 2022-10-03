from mountain import Mountain


def main() -> None:
    mount1: Mountain = Mountain(name="Denali", state="Alaska", mountain_range="Alask Range", elevation=20_310,
                                coordinates=(63.0690, 151.0063))
    mount2: Mountain = Mountain(name="Mount Foraker", state="Alaska", mountain_range="Alask Range", elevation=17_400,
                                coordinates=(62.9604, 151.3998))
    mount3: Mountain = Mountain(name="Mount Blackburn", state="Alaska", mountain_range="Wrangell Mountains",
                                elevation=16_390, coordinates=(61.7305, 143.4031))
    mount1.print_data()
    mount2.print_data()
    mount3.print_data()


if __name__ == "__main__":
    main()
