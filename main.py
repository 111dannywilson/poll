from funcs import (
    set_poll,
    set_options_limit,
    validate_input,
    all_options,
    options_data,
    get_percentage,
)

question = input("Your Question: ")
validate_input(question)
num_of_options = input("Number of options: ")
set_options_limit(num_of_options)
set_poll(question, all_options)


options_data()

# get_percentage()
