# Coffee Shop Domain Model Lab

## Learning Goals
- Build robust and dynamic Python objects with proper relationships
- Implement object-oriented programming principles in Python
- Create classes with proper encapsulation, validation, and relationships
- Work with many-to-many relationships through join classes

## Key Vocab
- **Class**: A blueprint for creating objects that bundle data and functionality together.
- **Object**: An instance of a class containing both data (attributes) and behavior (methods).
- **Object-Oriented Programming**: Programming paradigm focused on objects containing data and methods to manipulate that data.
- **Property**: A special kind of attribute with getter and setter methods for controlled access.
- **Instance Method**: A function defined inside a class that operates on an instance of that class.
- **Class Method**: A method that operates on the class itself rather than instances.
- **Many-to-Many Relationship**: When instances of one class can be associated with many instances of another class, and vice versa.

## Instructions
This is a test-driven lab. Run `pipenv install` to create your virtual environment and `pipenv shell` to enter it. Then run `pytest -x` to run your tests. Use these instructions and pytest's error messages to complete your work.

You will build a domain model for a Coffee Shop with three main entities: `Customer`, `Coffee`, and `Order`. These classes should establish proper relationships and implement the required functionality.

### Classes and Requirements

#### 1. Customer Class (`customer.py`)
- Should be initialized with a `name` (string between 1 and 15 characters)
- Should have a `name` property with validation
- Should have these instance methods/properties:
  - `create_order(coffee, price)`: Creates a new Order instance
  - `orders`: Returns list of all orders for this customer
  - `coffees`: Returns unique list of coffees this customer has ordered
  - `num_orders`: Returns number of orders made by this customer
  - `average_price`: Returns average price of all customer's orders
- Should have this class method:
  - `most_aficionado(coffee)`: Returns the customer who has spent the most on the given coffee

#### 2. Coffee Class (`coffee.py`)
- Should be initialized with a `name` (string at least 3 characters long)
- Should have a `name` property that is immutable after creation
- Should have these instance methods/properties:
  - `orders`: Returns list of all orders for this coffee
  - `customers`: Returns unique list of customers who ordered this coffee
  - `num_orders`: Returns total number of times this coffee has been ordered
  - `average_price`: Returns average price for this coffee based on its orders

#### 3. Order Class (`order.py`)
- Should be initialized with a `customer` (Customer instance), `coffee` (Coffee instance), and `price` (float between 1.0 and 10.0)
- Should have properties for `customer`, `coffee`, and `price` with validation
- Should maintain a class-level list `all` containing all Order instances

### Relationships
- **Customer ↔ Order**: One-to-Many (A customer can have many orders)
- **Coffee ↔ Order**: One-to-Many (A coffee can have many orders)
- **Customer ↔ Coffee**: Many-to-Many (through Order)

### Example Usage
```python
from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
espresso = Coffee("Espresso")
latte = Coffee("Latte")

# Create orders
order1 = alice.create_order(espresso, 3.5)
order2 = bob.create_order(latte, 4.0)

# Access properties
print(f"{alice.name} has ordered {alice.num_orders} times")
print(f"Average price for {espresso.name}: ${espresso.average_price:.2f}")

# Use class methods
top_customer = Customer.most_aficionado(espresso)