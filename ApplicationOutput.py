import AreFatherMotherWifeAlive as cp

def show(sons, daughters, amount_per_share):
    if sons and daughters:
        son_amount = amount_per_share * 2  # Each son's amount
        daughter_amount = amount_per_share  # Each daughter's amount
        print(f"Each son will get the amount of inheritance: {son_amount} (sons get double what daughters receive).")
        print(f"Each daughter will get the amount: {daughter_amount}")

    elif daughters:
        daughter_amount = amount_per_share  # Each daughter's amount
        print(f"Each daughter will get the amount: {daughter_amount}")

    elif sons:
        son_amount = amount_per_share * 2  # Each son's amount
        print(f"Each son will get the amount of inheritance: {son_amount} (sons get double what daughters receive).")

    else:
        print("This amount can be divided among the poor and those experiencing poverty.")

def part_of_spouse_and_parents(mother_amount, father_amount, wife_amount, father, wife, mother, amount=0):
    if cp.is_mother_alive(mother):
        print(f"Mother will get the amount: {mother_amount} Rs.")
    if cp.is_father_alive(father):
        print(f"Father will get the amount: {father_amount} Rs.")
    if cp.is_wife_alive(wife):
        print(f"Each wife will get the amount: {wife_amount} Rs.")
    if amount != 0:
        print(f"Remaining amount of inheritance: {amount} Rs.")
