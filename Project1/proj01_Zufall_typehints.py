# Project No.: 1
# Author: Jadon Zufall
# Description: Project 1 for computer science 2 lab, this project entails of making a program which takes english to
#              spanish text file and then quizzes the user on the words contained within the text file.  Then outputs
#              the users results to a location of their choice.


"""
Personal check list (If curious about my thought process).
[X] Use dictionary to store key value pairs.
    * Dictionary is used in order to store the information read from the file.
[X] Use lists and tuples to examine and manipulate the items stored in them.
    * Both tuples and lists are used when passing values to and from functions.
[X] Use file processing and exception handling.
    * Files are processed and exceptions for FileNotFound and ValueError are both used.
[X] Use string slicing, operations, searching, testing and manipulating.
    * Sliced strings when separating keys and values.
    * Operations when comparing strings.
    * Searching when looking for strings in other strings.
    * Testing when comparing values.
    * Manipulating by clearing excess characters and setting string to lowercase.
[X] Use functions, parameter-passing, return values.
    * If I didn't programming this would have made me cry.
[X] Use if/elif/... else.
    * Of course not sure how'd I'd really do this without that.
[X] Use nesting loops/input validation.
    * This was used when validating the answers to the questions, don't see a need for it elsewhere.
[X] Use incremental development to write and test your program.
    * I may or may not have written this without testing it a single time, but hey it worked.
[X] NO GLOBAL VARIABLES ALLOWED.
    * Not a single one.
[X] Use proper Python naming conventions: variable_name, function_name.
    * This one was a little bit weird because it said that but then the function names provided later on were not in
    proper snake case so I was a little confused.  I just stuck to PEP8 as that is what I am used to but please let me
    know if you would like me to change this.
[X] Function names must describe what the function does.
    * I wrote doc strings just in case but I feel the function names are pretty good.
"""

# Import datetime in order to automatically fill the date if no input is provided.
from datetime import datetime

# Import sample in order to randomize the questions asked.
from random import sample


def get_file_name() -> str:
    """ Prompts user for file name and validate the user's input. """
    # Declare file_name as empty string, this will be our return value.
    file_name: str = ""

    # Set our input as invalid then loop until our input is valid.
    valid_input: bool = False
    while not valid_input:
        # Prompt user for the file name.
        file_name: str = input("Please enter a file name: ")

        # Ensure the file is a .txt file by checking that the string ends with the txt extension.
        if not file_name.endswith(".txt"):
            print("\nPlease enter a file ending with the extension .txt\n")
            continue

        # Ensure the file exists by opening the file in read mode then immediately closing the file.
        try:
            file = open(file_name, "r")
            file.close()
        except FileNotFoundError:
            print("Error, Invalid file name!")
            raise SystemExit

        # The user's input made it past all checks so the user's input is valid and we can end the while loop.
        valid_input: bool = True

    # Return the user's validated input.
    return file_name


def read_file_data(file_name: str) -> dict[str, list[str]]:
    """ Reads the data stored in the validated file_name, then configures the file into a dictionary. """
    # Declare file_data as an empty dictionary, this will be our return value.
    file_data: dict = dict()

    # Open the target file in read mode, read the lines, close the file.
    file = open(file_name, "r")
    file_lines: list = file.readlines()

    # Iterate over each line in the file and add it to the dictionary.
    for line in file_lines:
        # Strip the line of any tailing spaces or line breaks.
        stripped_line: str = line.strip()

        # Ensure the line contains the defined separator, if it does not then skip that line.
        if stripped_line.count(":") <= 0:
            continue

        # Separate the line, then separate the key and the values.
        split_line = stripped_line.split(":", 2)
        key: str = split_line[0].strip().lower()
        values: list[str] = split_line[1].split(",")

        # Clean up the values to make sure capitals and random spaces don't get in the way.
        values: list[str] = [word.strip().lower() for word in values]

        # Assign the found values to the dictionary.
        file_data[key]: list[str] = values

    # Return the filled dictionary.
    return file_data


def count_questions(file_data: dict[str, list[str]]) -> int:
    """ Counts the number of questions the program can ask from the data provided. """
    """
    # Declare question_count as an integer equal to zero, this will be our return value.
    question_count: int = 0

    # Create a list of values from the dictionary.
    file_data_values: list[list[str]] = list(file_data.values())

    # Iterate over each value and count the possible answers.
    for value in file_data_values:
        question_count += len(value)

    # Return the number of possible questions.
    return question_count
    """
    return len(list(file_data.keys()))


def get_user_data() -> tuple[str, str]:
    """ Prompts the user for name and date of the quiz. """
    # Declare name and date, these will be our return values.
    name: str = ""
    date: str = ""

    # Validate the users name.
    valid_name: bool = False
    while not valid_name:
        # Prompt the user for the name.
        name: str = input("Please enter your full name: ")

        # Check that the user provided some input.
        if name == "":
            print("Please enter a valid name.")
            continue

        # Name has passed all validation checks, so we exit the loop.
        valid_name: bool = True

    # Validate the users date input.
    valid_date: bool = False
    while not valid_date:
        # Prompt the user for the date.
        date: str = input("Please enter the date: ")

        # Check that the user provided some input, automatically use today's date if no date is provided.
        if date == "":
            date: str = datetime.now().strftime("%m/%d/%y")
            print(f"No date was provided, automatically assuming today's date {date}.")

        # Date has passed all validation checks, so we exit the loop.
        valid_date: bool = True

    # Returns the validated name and validated date in a tuple.
    return name, date


