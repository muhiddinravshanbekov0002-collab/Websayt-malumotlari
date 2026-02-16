class OrderHandler:
    def __init__(self):
        self.orders = {}
        self.current_order_id = 0

    def create_order(self):
        self.current_order_id += 1
        self.orders[self.current_order_id] = {'items': [], 'status': 'created', 'total': 0}
        return self.current_order_id

    def add_item(self, order_id, item_name, item_price):
        if order_id in self.orders:
            self.orders[order_id]['items'].append({'name': item_name, 'price': item_price})
            self.update_total(order_id)
        else:
            raise ValueError("Order ID not found.")

    def update_total(self, order_id):
        total = sum(item['price'] for item in self.orders[order_id]['items'])
        self.orders[order_id]['total'] = total

    def manage_order_status(self, order_id, status):
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
        else:
            raise ValueError("Order ID not found.")

    def calculate_total(self, order_id):
        if order_id in self.orders:
            return self.orders[order_id]['total']
        else:
            raise ValueError("Order ID not found.")