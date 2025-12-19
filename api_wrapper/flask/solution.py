from flask import Flask, request, jsonify

app = Flask(__name__)

# State management
counter_value = 0

@app.route('/counter', methods=['GET'])
def get_counter():
    """Get current counter value"""
    return jsonify({'value': counter_value}), 200

@app.route('/counter/increment', methods=['POST'])
def increment():
    """Increment counter by 1"""
    global counter_value
    counter_value += 1
    return jsonify({'value': counter_value}), 200

@app.route('/counter/decrement', methods=['POST'])
def decrement():
    """Decrement counter by 1"""
    global counter_value
    counter_value -= 1
    return jsonify({'value': counter_value}), 200

@app.route('/counter', methods=['DELETE'])
def reset():
    """Reset counter to 0"""
    global counter_value
    counter_value = 0
    return jsonify({'value': counter_value, 'message': 'Counter reset'}), 200

@app.route('/counter/set', methods=['POST'])
def set_value():
    """Set counter to specific value"""
    global counter_value
    
    data = request.get_json()
    
    # Validate request
    if not data or 'value' not in data:
        return jsonify({'error': 'Missing value field'}), 400
    
    try:
        new_value = int(data['value'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Value must be an integer'}), 400
    
    counter_value = new_value
    return jsonify({'value': counter_value}), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
