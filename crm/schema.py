# crm/schema.py
import graphene
import re
from graphene_django import DjangoObjectType
from .models import Customer, Product, Order

class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class OrderType(DjangoObjectType):
    class Meta:
        model = Order

class CreateCustomer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String()

    customer = graphene.Field(CustomerType)
    message = graphene.String()

    def mutate(self, info, name, email, phone=None):
        if Customer.objects.filter(email=email).exists():
            return CreateCustomer(customer=None, message="Email already exists")
        
        if phone:
            pattern = r'^(\+\d{10,15}|\d{3}-\d{3}-\d{4})$'
            if not re.match(pattern, phone):
                return CreateCustomer(customer=None, message="Invalid phone format")
        
        customer = Customer(name=name, email=email, phone=phone)
        customer.save()
        return CreateCustomer(customer=customer, message="Customer created successfully")

class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()

class Query(graphene.ObjectType):
    customers = graphene.List(CustomerType)

    def resolve_customers(self, info):
        return Customer.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
