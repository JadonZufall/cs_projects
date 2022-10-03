

class Mountain:
    def __init__(self, name: str, state: str, mountain_range: str, elevation: int, coordinates: tuple[float, float]) -> None:
        self.__name: str = name
        self.__state: str = state
        self.__mountain_range: str = mountain_range
        self.__elevation: int = elevation
        self.__coordinates: tuple[float, float] = coordinates

    def print_data(self) -> None:
        print(f"{self.__name} | {self.__state} | {self.__mountain_range} | {self.__elevation} | {self.__coordinates[0]}N, {self.__coordinates[1]}W")
