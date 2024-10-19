import CheckPart as cp

def show(sons,daughters,amount_per_share):
    if sons and daughters:
        son_amount = amount_per_share * 2  # each son's amount
        daughter_amount = amount_per_share  # each daughter amount
        print(f"Each son will get the amount of inheritance..: {son_amount} (as the son get double than daughter..)")
        print(f"Each daughter will get the amount..: {daughter_amount}")

    elif daughters:
        daughter_amount = amount_per_share  # each daughter amount
        print(f"Each daughter will get the amount..: {daughter_amount}")

    elif sons:
        son_amount = amount_per_share * 2  # each son's amount
        print(f"Each son will get the amount..: {son_amount} (as the son get double than daughter..)")

    else:
        print("This amount can be divided between poors and people who experiencing poverty..")

def partOfSpouseAndParents(mother_amount,father_amount,wife_amount,father,wife,mother,amount=0):
    if cp.isMotherAlive(mother):
        print(f"Mother will get the amount..: {mother_amount} Rs.")
    if cp.isFatherAlive(father):
        print(f"Father will get the amount..: {father_amount} Rs.")
    if cp.isWifeAlive(wife):
        print(f"Each wife will get the amount..: {wife_amount} Rs.")
    if amount !=0:
        print(f"Remaining amount of inheritance..: {amount} Rs.")

