# ALX Backend GraphQL CRM

A Customer Relationship Management (CRM) backend powered by GraphQL.  
This project is part of the **ALX Backend ProDev track**, focusing on building modern, efficient APIs that go beyond REST.

---

## 📝 Project Overview

This repository demonstrates how to design and implement a **GraphQL backend service** for a CRM system.  
Instead of multiple REST endpoints, GraphQL provides a **single entry point** for flexible and efficient data access.

With this project, we:

- Build a **GraphQL schema** to handle Customers, Products, and Orders.
- Implement **queries and mutations** for seamless interaction.
- Use **Django** as the backend framework with **SQLite** as the database.
- Explore how **GraphQL improves efficiency and developer experience** in API design.

---

## 🛠 Tech Stack

- **Python 3**  
- **Django**  
- **Graphene-Django** (GraphQL integration for Django)  
- **SQLite3** (default database)  

---

## ✨ Key Features

- **GraphQL Queries** – Retrieve customer and order data flexibly.  
- **GraphQL Mutations** – Add, update, or delete customers and products.  
- **Single API Endpoint** – No more juggling multiple REST endpoints.  
- **Scalable Structure** – Easily extendable with more models and features.  

---

## 🔍 Example GraphQL Usage

**Query all customers with their orders:**

```graphql
{
  allCustomers {
    id
    name
    email
    orders {
      id
      product
      amount
    }
  }
}

---

**Add a new customer:**

```graphql
mutation {
  createCustomer(name: "John Doe", email: "john@example.com") {
    customer {
      id
      name
      email
    }
  }
}

---
## 💡 Why GraphQL?

Unlike REST, GraphQL allows the client to request exactly what it needs, reducing over-fetching and under-fetching issues.
This makes it ideal for CRM systems, where data relationships are rich and queries require flexibility.

---
## 📌 About

This project was built as part of the ALX Backend ProDev track.
It demonstrates modern API design principles while reinforcing backend development skills with Django and GraphQL.
