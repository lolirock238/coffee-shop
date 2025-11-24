class Order:
    all = []

    def __init__(self, customer, coffee, price):
        # validate customer
        if not isinstance(customer, str):
            raise ValueError("customer must be a string")
        self._customer = customer

        # validate coffee
        if not isinstance(coffee, str):
            raise ValueError("coffee must be a string")
        self._coffee = coffee

        # validate price
        if not isinstance(price, (int, float)):
            raise ValueError("price must be a number")

        if price < 1 or price > 15:
            raise ValueError("price must be between 1 and 15")
        self._price = price

        Order.all.append(self)
    @property
    def customer(self):
        return self._customer
    @property
    def coffee(self):
        return self._coffee
    @property
    def price(self):
        return self._price