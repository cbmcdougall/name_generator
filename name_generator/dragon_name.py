def get_dragon_name(name, birth_month):
    name_first_half, name_second_half = name[:2], name[1:]
    month_first_half, month_second_half = birth_month[:len(birth_month)//2], birth_month[len(birth_month)//2:]
    dragon_name = name_first_half + month_second_half + " " + name_second_half + month_first_half
    return dragon_name.upper()
