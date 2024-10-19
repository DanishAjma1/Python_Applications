import ApplicationOutput as op
import SpouseAndParentSharesCalculation as sps
def calculate(amount, sons, daughters, mother, father, wife):
    if amount > 0:
        if sons > 0 and daughters >= 0 or sons >= 0 and daughters > 0:
            amount = sps.spouse_with_sons_or_daughters(amount, mother, father, wife)
            total_share = sons * 2 + daughters  # Calculate the total share
            amount_per_share = amount / total_share  # Amount per share
            op.show(sons, daughters, amount_per_share)  # Function to display the result
        else:
            sps.spouse_without_sons_or_daughters(amount, mother, father, wife)
            exit()
    elif amount == 0:
        print("There is no amount to be divided between sons or daughters.")
    else:
        print("The amount must be greater than or equal to zero.")
        exit()
