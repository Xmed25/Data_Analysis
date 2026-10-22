
import csv

transactions = [
    {"product": "Laptop", "region": "North", "quantity": 2, "price": 15000, "discount": 0.10, "date": "2026-01-03", "salesperson": "Ahmed"},
    {"product": "Mouse", "region": "South", "quantity": 5, "price": 300, "discount": 0.05, "date": "2026-01-04", "salesperson": "Omar"},
    {"product": "Laptop", "region": "South", "quantity": 1, "price": 15000, "discount": 0.00, "date": "2026-01-05", "salesperson": "Mona"},
    {"product": "Keyboard", "region": "East", "quantity": 3, "price": 800, "discount": 0.10, "date": "2026-01-06", "salesperson": "Sara"},
    {"product": "Monitor", "region": "West", "quantity": 2, "price": 4500, "discount": 0.05, "date": "2026-01-07", "salesperson": "Ali"},
    {"product": "Headphones", "region": "North", "quantity": 4, "price": 1200, "discount": 0.15, "date": "2026-01-08", "salesperson": "Ahmed"},
    {"product": "Mouse", "region": "East", "quantity": 10, "price": 300, "discount": 0.10, "date": "2026-01-09", "salesperson": "Mona"},
    {"product": "Printer", "region": "South", "quantity": 1, "price": 6000, "discount": 0.05, "date": "2026-01-10", "salesperson": "Omar"},
    {"product": "Keyboard", "region": "West", "quantity": 6, "price": 800, "discount": 0.00, "date": "2026-01-11", "salesperson": "Sara"},
    {"product": "Laptop", "region": "East", "quantity": 3, "price": 15000, "discount": 0.08, "date": "2026-01-12", "salesperson": "Ali"},

    {"product": "Monitor", "region": "North", "quantity": 5, "price": 4500, "discount": 0.10, "date": "2026-01-13", "salesperson": "Mona"},
    {"product": "Mouse", "region": "West", "quantity": 8, "price": 300, "discount": 0.05, "date": "2026-01-14", "salesperson": "Ahmed"},
    {"product": "Headphones", "region": "South", "quantity": 2, "price": 1200, "discount": 0.00, "date": "2026-01-15", "salesperson": "Omar"},
    {"product": "Printer", "region": "East", "quantity": 2, "price": 6000, "discount": 0.12, "date": "2026-01-16", "salesperson": "Sara"},
    {"product": "Laptop", "region": "West", "quantity": 1, "price": 15000, "discount": 0.05, "date": "2026-01-17", "salesperson": "Ali"},
    {"product": "Keyboard", "region": "North", "quantity": 4, "price": 800, "discount": 0.05, "date": "2026-01-18", "salesperson": "Ahmed"},
    {"product": "Monitor", "region": "South", "quantity": 3, "price": 4500, "discount": 0.00, "date": "2026-01-19", "salesperson": "Omar"},
    {"product": "Mouse", "region": "North", "quantity": 12, "price": 300, "discount": 0.15, "date": "2026-01-20", "salesperson": "Sara"},
    {"product": "Headphones", "region": "East", "quantity": 5, "price": 1200, "discount": 0.10, "date": "2026-01-21", "salesperson": "Mona"},
    {"product": "Printer", "region": "West", "quantity": 1, "price": 6000, "discount": 0.00, "date": "2026-01-22", "salesperson": "Ali"},

    {"product": "Laptop", "region": "North", "quantity": 4, "price": 15000, "discount": 0.12, "date": "2026-02-01", "salesperson": "Sara"},
    {"product": "Mouse", "region": "South", "quantity": 7, "price": 300, "discount": 0.00, "date": "2026-02-02", "salesperson": "Ahmed"},
    {"product": "Keyboard", "region": "East", "quantity": 5, "price": 800, "discount": 0.05, "date": "2026-02-03", "salesperson": "Omar"},
    {"product": "Monitor", "region": "West", "quantity": 4, "price": 4500, "discount": 0.08, "date": "2026-02-04", "salesperson": "Mona"},
    {"product": "Headphones", "region": "North", "quantity": 6, "price": 1200, "discount": 0.05, "date": "2026-02-05", "salesperson": "Ali"},
    {"product": "Printer", "region": "South", "quantity": 3, "price": 6000, "discount": 0.10, "date": "2026-02-06", "salesperson": "Sara"},
    {"product": "Laptop", "region": "East", "quantity": 2, "price": 15000, "discount": 0.00, "date": "2026-02-07", "salesperson": "Ahmed"},
    {"product": "Mouse", "region": "West", "quantity": 15, "price": 300, "discount": 0.10, "date": "2026-02-08", "salesperson": "Omar"},
    {"product": "Keyboard", "region": "South", "quantity": 8, "price": 800, "discount": 0.12, "date": "2026-02-09", "salesperson": "Mona"},
    {"product": "Monitor", "region": "East", "quantity": 2, "price": 4500, "discount": 0.00, "date": "2026-02-10", "salesperson": "Ali"},

    {"product": "Laptop", "region": "West", "quantity": 3, "price": 15000, "discount": 0.07, "date": "2026-02-11", "salesperson": "Omar"},
    {"product": "Headphones", "region": "South", "quantity": 7, "price": 1200, "discount": 0.15, "date": "2026-02-12", "salesperson": "Ahmed"},
    {"product": "Printer", "region": "North", "quantity": 2, "price": 6000, "discount": 0.05, "date": "2026-02-13", "salesperson": "Mona"},
    {"product": "Mouse", "region": "East", "quantity": 20, "price": 300, "discount": 0.08, "date": "2026-02-14", "salesperson": "Sara"},
    {"product": "Keyboard", "region": "West", "quantity": 3, "price": 800, "discount": 0.00, "date": "2026-02-15", "salesperson": "Ali"},
    {"product": "Monitor", "region": "North", "quantity": 6, "price": 4500, "discount": 0.10, "date": "2026-02-16", "salesperson": "Ahmed"},
    {"product": "Laptop", "region": "South", "quantity": 1, "price": 15000, "discount": 0.15, "date": "2026-02-17", "salesperson": "Mona"},
    {"product": "Headphones", "region": "East", "quantity": 3, "price": 1200, "discount": 0.00, "date": "2026-02-18", "salesperson": "Omar"},
    {"product": "Printer", "region": "West", "quantity": 4, "price": 6000, "discount": 0.08, "date": "2026-02-19", "salesperson": "Sara"},
    {"product": "Keyboard", "region": "North", "quantity": 7, "price": 800, "discount": 0.05, "date": "2026-02-20", "salesperson": "Ali"},

    {"product": "Laptop", "region": "North", "quantity": 2, "price": 15000, "discount": 0.05, "date": "2026-03-01", "salesperson": "Ahmed"},
    {"product": "Monitor", "region": "South", "quantity": 5, "price": 4500, "discount": 0.12, "date": "2026-03-02", "salesperson": "Sara"},
    {"product": "Mouse", "region": "East", "quantity": 9, "price": 300, "discount": 0.00, "date": "2026-03-03", "salesperson": "Ali"},
    {"product": "Printer", "region": "West", "quantity": 2, "price": 6000, "discount": 0.10, "date": "2026-03-04", "salesperson": "Omar"},
    {"product": "Headphones", "region": "North", "quantity": 8, "price": 1200, "discount": 0.08, "date": "2026-03-05", "salesperson": "Mona"},
    {"product": "Keyboard", "region": "South", "quantity": 6, "price": 800, "discount": 0.05, "date": "2026-03-06", "salesperson": "Ahmed"},
    {"product": "Laptop", "region": "East", "quantity": 2, "price": 15000, "discount": 0.10, "date": "2026-03-07", "salesperson": "Sara"},
    {"product": "Monitor", "region": "West", "quantity": 3, "price": 4500, "discount": 0.00, "date": "2026-03-08", "salesperson": "Ali"},
    {"product": "Mouse", "region": "South", "quantity": 14, "price": 300, "discount": 0.05, "date": "2026-03-09", "salesperson": "Omar"},
    {"product": "Printer", "region": "East", "quantity": 1, "price": 6000, "discount": 0.15, "date": "2026-03-10", "salesperson": "Mona"},

    {"product": "Laptop", "region": "West", "quantity": 5, "price": 15000, "discount": 0.10, "date": "2026-03-11", "salesperson": "Ahmed"},
    {"product": "Keyboard", "region": "North", "quantity": 9, "price": 800, "discount": 0.00, "date": "2026-03-12", "salesperson": "Ali"},
    {"product": "Headphones", "region": "South", "quantity": 4, "price": 1200, "discount": 0.12, "date": "2026-03-13", "salesperson": "Sara"},
    {"product": "Monitor", "region": "East", "quantity": 2, "price": 4500, "discount": 0.05, "date": "2026-03-14", "salesperson": "Omar"},
    {"product": "Mouse", "region": "West", "quantity": 11, "price": 300, "discount": 0.10, "date": "2026-03-15", "salesperson": "Mona"},
    {"product": "Printer", "region": "North", "quantity": 3, "price": 6000, "discount": 0.00, "date": "2026-03-16", "salesperson": "Ahmed"},
    {"product": "Laptop", "region": "South", "quantity": 2, "price": 15000, "discount": 0.05, "date": "2026-03-17", "salesperson": "Ali"},
    {"product": "Keyboard", "region": "East", "quantity": 4, "price": 800, "discount": 0.08, "date": "2026-03-18", "salesperson": "Sara"},
    {"product": "Headphones", "region": "West", "quantity": 6, "price": 1200, "discount": 0.05, "date": "2026-03-19", "salesperson": "Omar"},
    {"product": "Monitor", "region": "North", "quantity": 4, "price": 4500, "discount": 0.10, "date": "2026-03-20", "salesperson": "Mona"}
]



with open("transactions.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=transactions[0].keys())

    writer.writeheader()
    writer.writerows(transactions)

