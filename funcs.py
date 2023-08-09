def set_poll(question: str, options: list):
    """Setting a poll -> The question and options

    Args:
        question (str): Question to present
        options (list): list of options, must be more than one
    """
    if not question or question.strip() == "":
        return "Question field should not be empty"
    if len(options) <= 1:
        return "There should be more than one option"
    poll = {"poll": {"question": question, "options": options, "selected_options": []}}
    print(poll["poll"]["question"])
    for number, options in enumerate(poll["poll"]["options"]):
        number += 1
        print(f"{number}. {options}")
    print("Select number of poll option to vote")


def validate_input(question) -> str:
    if question.isdigit():
        print("Question should be a text")
        exit()


def set_options_limit(limit: str):
    if not limit.isdigit():
        print("Limit should be a number")
        exit()
    limit = int(limit)
    option_number = 0
    while len(all_options) < limit:
        option_number += 1
        option = input(f"Option{option_number}: ")
        all_options.append(option)


def options_data() -> dict:
    global number_of_votes
    """Storing options chosen

    Returns:
        dict: the count of each options chosen
    """
    vote = ""
    while vote != quit:
        vote = input("What do you choose: ")
        number_of_votes += 1
        if vote not in all_options:
            print("Option not provided, choose again")
            continue
        selected_options.append(vote)
        get_percentage()


def get_percentage():
    """Getting percentage of each option chosen"""
    # Get the number of occurrences in selected options
    for ch in selected_options:
        if ch not in selected_options:
            counter[ch] = "".join(selected_options).count(ch)
        counter[ch] = "".join(selected_options).count(ch)
    print(counter)
    print(
        f"People who chose {selected_options[-1]}: {selected_options[-1]} -> {counter[selected_options[-1]]} out of {number_of_votes}"
    )


all_options = []
selected_options = []
counter = {}
number_of_votes = 0
