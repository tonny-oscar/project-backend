# from flask import Flask, jsonify
# from stock_data import get_low_stock_alerts
# from orders_data import get_new_orders

# app = Flask(__name__)

# @app.route('/api/alerts', methods=['GET'])
# def get_alerts():
#     low_stock_alerts = get_low_stock_alerts()
#     new_orders = get_new_orders()
#     return jsonify({
#         "lowStockAlerts": low_stock_alerts,
#         "newOrders": new_orders
#     })

# if __name__ == '__main__':
#     app.run(debug=True, port=3001)

from flask import Flask, jsonify, request
from flask_cors import CORS
from stock_data import get_low_stock_alerts, add_stock_item
from orders_data import get_new_orders

app = Flask(__name__)
CORS(app)
# Existing alerts route
@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    low_stock_alerts = get_low_stock_alerts()
    new_orders = get_new_orders()
    return jsonify({
        "lowStockAlerts": low_stock_alerts,
        "newOrders": new_orders
    })

# New route for adding stock
@app.route('/api/stock', methods=['POST'])
def add_stock():
    data = request.json
    product_id = data.get('productId')
    product_name = data.get('productName')
    quantity = data.get('quantity')

    # Add the stock item
    add_stock_item(product_id, product_name, quantity)

    return jsonify({"message": "Stock item added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=3001)
