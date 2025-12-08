import sys
sys.path.insert(0, '.')

print("=== Checking Coffee Shop Implementation ===")

# Test 1: Can we import?
try:
    from customer import Customer
    from coffee import Coffee
    from order import Order
    print("✓ Imports successful")
except ImportError as e:
    print(f"✗ Import failed: {e}")
    sys.exit(1)

# Test 2: Create objects
try:
    c = Customer("Alice")
    print(f"✓ Customer created: {c.name}")
except Exception as e:
    print(f"✗ Customer creation failed: {e}")

# Test 3: Check properties
try:
    # Check if properties exist
    props_to_check = ['orders', 'coffees', 'num_orders', 'average_price']
    for prop in props_to_check:
        if hasattr(c, prop):
            print(f"✓ Customer has {prop} property")
        else:
            print(f"✗ Customer missing {prop} property")
except Exception as e:
    print(f"✗ Property check failed: {e}")

# Test 4: Check methods
try:
    if hasattr(c, 'create_order'):
        print("✓ Customer has create_order method")
    else:
        print("✗ Customer missing create_order method")
    
    if hasattr(Customer, 'most_aficionado'):
        print("✓ Customer has most_aficionado class method")
    else:
        print("✗ Customer missing most_aficionado class method")
except Exception as e:
    print(f"✗ Method check failed: {e}")

# Test 5: Create coffee
try:
    coffee = Coffee("Espresso")
    print(f"✓ Coffee created: {coffee.name}")
except Exception as e:
    print(f"✗ Coffee creation failed: {e}")

# Test 6: Create order
try:
    order = Order(c, coffee, 5.0)
    print(f"✓ Order created: ${order.price}")
except Exception as e:
    print(f"✗ Order creation failed: {e}")

print("\n=== Check Complete ===")