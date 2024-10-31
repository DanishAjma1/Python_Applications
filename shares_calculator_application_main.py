import shares_application_output as output

def calculate_share_and_deduct_from_total(amount, ratio, count=1):
    part = ratio * amount
    amount -= part * count
    return part, amount

# Function to calculate shares when there are sons or daughters
def calculate_shares_for_spouse_with_sons_or_daughters(amount, mother, father, wife):
    wife_count = wife
    wife = bool(is_wife_alive(wife))
    print(mother,father,wife)
    wife_amount = 0
    father_amount = 0
    mother_amount = 0

    # Check if wife, mother, and father are alive and calculate their respective shares
    if wife and mother and father:  # Assuming these variables indicate if they are alive
        wife_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 8, wife_count)
        mother_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 6)
        father_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 6)

    elif wife and mother:
        wife_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 8, wife_count)
        mother_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 6)

    elif wife and father:
        wife_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 8, wife_count)
        father_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 6)

    elif mother and father:
        mother_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 6)
        father_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 6)

    elif mother:
        mother_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 6)

    elif father:
        father_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 6)

    elif wife:
        wife_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 8, wife_count)

    else:
        print("If there is nothing for you to calculate the inheritance, what are you doing here...?")

    # Output the calculated shares
    output.diplay_shares_of_spouse_and_parents(mother_amount, father_amount, wife_amount, father, wife, mother)
    return amount


def calculate_shares_for_spouse_without_sons_or_daughters(amount, mother, father, wife):
    wife_count = wife
    wife = bool(is_wife_alive(wife))
    wife_amount = 0
    father_amount = 0
    mother_amount = 0

    # Check if wife, mother, and father are alive and calculate their respective shares
    if wife and mother and father:
        wife_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 4, wife_count)
        mother_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 4)
        father_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 2)

    elif wife and mother:
        wife_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 4, wife_count)
        mother_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 3)

    elif wife and father:
        wife_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 4, wife_count)
        father_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 6)

    elif mother and father:
        mother_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 3)
        father_amount, amount = calculate_share_and_deduct_from_total(amount, 2 / 3)

    elif mother:
        mother_amount, amount = calculate_share_and_deduct_from_total(amount, 1)

    elif father:
        father_amount, amount = calculate_share_and_deduct_from_total(amount, 1)

    elif wife:
        wife_amount, amount = calculate_share_and_deduct_from_total(amount, 1 / 4, wife_count)

    else:
        print("If there is nothing for you to calculate the inheritance, what are you doing here...?")

    output.diplay_shares_of_spouse_and_parents(mother_amount, father_amount, wife_amount, father, wife, mother, amount)
    return amount



def is_father_alive(father): return father == "y"
def is_mother_alive(mother): return mother == "y"
def is_wife_alive(wifes): return wifes > 0


def shares_calculation(amount, son, daughter, mother, father, wives):
    if amount > 0:
        if son > 0 and daughter >= 0 or son >= 0 and daughter > 0:
            amount = calculate_shares_for_spouse_with_sons_or_daughters(amount, mother, father, wives)
            total_share = son * 2 + daughter  # Calculate the total share
            amount_per_share = amount / total_share  # Amount per share
            output.application_output(son, daughter, amount_per_share)  # Function to display the result
        else:
            calculate_shares_for_spouse_without_sons_or_daughters(amount, mother, father, wives)
            exit()
    elif amount == 0:
        print("There is no amount to be divided between sons or daughters.")
    else:
        print("The amount must be greater than or equal to zero.")
        exit()

def main():
    try:
        # Get the inherited amount and details about family members
        inheritance_amount = float(input("Enter the total inheritance amount that a man left after deceased...: "))
        sons = int(input("How many sons does he have..? "))
        daughters = int(input("How many daughters does he have..? "))
        spouse_alive = input("Is his wife alive? (y for yes, n for no): ").lower()

        wife = 0
        if spouse_alive == "y":
            wife = int(input("How many wives does he have..? "))

        mother_alive = input("Is his mother alive? (y for yes, n for no): ").lower()
        father_alive = input("Is his father alive? (y for yes, n for no): ").lower()

        mother_alive = bool(is_mother_alive(mother_alive))
        father_alive = bool(is_father_alive(father_alive))

        # Call the calculate function to Calculate shares
        shares_calculation(inheritance_amount, sons, daughters, mother_alive, father_alive, wife)

        # Ensure the input variables are valid integers or floats
        sons = int(sons)
        daughters = int(daughters)
        inheritance_amount = float(inheritance_amount)
        wife = int(wife)

    except ValueError:
        # Handle invalid input values
        print("Enter valid data..!")
        exit()  # Exit the application

if __name__ == "__main__":
    main()