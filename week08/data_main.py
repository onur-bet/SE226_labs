from data_package import cleaner
from data_package import analyzer


user_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8, 21): ")

raw_list = user_input.split(",")


cleaned_strings = cleaner.strip_whitespaces(raw_list)
cleaned_strings = [x for x in cleaned_strings if x != ""]


is_valid = True

for item in cleaned_strings:

    check_item = item.lstrip('-').replace('.', '', 1)

    if not check_item.isdigit():
        is_valid = False
        break


if not is_valid:
    print("Data Error: Please make sure you only enter numbers separated by commas.")
else:

    num_list = [float(x) for x in cleaned_strings]


    final_data = cleaner.remove_duplicates(num_list)


    if final_data:
        print(f"Cleaned and unique data: {final_data}")
        print(f"Mean: {analyzer.calculate_mean(final_data):.2f}")
        print(f"Maximum: {analyzer.find_maximum(final_data)}")
        print(f"Minimum: {analyzer.find_minimum(final_data)}")