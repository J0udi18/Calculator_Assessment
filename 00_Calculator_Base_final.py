import math
import pandas as pd
from termcolor import colored


# Function to colorize text for terminal output
def colored_message(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "blink": "\033[5m",
    }
    end_color = "\033[0m"  # Reset terminal color
    return colors.get(color.lower(), "") + text + end_color


# Function to check and retrieve a valid number input from the user
def num_check(question, error, num_type, exit_code='exit'):
    while True:
        try:
            response = input(colored_message(question, "yellow"))
            if response == exit_code:
                return exit_code
            else:
                response = num_type(response)
                if response <= 0:
                    print(colored_message(error, "red"))
                else:
                    return response
        except ValueError:
            print(colored_message(error, "red"))


# Function to get a yes/no response from the user
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "no", "y", "n"]:
            return response
        print(colored_message("Please enter either yes or no", "red"))


# Function to get coordinates from the user
def get_coordinate(prompt):
    while True:
        try:
            coordinate = input(colored_message(prompt, "yellow"))
            if coordinate.lower() == 'xxx':
                return None
            else:
                x, y = map(float, coordinate.split(','))
                return x, y
        except ValueError:
            print(colored_message("Invalid input. Please enter coordinates in the format 'x, y' (e.g., 3, 4)", "red"))


# Function to generate a statement with decorations
def statement_generator(statement, side_decoration, top_bottom_decoration):
    sides = side_decoration * 5
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = top_bottom_decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""


# Function to display instructions
def instructions():
    print("\033[128;1;4m****Instructions****\033[0m")
    print()
    print("Choose an option:")
    print("1. Distance between two points")
    print("2. Midpoint of two points")
    print("3. Gradient between two points")
    print("4. Area of a triangle given its vertices")
    print("Remember to leave a space between the two values.")
    print()
    return ""


