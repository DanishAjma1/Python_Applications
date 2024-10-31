import shares_calculator_application_main as application

def application_output(sons, daughters, amount_per_share):
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

def diplay_shares_of_spouse_and_parents(mother_amount, father_amount, wife_amount, father, wife, mother, amount=0):
    if mother:
        print(f"Mother will get the amount: {mother_amount} Rs.")
    if father:
        print(f"Father will get the amount: {father_amount} Rs.")
    if wife:
        print(f"Each wife will get the amount: {wife_amount} Rs.")
    if amount != 0:
        print(f"Remaining amount of inheritance: {amount} Rs.")
