class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("coffee name must be a string")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @property
    def orders(self):
        return self._orders

    @property
    def customers(self):
        return list({order.customer for order in self._orders})
