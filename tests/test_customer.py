import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    """Test cases for Customer class"""
    
    def test_customer_creation(self):
        """Test that customer can be created with valid name"""
        customer = Customer("Alice")
        assert customer.name == "Alice"
    
    def test_customer_name_validation(self):
        """Test name validation"""
        with pytest.raises(ValueError):
            Customer("")  # Too short
        
        with pytest.raises(ValueError):
            Customer("A" * 16)  # Too long
        
        with pytest.raises(ValueError):
            Customer(123)  # Not a string
    
    def test_create_order(self):
        """Test creating an order"""
        customer = Customer("Bob")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 5.0)
        
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 5.0
    
    def test_customer_orders_property(self):
        """Test orders property returns correct orders"""
        customer = Customer("Charlie")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Cappuccino")
        
        order1 = Order(customer, coffee1, 3.0)
        order2 = Order(customer, coffee2, 4.0)
        
        assert len(customer.orders) == 2
        assert order1 in customer.orders
        assert order2 in customer.orders
    
    def test_customer_coffees_property(self):
        """Test coffees property returns unique coffees"""
        customer = Customer("David")
        coffee = Coffee("Americano")
        
        Order(customer, coffee, 3.0)
        Order(customer, coffee, 3.5)  # Same coffee, different order
        
        assert len(customer.coffees) == 1
        assert coffee in customer.coffees
    
    def test_num_orders_property(self):
        """Test num_orders property"""
        customer = Customer("Eve")
        coffee = Coffee("Mocha")
        
        assert customer.num_orders == 0
        
        Order(customer, coffee, 4.5)
        assert customer.num_orders == 1
        
        Order(customer, coffee, 5.0)
        assert customer.num_orders == 2
    
    def test_average_price_property(self):
        """Test average_price property"""
        customer = Customer("Frank")
        coffee = Coffee("Flat White")
        
        assert customer.average_price == 0  # No orders yet
        
        Order(customer, coffee, 3.0)
        Order(customer, coffee, 5.0)
        
        assert customer.average_price == 4.0
    
    def test_most_aficionado_class_method(self):
        """Test most_aficionado class method"""
        coffee = Coffee("Special Blend")
        
        customer1 = Customer("Grace")
        customer2 = Customer("Henry")
        
        Order(customer1, coffee, 9.0)
        Order(customer1, coffee, 8.0)  # Total: 17.0
        
        Order(customer2, coffee, 10.0)  # Total: 10.0
        
        top_customer = Customer.most_aficionado(coffee)
        assert top_customer == customer1
        
        # Test with coffee that has no orders
        new_coffee = Coffee("New Blend")
        assert Customer.most_aficionado(new_coffee) is None