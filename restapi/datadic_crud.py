from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# สร้าง Dictionary สำหรับเก็บข้อมูล
items = {}
current_id = 1
@app.route('/items', methods=['POST'])
def create_item():
    global current_id
    data = request.get_json()
    item = {
        'id': current_id,
        'name': data['name'],
        'description': data.get('description', '')
    }
    items[current_id] = item
    current_id += 1
    return jsonify(item), 201

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(items.values()))

@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = items.get(id)
    if item is None:
        abort(404, description="Item not found")
    return jsonify(item)

@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json()
    item = items.get(id)
    if item is None:
        abort(404, description="Item not found")
    item['name'] = data['name']
    item['description'] = data.get('description', item['description'])
    return jsonify(item)

@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    if id not in items:
        abort(404, description="Item not found")
    del items[id]
    return jsonify({'message': 'Item deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
