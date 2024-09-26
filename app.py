from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

# Initialize Flask app
app = Flask(__name__)

# Database configuration - set DATABASE_URL environment variable in production
databaseURL = "postgres://uf79v0sshn2ss3:p50ffa170df1943fc61c243f940953175ac0aa5fe408af1cfa336739e4ec022f4@cf980tnnkgv1bp.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dceghr8mkifp1h"
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(databaseURL) or 'postgresql://localhost/your_local_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model (e.g., a simple `Item` model)
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Columm(db.Integer)

    def __repr__(self):
        return f"<Item {self.name}>"

# Create the database
with app.app_context():
    db.create_all()




# CRUD routes
# Create Item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], quantity=data.get('quantity', 0))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item created"}), 201

# Read All Items
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    result = [{"id": item.id, "name": item.name, "quantity": item.quantity} for item in items]
    return jsonify(result)

# Update Item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = Item.query.get_or_404(item_id)
    item.name = data['name', item.name]
    item.description = data.get('quantity', item.quantity)
    db.session.commit()
    return jsonify({"message": "Item updated"})

# Delete Item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)


