# order_tracker.py
import datetime

class Order:
    def __init__(self, order_id, customer_name, items, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount
        self.order_date = datetime.datetime.now()

    def get_order_summary(self):
        return f"Order ID: {self.order_id}\nCustomer: {self.customer_name}\nItems: {self.items}\nTotal: ${self.total_amount}\nDate: {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}"

class OrderTracker:
    def __init__(self):
        self.orders = {}

    def add_order(self, order_id, customer_name, items, total_amount):
        if order_id in self.orders:
            raise ValueError("Order ID already exists.")
        order = Order(order_id, customer_name, items, total_amount)
        self.orders[order_id] = order
        print(f"Order {order_id} added successfully.")

    def get_order(self, order_id):
        if order_id not in self.orders:
            raise ValueError("Order not found.")
        return self.orders[order_id].get_order_summary()

    def delete_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            print(f"Order {order_id} deleted successfully.")
        else:
            raise ValueError("Order not found.")

    def list_orders(self):
        return [order.get_order_summary() for order in self.orders.values()]

# Example usage:
if __name__ == "__main__":
    ot = OrderTracker()
    ot.add_order("1001", "John Doe", ["Widget A", "Widget B"], 150.75)
    ot.add_order("1002", "Jane Smith", ["Widget C"], 75.25)

    print("\nList of Orders:")
    for order in ot.list_orders():
        print(order)

    print("\nRetrieve a Specific Order:")
    print(ot.get_order("1001"))

    ot.delete_order("1002")
    print("\nOrder 1002 deleted. Remaining orders:")
    for order in ot.list_orders():
        print(order)
