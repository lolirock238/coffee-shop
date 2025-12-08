class Coffee:
    all_coffees = []
    
    def __init__(self, name):
        self._name = None  # Initialize to None first
        self.name = name   # Use setter for validation
        Coffee.all_coffees.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # Validate type
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        
        # Validate length
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        
        # Validate immutability
        if self._name is not None:
            raise AttributeError("Cannot change coffee name after creation")
        
        self._name = value
    
    @property
    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee == self]
    
    @property
    def customers(self):
        return list({order.customer for order in self.orders})
    
    @property
    def num_orders(self):
        return len(self.orders)
    
    @property
    def average_price(self):
        if not self.orders:
            return 0
        return sum(order.price for order in self.orders) / len(self.orders)