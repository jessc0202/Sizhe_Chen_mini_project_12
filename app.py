from flask import Flask, request, jsonify

app = Flask(__name__)

# Default route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# New route to add two numbers
@app.route('/add', methods=['GET'])
def add_numbers():
    # Retrieve query parameters `a` and `b`
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    
    if a is None or b is None:
        return jsonify({"error": "Please provide both 'a' and 'b' as query parameters."}), 400
    
    result = a + b
    return jsonify({"result": result})

# New route to multiply two numbers
@app.route('/multiply', methods=['GET'])
def multiply_numbers():
    # Retrieve query parameters `a` and `b`
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    
    if a is None or b is None:
        return jsonify({"error": "Please provide both 'a' and 'b' as query parameters."}), 400
    
    result = a * b
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