def get_amount_questions(number_questions: int) -> int:
    """ Prompts the user for the number of questions they wish to be quizzed on and validates the input. """
    # Declare question_amount as a integer equal to zero, this will be our return value.
    question_amount: int = 0

    # Validate that the number of questions the user is requesting is in range.
    valid_amount: bool = False
    while not valid_amount:
        # Prompt the user for the number of questions they wish to answer.
        string_amount: str = input("How many words would you like to be quizzed on? ")

        # Validate that the number can be converted to an integer.
        try:
            question_amount: int = int(string_amount)
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Validate that the number is within range of the data provided.
        if not (0 < question_amount <= number_questions):
            print(f"Please enter a valid number between 1 and {number_questions}.")
            continue

        # Question amount is valid and can break out of the validation loop.
        valid_amount: bool = True

    # Returns the validated amount of questions the user wishes to be asked.
    return question_amount


def get_questions_list(file_data: dict[str, list[str]], number_questions: int) -> list[str]:
    """ Selects random words from the keys provided in the file. """
    # Create a list containing all the keys from the file_data.
    file_data_keys: list[str] = list(file_data.keys())

    # Sample the keys from the file_data, getting the number of keys equal to the number of questions.
    file_data_sample: list[str] = sample(file_data_keys, number_questions)

    # Return the sample taken from the file_data's keys.
    return file_data_sample


def ask_questions(file_data: dict[str, list[str]], questions: list[str]) -> list[list[bool, str, list[str], list[str]]]:
    """ Prompts the user to respond to the questions selected by the program. """
    # Declares quiz_results as an empty two-dimensional list for storing quiz results.
    quiz_results: list[list[bool, str, list[str], list[str]]] = []

    # Iterate over each question and get all required responses.
    for question_number, question in enumerate(questions):
        # Print the english word the user needs to translate.
        print(f"\nEnglish word: {question}")

        # Get the list of answers for the question from the file_data.
        answer: list[str] = file_data[question]

        # Get the number of answers there are to this question.
        len_answer: int = len(answer)

        # Display to the user how many words they need to input.
        print(f"Enter {len_answer} equivalent Spanish word(s).")

        # Declare responses as an empty list to store user responses for this question.
        responses: list[str] = []

        # Iterate as many times as there are words.
        for word_number in range(0, len_answer):
            # Prompt the user to answer the question with the word_number + 1 so index matches.
            user_input: str = input(f"Word [{word_number + 1}]: ")

            # Append the user's response to the responses list, well also cleaning it up a little bit.
            responses.append(user_input.strip().lower())

        # Declare variable used to store if the user got the question correct or not.
        question_correct: bool = True

        # Iterate again validating the users responses, if clears for loop without triggering a check then the user's
        # response will be considered correct and question_correct's value won't change.
        for word_number in range(0, len_answer):
            # Checks to see if the user inputted the same response more then once.
            if responses.count(responses[word_number]) > 1:
                question_correct: bool = False
                break

            # Checks to see if the user's response was a valid answer.
            elif not responses[word_number] in answer:
                question_correct: bool = False
                break

        # Display if the user got the question correct or not.
        if question_correct:
            print("Correct!\n---")
        else:
            print("Incorrect!\n---")

        # Store the question responses in quiz_results for later use.
        quiz_results.append([question_correct, question, answer, responses])

    # Returns the users quiz_results.
    return quiz_results


def output_results(name: str, date: str, quiz_results: list, number_correct: int) -> None:
    """ Writes the results to user prompted file. """
    # Request file name from user.
    file_name: str = input("Enter an output file (or press enter to quit): ")

    # If the user doesn't enter anything then just exit the program.
    if file_name == "":
        return None
    elif file_name.strip() == "":
        return None

    # Open a context manager in case anything goes wrong here.
    with open(file_name, "w") as file:
        # Write the name and date of the user.
        file.write(f"Name: {name}\nDate: {date}\n")

        # Iterate over each question, writing the questions and the correct answers.
        for question in quiz_results:
            file.write(f"{question[1]}: {', '.join(question[2])}\n")

        # Write the users final score.
        file.write(f"Score: {number_correct} out of {len(quiz_results)} correct")

    # Return no value.
    return None


def main() -> None:
    """ Main function of the program. """
    # Displays welcome message.
    print("Welcome to the vocabulary quiz program.\n")

    # Prompt the user for a file name and validate it.
    file_name: str = get_file_name()

    # Read data from the file and convert it into a dictionary.
    file_data: dict[str, list[str]] = read_file_data(file_name=file_name)

    # Count the number of questions in the file_data.
    number_questions: int = count_questions(file_data=file_data)

    # Display the number of questions to the user.
    print(f"{number_questions} entries found.")

    # Get's the users name and date.
    user_data: tuple[str, str] = get_user_data()
    name: str = user_data[0]
    date: str = user_data[1]

    # Prompts the user from the amount of questions they wish to answer.
    question_amount: int = get_amount_questions(number_questions=number_questions)

    # Samples the file_data and selects random words to quiz the user on.
    questions: list[str] = get_questions_list(file_data=file_data, number_questions=question_amount)

    # Ask the user the quiz questions.
    quiz_results: list[list[bool, str, list[str], list[str]]] = ask_questions(file_data=file_data, questions=questions)

    # Display the users results.
    number_correct: int = 0
    for i in quiz_results:
        if i[0]:
            number_correct += 1
    print(f"{number_correct} out of {question_amount} correct.")

    # Output results to file.
    output_results(name=name, date=date, quiz_results=quiz_results, number_correct=number_correct)

    # Terminate the program with bye message.
    print("\nBye!")


# Execute program if ran as main.
if __name__ == "__main__":
    main()
