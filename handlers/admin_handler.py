# admin_handler.py

class AdminPanel:
    def __init__(self):
        self.menu_items = []
        self.orders = []
        self.users = []

    def add_menu_item(self, item):
        self.menu_items.append(item)
        print(f'Added menu item: {item}\n')

    def remove_menu_item(self, item):
        if item in self.menu_items:
            self.menu_items.remove(item)
            print(f'Removed menu item: {item}\n')
        else:
            print(f'Menu item: {item} not found.\n')

    def view_orders(self):
        if not self.orders:
            print('No orders to display.\n')
            return
        for order in self.orders:
            print(order)

    def manage_users(self):
        if not self.users:
            print('No users to manage.\n')
            return
        for user in self.users:
            print(user)

    def add_order(self, order):
        self.orders.append(order)
        print(f'Added order: {order}\n')

    def add_user(self, user):
        self.users.append(user)
        print(f'Added user: {user}\n')

# Example usage of the AdminPanel class
if __name__ == '__main__':
    admin_panel = AdminPanel()
    admin_panel.add_menu_item('Pizza')
    admin_panel.add_order({'id': 1, 'item': 'Pizza', 'quantity': 2})
    admin_panel.add_user({'name': 'John Doe', 'role': 'customer'})
    admin_panel.view_orders()
    admin_panel.manage_users()