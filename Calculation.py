import output as op
import spouseOrParentShares as sps

def calculate(amount,sons,daughters,mother,father,wife):
    if amount > 0:
        if  sons > 0 and daughters >= 0 or sons >= 0 and daughters > 0:
            amount=sps.SpouseWithSonsOrDaughters(amount,mother,father,wife)
            totalShare = sons * 2 + daughters  # Calculate the total share
            amount_per_share = amount / totalShare  # amount per share
            op.show(sons, daughters, amount_per_share)     #function...
        else:
            sps.SpouseWithoutSonsOrDaughters(amount,mother,father,wife)
            exit()
    elif amount == 0:
        print("There is not amount to be divided between sons or daughters..")
    else:
        print("The Amount must be grater than or equal to zero")
        exit(0)