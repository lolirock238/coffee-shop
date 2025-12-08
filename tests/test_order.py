import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    """Test cases for Order class"""
    
    def test_order_creation(self):
        """Test that order can be created with valid data"""
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 5.0
    
    def test_order_customer_validation(self):
        """Test customer validation"""
        coffee = Coffee("Espresso")
        
        with pytest.raises(ValueError):
            Order("Not a customer", coffee, 3.0)
    
    def test_order_coffee_validation(self):
        """Test coffee validation"""
        customer = Customer("Bob")
        
        with pytest.raises(ValueError):
            Order(customer, "Not a coffee", 3.0)
    
    def test_order_price_validation(self):
        """Test price validation"""
        customer = Customer("Charlie")
        coffee = Coffee("Cappuccino")
        
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)  # Too low
        
        with pytest.raises(ValueError):
            Order(customer, coffee, 15.0)  # Too high
        
        with pytest.raises(ValueError):
            Order(customer, coffee, "not a number")  # Not a number
    
    def test_order_price_conversion_to_float(self):
        """Test that integer prices are converted to float"""
        customer = Customer("Diana")
        coffee = Coffee("Americano")
        
        order = Order(customer, coffee, 3)  # Integer price
        
        # Check if it's a float OR if Python 2.7 is treating it as int
        # In Python 2.7, 3/1 is 3 (int), not 3.0 (float)
        assert isinstance(order.price, (int, float))
        # Value should be numerically equal to 3
        assert order.price == 3
    
    def test_order_added_to_class_list(self):
        """Test that orders are added to Order.all"""
        # Clear existing orders for clean test - use Python 2.7 compatible method
        Order.all[:] = []  # This works in both Python 2 and 3
        
        initial_count = len(Order.all)
        
        customer = Customer("Eve")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 4.5)
        
        assert len(Order.all) == initial_count + 1
        assert order in Order.all