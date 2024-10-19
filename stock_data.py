# def get_low_stock_alerts():
#     # Mock data for low stock
#     stock = [
#         {"productId": "101", "productName": "Widget A", "quantity": 3},
#         {"productId": "102", "productName": "Widget B", "quantity": 1},
#     ]
#     return [f"Low stock: {item['productName']} (ID: {item['productId']})" for item in stock if item['quantity'] < 5]

# Simulated database of stock items
stock_items = [
    {"productId": "101", "productName": "Widget A", "quantity": 3},
    {"productId": "102", "productName": "Widget B", "quantity": 1},
]

def get_low_stock_alerts():
    return [f"Low stock: {item['productName']} (ID: {item['productId']})" for item in stock_items if item['quantity'] < 5]

def add_stock_item(product_id, product_name, quantity):
    stock_items.append({
        "productId": product_id,
        "productName": product_name,
        "quantity": int(quantity)
    })
