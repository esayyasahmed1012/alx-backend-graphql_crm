import graphene
from graphene_django import DjangoObjectType
from .models import Customer, Product, Order
from django.db import transaction
import re

# GraphQL types
class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class OrderType(DjangoObjectType):
    class Meta:
        model = Order

# Create a single customer
class CreateCustomer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String()

    customer = graphene.Field(CustomerType)
    message = graphene.String()

    def mutate(self, info, name, email, phone=None):
        # Validate email uniqueness
        if Customer.objects.filter(email=email).exists():
            return CreateCustomer(customer=None, message="Email already exists")
        
        # Validate phone
        if phone:
            pattern = r'^(\+\d{10,15}|\d{3}-\d{3}-\d{4})$'
            if not re.match(pattern, phone):
                return CreateCustomer(customer=None, message="Invalid phone format")
        
        customer = Customer(name=name, email=email, phone=phone)
        customer.save()
        return CreateCustomer(customer=customer, message="Customer created successfully")
