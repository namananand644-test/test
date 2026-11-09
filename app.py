def calculate_total(price, quantity):
    return price * quantity


def apply_discount(total, discount):
    return total - (total * discount / 100)
