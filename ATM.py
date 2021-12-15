class ATM():
    def __init__(self, card_no, pin):
        self.card_no = card_no
        self.pin = pin
        print("Welcome")

    def withdraw_cash(self, amount):
        print(amount, "withdrawn")

    def add_amount_to_account(self, amount):
        print(amount, "added to your account")

    def check_balance(self, amount):
        print("You have", amount)

test = ATM("1234-5678-9012-3456", "0000")
test.withdraw_cash(500)
test.add_amount_to_account(1000)
test.check_balance(15000)