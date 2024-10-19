import AreFatherMotherWifeAlive as cp
import ApplicationOutput as op

# Helper function to calculate and subtract amount based on a given ratio
def calculate_and_deduct(amount, ratio, count=1):
    part = ratio * amount
    amount -= part * count
    return part, amount

# Function to calculate shares when there are sons or daughters
def spouse_with_sons_or_daughters(amount, mother, father, wife):
    wife_amount = 0
    father_amount = 0
    mother_amount = 0

    # Check if wife, mother, and father are alive and calculate their respective shares
    if cp.is_wife_alive(wife) and cp.is_mother_alive(mother) and cp.is_father_alive(father):
        wife_amount, amount = calculate_and_deduct(amount, 1 / 8, wife)
        mother_amount, amount = calculate_and_deduct(amount, 1 / 6)
        father_amount, amount = calculate_and_deduct(amount, 1 / 6)

    elif cp.is_wife_alive(wife) and cp.is_mother_alive(mother):
        wife_amount, amount = calculate_and_deduct(amount, 1 / 8, wife)
        mother_amount, amount = calculate_and_deduct(amount, 1 / 6)

    elif cp.is_wife_alive(wife) and cp.is_father_alive(father):
        wife_amount, amount = calculate_and_deduct(amount, 1 / 8, wife)
        father_amount, amount = calculate_and_deduct(amount, 1 / 6)

    elif cp.is_mother_alive(mother) and cp.is_father_alive(father):
        mother_amount, amount = calculate_and_deduct(amount, 1 / 6)
        father_amount, amount = calculate_and_deduct(amount, 1 / 6)

    elif cp.is_mother_alive(mother):
        mother_amount, amount = calculate_and_deduct(amount, 1 / 6)

    elif cp.is_father_alive(father):
        father_amount, amount = calculate_and_deduct(amount, 1 / 6)

    elif cp.is_wife_alive(wife):
        wife_amount, amount = calculate_and_deduct(amount, 1 / 6, wife)

    else:
        print("If there is nothing for you to calculate the inheritance, what are you doing here...?")

    # Output the calculated shares
    op.part_of_spouse_and_parents(mother_amount, father_amount, wife_amount, father, wife, mother)
    return amount

# Function to calculate shares when there are no sons or daughters
def spouse_without_sons_or_daughters(amount, mother, father, wife):
    wife_amount = 0
    father_amount = 0
    mother_amount = 0

    # Check if wife, mother, and father are alive and calculate their respective shares
    if cp.is_wife_alive(wife) and cp.is_mother_alive(mother) and cp.is_father_alive(father):
        wife_amount, amount = calculate_and_deduct(amount, 1 / 4, wife)
        mother_amount, amount = calculate_and_deduct(amount, 1 / 4)
        father_amount, amount = calculate_and_deduct(amount, 1 / 2)

    elif cp.is_wife_alive(wife) and cp.is_mother_alive(mother):
        wife_amount, amount = calculate_and_deduct(amount, 1 / 4, wife)
        mother_amount, amount = calculate_and_deduct(amount, 1 / 3)

    elif cp.is_wife_alive(wife) and cp.is_father_alive(father):
        wife_amount, amount = calculate_and_deduct(amount, 1 / 4, wife)
        father_amount, amount = calculate_and_deduct(amount, 1 / 6)

    elif cp.is_mother_alive(mother) and cp.is_father_alive(father):
        mother_amount, amount = calculate_and_deduct(amount, 1 / 3)
        father_amount, amount = calculate_and_deduct(amount, 2 / 3)

    elif cp.is_mother_alive(mother):
        mother_amount, amount = calculate_and_deduct(amount, 1)

    elif cp.is_father_alive(father):
        father_amount, amount = calculate_and_deduct(amount, 1)

    elif cp.is_wife_alive(wife):
        wife_amount, amount = calculate_and_deduct(amount, 1 / 4, wife)

    else:
        print("If there is nothing for you to calculate the inheritance, what are you doing here...?")

    op.part_of_spouse_and_parents(mother_amount, father_amount, wife_amount, father, wife, mother, amount)
    return amount
