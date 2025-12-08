class Customer:
    all_customers = []
    
    def __init__(self, name):
        self._name = None
        self.name = name
        Customer.all_customers.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value
    
    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        return order
    
    @property
    def orders(self):
        from order import Order
        return [order for order in Order.all if order.customer == self]
    
    @property
    def coffees(self):
        return list({order.coffee for order in self.orders})
    
    @property
    def num_orders(self):
        return len(self.orders)
    
    @property
    def average_price(self):
        if not self.orders:
            return 0
        return sum(order.price for order in self.orders) / len(self.orders)
    
    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise ValueError("Must provide a Coffee instance")
        
        max_spent = -1
        top_customer = None
        
        for customer in cls.all_customers:
            customer_total = 0
            for order in customer.orders:
                if order.coffee == coffee:
                    customer_total += order.price
            
            if customer_total > max_spent:
                max_spent = customer_total
                top_customer = customer
        
        return top_customer if max_spent > 0 else None