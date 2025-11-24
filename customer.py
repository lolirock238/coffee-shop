class Customer:
    all_orders = []

    def __init__(self, name, ch):

        #  name validation 
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        self._name = name

        #  ch validation 
        if not isinstance(ch, int):
            raise ValueError("ch must be an integer.")
        
        if ch < 1 or ch > 15:
            raise ValueError("ch must be between 1 and 15.")

        self._ch = ch

        self._orders =[]
    @property
    def name(self):
        return self._name
    @property
    def order_coffee(self,coffee,price):
        return Order(self,coffee,price)
    @property
    def orders(self):
        return self._orders
    @property
    def coffees(self):
        return list({order.coffee for order in self._orders})
    @property
    def num_orders(self):
        return len(self._orders)
    @property
    def average_price(self):
        pass
