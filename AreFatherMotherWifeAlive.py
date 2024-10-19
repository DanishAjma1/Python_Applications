def is_father_alive(father):
    if father == "y":
        return True
    return False  # Added to ensure False is returned if condition isn't met


def is_mother_alive(mother):
    if mother == "y":
        return True
    return False  # Added to ensure False is returned if condition isn't met


def is_wife_alive(wife):
    if wife > 0:  # Assuming this checks if the wife is alive based on number
        return True
    return False  # Added to ensure False is returned if condition isn't met
