class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        self._customer = None  # Initialize to None first
        self._coffee = None    # Initialize to None first
        self._price = None     # Initialize to None first
        
        # Use setters for validation
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        Order.all.append(self)
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise ValueError("Customer must be a Customer instance")
        self._customer = value
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        self._coffee = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        # Validate type
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a number")
        
        # Convert to float for consistency
        float_value = float(value)
        
        # Validate range
        if not 1.0 <= float_value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        
        self._price = float_value