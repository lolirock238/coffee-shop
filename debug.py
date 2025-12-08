#!/usr/bin/env python3
"""
Debug script for testing the Coffee Shop domain model
"""

# Import at the top - this should work now
from customer import Customer
from coffee import Coffee
from order import Order

def main():
    """Test the domain model functionality"""
    print("=== Coffee Shop Domain Model Debug ===\n")
    
    # Clear any existing data
    Customer.all_customers.clear()
    Coffee.all_coffees.clear()
    Order.all.clear()
    
    # Create customers
    print("Creating customers...")
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")
    
    # Create coffees
    print("Creating coffees...")
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    
    # Create orders
    print("Creating orders...")
    order1 = alice.create_order(espresso, 3.5)
    order2 = alice.create_order(latte, 4.5)
    order3 = bob.create_order(espresso, 3.0)
    order4 = bob.create_order(cappuccino, 5.0)
    order5 = charlie.create_order(latte, 4.0)
    order6 = charlie.create_order(espresso, 3.5)
    order7 = charlie.create_order(cappuccino, 5.5)
    
    # Test customer properties
    print("\n=== Customer Properties ===")
    print(f"{alice.name}'s orders: {len(alice.orders)}")
    print(f"{alice.name}'s coffees: {[c.name for c in alice.coffees]}")
    print(f"{alice.name}'s average price: ${alice.average_price:.2f}")
    
    # Test coffee properties
    print("\n=== Coffee Properties ===")
    print(f"{espresso.name} orders: {espresso.num_orders}")
    print(f"{espresso.name} customers: {[c.name for c in espresso.customers]}")
    print(f"{espresso.name} average price: ${espresso.average_price:.2f}")
    
    # Test class methods
    print("\n=== Class Methods ===")
    top_espresso_drinker = Customer.most_aficionado(espresso)
    if top_espresso_drinker:
        print(f"Biggest espresso fan: {top_espresso_drinker.name}")
    
    # Test edge cases
    print("\n=== Edge Cases ===")
    
    # Customer with no orders
    dave = Customer("Dave")
    print(f"{dave.name}'s orders: {dave.num_orders}")
    print(f"{dave.name}'s average price: ${dave.average_price:.2f}")
    
    # Coffee with no orders
    new_coffee = Coffee("New Blend")
    print(f"{new_coffee.name}'s orders: {new_coffee.num_orders}")
    
    print("\n=== Debug Complete ===")

if __name__ == "__main__":
    main()