from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    """Homepage route"""
    return 'Hello, Flask World! I am Vicky!!!'

@app.route('/greet', methods=['GET'])
def greet():
    """Greet a user by name"""
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/add', methods=['POST'])
def add_numbers():
    """Add two numbers"""
    data = request.get_json()
    if not data or 'num1' not in data or 'num2' not in data:
        return jsonify({"error": "Missing parameters"}), 400

    num1, num2 = data.get('num1'), data.get('num2')
    try:
        result = float(num1) + float(num2)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 400

@app.route('/status', methods=['GET'])
def status():
    """Health check route"""
    return jsonify({"status": "running", "version": "1.0.0"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
