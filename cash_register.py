# task 1
class CashRegister:

    def __init__(self):
        self.total_items = {} # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item_n_price):
        self.total_items.update(item_n_price)

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, monetary_amount):
        self.discount += monetary_amount

    def get_total(self):
        total_before_discount = sum(self.total_items.values())
        total = total_before_discount - self.discount
        print(f"Total Amount payable: £ {total:.2f}")

    def show_items(self):
        print("---shopping receipt---")
        for item, price in self.total_items.items():
            print(f"{item:10}  £ {price:.2f}")
        print("----------------------")

    def reset_register(self):
        self.total_items = {}
        self.discount = 0


# initialise one cash register as register 1
register_1 = CashRegister()

# adding items to the basket
register_1.add_item({'flip-flops': 4.5})
register_1.add_item({'sunglasses': 12})
register_1.add_item({'towel': 8})
register_1.add_item({'ski goggles': 25})

register_1.remove_item('ski goggles')

# sunglasses are 20 % off
register_1.apply_discount(2.4)

# total amount payable at the till
register_1.get_total()

# receipt
register_1.show_items()