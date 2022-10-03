import random


def main() -> None:
    values_in_dict = {
        "Capital of Nigera is Lagos": False,
        "Capital of Madagascar is Antananarivo": True,
        "Capital of Mali is Bamkako": True,
        "Capital of Burundi is Bujumbura": True,
        "South Africa has 3 capital cities": True,
        "Capital of Tanzania is Conakry": False,
        "Capital of Zambia is Kampala": False
    }
    convert_input = {
        "1": True, "2": False
    }
    score = 0
    questions_list = list(values_in_dict.keys())
    random.shuffle(questions_list)
    for i in range(0, 3):
        validating = True
        while validating:
            print(questions_list[i])
            user_input = input("1 for true, 2 for false\n")
            try:
                if values_in_dict[questions_list[i]] is convert_input[user_input]:
                    print("Correct")
                    validating = False
                    score += 1
                else:
                    print("Incorrect")
                    validating = False
            except KeyError:
                print("Please select a valid option 1 or 2.")

    print(f"Your final score was {score}/3")


if __name__ == "__main__":
    main()
