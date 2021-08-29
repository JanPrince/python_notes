

class CreditCard(object):
    """
    A consumer credit card
    """
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.

        The initial balance is zero.

        customer:        the name of the customer (e.g., John Bowman )
         bank  :         the name of the bank (e.g., California Savings )
         acnt  :         the account identifier (e.g., 5391 0375 9387 5309 )
         limit :         credit limit (measured in dollars)

        """
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self.limit = limit
        self.balance = 0

    def get_account(self):
        return self.account

    def get_bank(self):
        return self.bank

    def get_customer(self):
        return self.customer

    def get_limit(self):
        return self.limit

    def get_balance(self):
        return self.balance

    def deposit(self, price):
        """

        :param price:  price to be loaded to the credit card
        :return: True or false
        """
        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
            return True

    def make_payments(self, amount):
        self.balance -= amount


john = CreditCard("John Wick", "California savings", 342312223322342, 10000000)

print(john.get_balance())
print(john.get_account())

john.deposit(34)

print(john.get_balance())