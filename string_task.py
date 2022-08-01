# Since strings are immutable objects, we create an empty list to store data for a new string there.
new_list = []


def convert_string(string):
    # We cycle through the line to find out the number of repetitions of letters
    for symbol in string.lower():
        # If the letter is repeated once, then insert it into the list (
        if string.count(symbol) == 1:
            new_list.append("(")
        # If the letter is repeated several times, then we insert it into the list )
        else:
            new_list.append(")")
    # Turning the contents of the list into a string
    new_str = "".join(new_list)
    # Output the resulting string
    print(new_str)


if __name__ == "__main__":
    input_user_string = input("Enter the text: ")
    convert_string(input_user_string)
