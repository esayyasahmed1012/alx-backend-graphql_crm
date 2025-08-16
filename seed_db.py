from crm.models import Customer, Product

customers = [
    {"name": "Alice", "email": "alice@example.com", "phone": "+1234567890"},
    {"name": "Bob", "email": "bob@example.com"},
]

products = [
    {"name": "Laptop", "price": 999.99, "stock": 10},
    {"name": "Mouse", "price": 25.5, "stock": 100},
]

for cust in customers:
    Customer.objects.get_or_create(**cust)

for prod in products:
    Product.objects.get_or_create(**prod)
