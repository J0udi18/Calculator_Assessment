# Function goes here
def yes_no(question):

    error = "Please answer yes / no"

    valid = False
    while not valid:

        # ask question and put response in lowercase
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(error)
