
def fib_number(n):
    if n == 0:
        # Base case 0.
        return 0
    elif n == 1:
        # Base case 1.
        return 1
    else:
        return fib_number(n - 1) + fib_number(n - 2)


def calculate_fib_number_up_to(n):
    print("\n")
    for i in range(0, n):
        print(fib_number(i), end=", ")


def main() -> None:
    """ Main function of the program """
    while True:
        try:
            calculate_fib_number_up_to(int(input("How many numbers would you like to calculate? ")))
            break
        except ValueError:
            print("Please enter a valid number")
            continue
    return None


if __name__ == "__main__":
    main()