# Function to calculate distance between two points
def distance_formula(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Function to calculate midpoint of two points
def midpoint(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2


# Function to calculate gradient (slope) between two points
def gradient(x1, y1, x2, y2):
    if x2 == x1:
        return None
    else:
        return (y2 - y1) / (x2 - x1)


# Function to calculate area of a triangle given its vertices
def area_triangle(x1, y1, x2, y2, x3, y3):
    return abs(0.5 * ((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))))


# Function to get user's choice of operation
def get_user_choice(used_before, previous_choice=None):
    choices = {
        "1": "Distance between two points",
        "2": "Midpoint of two points",
        "3": "Gradient between two points",
        "4": "Area of a triangle given its vertices"
    }
    if used_before == "yes" or used_before == "y":
        if previous_choice is not None:
            print("Your previous choice was:", choices[previous_choice])
    valid_choices = ['1', '2', '3', '4']
    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice in valid_choices:
            print("You chose:", choices[choice])
            print(colored_message("If you want to change your choice enter 'xxx'", "green"))
            return choice
        else:
            print(colored_message("Invalid choice. Please enter one of the valid choices.", "red"))
            print()


# Function to print ending messages
def print_ending_message():
    print()
    print(colored_message("Thank you for using the Coordinate Geometry Calculator!", "magenta"))
    statement_generator("Enjoy exploring coordinates with our calculator!", "*", "=")
    print(colored_message("📐✨ Happy calculating! ✨📐", "blue"))
    print()


# Main Routine
statement_generator("Welcome to the Coordinate Geometry Calculator", "!", "=")
print()

used_before = yes_no("Have you used the program before? ")
if used_before == "no" or used_before == "n":
    instructions()
elif used_before == "yes" or used_before == "y":
    print("**** Program launched! ****")
    print()

# DataFrame to store results
df = pd.DataFrame(columns=[
    'Points',
    'DMGE',
    'Answer'
])

valid_choices = ['1', '2', '3', '4']
previous_choice = None

# List to hold results for printing and file writing
results_to_write = []

while True:
    choice = get_user_choice(used_before, previous_choice)
    previous_choice = choice

    # Container for new row
    new_row = {
        'Points': '',
        'DMGE': '',
        'Answer': ''
    }

    if choice == '1':
        print("\nEnter coordinates of the two points:")
        point1 = get_coordinate("Enter coordinates of first point (x1, y1): ")
        if not point1: continue
        point2 = get_coordinate("Enter coordinates of second point (x2, y2): ")
        if not point2: continue
        x1, y1 = point1
        x2, y2 = point2
        distance = distance_formula(x1, y1, x2, y2)
        result = f"{distance:.2f}"
        print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: {result}")
        new_row.update({
            'Points': f"({x1}, {y1}) and ({x2}, {y2})",
            'DMGE': 'Distance',
            'Answer': result
        })
        results_to_write.append(f"Distance: {result}")

    elif choice == '2':
        print("\nEnter coordinates of the two points:")
        point1 = get_coordinate("Enter coordinates of first point (x1, y1): ")
        if not point1: continue
        point2 = get_coordinate("Enter coordinates of second point (x2, y2): ")
        if not point2: continue
        mid = midpoint(*point1, *point2)
        result = f"({mid[0]:.2f}, {mid[1]:.2f})"
        print(
            f"The midpoint of the line segment between ({point1[0]}, {point1[1]}) and ({point2[0]}, {point2[1]}) is: {result}")
        new_row.update({
            'Points': f"({point1[0]}, {point1[1]}) and ({point2[0]}, {point2[1]})",
            'DMGE': 'Midpoint',
            'Answer': result
        })
        results_to_write.append(f"Midpoint: {result}")

    elif choice == '3':
        print("\nEnter coordinates of two points on the line:")
        point1 = get_coordinate("Enter coordinates of first point (x1, y1): ")
        if not point1: continue
        point2 = get_coordinate("Enter coordinates of second point (x2, y2): ")
        if not point2: continue
        grad = gradient(*point1, *point2)
        if grad is not None:
            result = f"{grad:.2f}"
            print(
                f"The gradient of the line passing through ({point1[0]}, {point1[1]}) and ({point2[0]}, {point2[1]}) is: {result}")
        else:
            result = "Undefined"
            print(
                f"The line passing through ({point1[0]}, {point1[1]}) and ({point2[0]}, {point2[1]}) is vertical. Gradient is undefined.")
        new_row.update({
            'Points': f"({point1[0]}, {point1[1]}) and ({point2[0]}, {point2[1]})",
            'DMGE': 'Gradient',
            'Answer': result
        })
        results_to_write.append(f"Gradient: {result}")

    elif choice == '4':
        print("\nEnter coordinates of the three vertices of the triangle:")
        point1 = get_coordinate("Enter coordinates of first vertex (x1, y1): ")
        if not point1: continue
        point2 = get_coordinate("Enter coordinates of second vertex (x2, y2): ")
        if not point2: continue
        point3 = get_coordinate("Enter coordinates of third vertex (x3, y3): ")
        if not point3: continue
        area = area_triangle(*point1, *point2, *point3)
        result = f"{area:.2f}"
        print(
            f"The area of the triangle with vertices ({point1[0]}, {point1[1]}), ({point2[0]}, {point2[1]}), ({point3[0]}, {point3[1]}) is: {result}")
        new_row.update({
            'Points': f"({point1[0]}, {point1[1]}) to ({point2[0]}, {point2[1]}) to ({point3[0]}, {point3[1]})",
            'DMGE': 'Area',
            'Answer': result
        })
        results_to_write.append(f"Area: {result}")

    # Append the new row to the DataFrame if any new values
    if any(new_row.values()):
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # Ask user if they want to continue
    continue_choice = yes_no("\nDo you want to perform another calculation? (yes/no): ")
    if continue_choice in ["no", "n"]:
        print_ending_message()
        break
    elif continue_choice in ["yes", "y"]:
        print("\nReturning to main menu...\n")
        used_before = yes_no
    else:
        print(colored_message("Invalid choice. Exiting program.", "red"))
        break

# Export DataFrame to a CSV file
df.to_csv('coordinate_geometry_calculations.csv', index=False)
print("\nResults have been saved to 'coordinate_geometry_calculations.csv'.")

# Write results to a text file with better formatting
file_name = "coordinate_geometry_calculations.txt"
with open(file_name, "w") as text_file:
    for index, row in df.iterrows():
        text_file.write(f"Points: {row['Points']}\n")
        text_file.write(f"DMGE: {row['DMGE']}\n")
        text_file.write(f"Answer: {row['Answer']}\n")
        text_file.write("\n" + "=" * 50 + "\n")

    # It adds a separator line at the bottom
    text_file.write("=" * 50 + "\n")

print("Results have been written to 'coordinate_geometry_calculations.txt'.")
print("\n" + "=" * 50)
print(df.to_string(index=False))
