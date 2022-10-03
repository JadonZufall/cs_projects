
def calc_n(n):
    if n == 0:
        return 1
    return (n * calc_n(n=(n - 1)))


def main() -> None:
    """ Main function of the program """
    print(calc_n(int(input("n = "))))
    return None


if __name__ == "__main__":
    main()
