from customer import Customer
from coffee import Coffee

class Order:
    all = []

    def __init__(self, customer, coffee, price):

        # validate customer is Customer object
        if not isinstance(customer, Customer):
            raise ValueError("customer must be a Customer instance")
        self._customer = customer

        # validate coffee is Coffee object
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be a Coffee instance")
        self._coffee = coffee

        # validate price
        if not isinstance(price, (int, float)):
            raise ValueError("price must be a number")

        if not (1 <= price <= 15):
            raise ValueError("price must be between 1 and 15")
        self._price = price

        Order.all.append(self)

        # Add to customer's orders
        customer._orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
