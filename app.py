# Shares calculator used to calculate the share for sons and daughters from the total inheritance amount.
# This is the main file of this application.

import SharesCalculation as cal

try:
    # Get the inherited amount and details about family members
    inheritance_amount = float(input("Enter the total inheritance amount that a man left after deceased (float): "))
    sons = int(input("How many sons does he have (int)? "))
    daughters = int(input("How many daughters does he have (int)? "))
    spouse_alive = input("Is his spouse alive? (y for yes, n for no): ").lower()

    wife = 0
    if spouse_alive == "y":
        wife = int(input("How many wives does he have? "))

    mother_alive = input("Is his mother alive? (y for yes, n for no): ").lower()
    father_alive = input("Is his father alive? (y for yes, n for no): ").lower()

    # Call the calculate function from the Calculation module
    cal.calculate(inheritance_amount, sons, daughters, mother_alive, father_alive, wife)

    # Ensure the input variables are valid integers or floats
    sons = int(sons)
    daughters = int(daughters)
    inheritance_amount = float(inheritance_amount)
    wife = int(wife)

except ValueError:
    # Handle invalid input values
    print("The values must be an integer or a float!")
    exit()  # Exit the application
