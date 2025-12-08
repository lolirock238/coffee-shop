import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    """Test cases for Coffee class"""
    
    def test_coffee_creation(self):
        """Test that coffee can be created with valid name"""
        coffee = Coffee("Espresso")
        assert coffee.name == "Espresso"
    
    def test_coffee_name_validation(self):
        """Test name validation"""
        with pytest.raises(ValueError):
            Coffee("AB")  # Too short
        
        with pytest.raises(ValueError):
            Coffee(123)  # Not a string
    
    def test_coffee_name_immutability(self):
        """Test that coffee name cannot be changed after creation"""
        coffee = Coffee("Latte")
        
        with pytest.raises(AttributeError):
            coffee.name = "New Name"
    
    def test_coffee_orders_property(self):
        """Test orders property returns correct orders"""
        coffee = Coffee("Cappuccino")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        
        order1 = Order(customer1, coffee, 4.0)
        order2 = Order(customer2, coffee, 4.5)
        
        assert len(coffee.orders) == 2
        assert order1 in coffee.orders
        assert order2 in coffee.orders
    
    def test_coffee_customers_property(self):
        """Test customers property returns unique customers"""
        coffee = Coffee("Americano")
        customer = Customer("Charlie")
        
        Order(customer, coffee, 3.0)
        Order(customer, coffee, 3.5)  # Same customer, different order
        
        assert len(coffee.customers) == 1
        assert customer in coffee.customers
    
    def test_num_orders_property(self):
        """Test num_orders property"""
        coffee = Coffee("Mocha")
        customer = Customer("Diana")
        
        assert coffee.num_orders == 0
        
        Order(customer, coffee, 4.5)
        assert coffee.num_orders == 1
        
        Order(customer, coffee, 5.0)
        assert coffee.num_orders == 2
    
    def test_average_price_property(self):
        """Test average_price property"""
        coffee = Coffee("Flat White")
        customer = Customer("Edward")
        
        assert coffee.average_price == 0  # No orders yet
        
        Order(customer, coffee, 3.0)
        Order(customer, coffee, 5.0)
        
        assert coffee.average_price == 4.0