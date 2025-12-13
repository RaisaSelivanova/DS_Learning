class Item:
    def __init__(self, valid, price):
        self.valid = valid
        self.price = price

def calculate_total(items):
    total = 0
    # Точка останова перед циклом
    for item in items:  # ← breakpoint здесь
        if item.valid:  # ← или здесь для проверки условия
            total += item.price
    return total
items = [
    Item(True, 100),
    Item(False, 200),
    Item(True, 150)
]
calculate_total(items)