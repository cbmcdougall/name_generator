def get_dragon_name(name, birth_month):
    """ Takes a name and birthmonth and generates a dragon name by mixing parts of each """
    name_first_part, name_second_part = name[:2], name[1:]

    month_first_half, month_second_half = birth_month[:len(birth_month)//2], birth_month[len(birth_month)//2:]

    dragon_name = name_first_part + month_second_half + " " + name_second_part + month_first_half

    return dragon_name.upper()
