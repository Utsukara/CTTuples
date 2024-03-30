
# Refine your skills in tuple unpacking by managing customer orders.

# Problem Statement:
# You are given a list of tuples, each representing a customer's order. 
# Each tuple contains the customer's name, the product ordered, and the quantity. 
# Your task is to unpack each tuple and print the order details in a user-friendly format.

# Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

# Write a function to iterate over the list of orders.
# Unpack each tuple in the list and format the details for display.

def print_order(order_list):
    if not order_list:
        print("No orders.")
        return
    for order in order_list:
        print(f"""
Name: {order[0]}
Item: {order[1]}
Quantity: {order[2]}""")
    return

print_order(orders)