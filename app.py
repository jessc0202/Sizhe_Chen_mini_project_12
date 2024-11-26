from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route to provide API information
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Flask Arithmetic API. Use /add or /multiply with query parameters 'a' and 'b'."
    })

# Route to add two numbers
@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please provide numeric values for 'a' and 'b'."}), 400

    result = a + b
    return jsonify({"result": result})

# Route to multiply two numbers
@app.route('/multiply', methods=['GET'])
def multiply_numbers():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please provide numeric values for 'a' and 'b'."}), 400

    result = a * b
    return jsonify({"result": result})

# Route to subtract two numbers
@app.route('/subtract', methods=['GET'])
def subtract_numbers():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please provide numeric values for 'a' and 'b'."}), 400

    result = a - b
    return jsonify({"result": result})

# Main execution
if __name__ == '__main__':
    app.run(debug=True)

