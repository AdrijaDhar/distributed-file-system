from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory metadata storage
file_metadata = {}

# Endpoint to register a worker node
@app.route('/register', methods=['POST'])
def register_worker():
    data = request.json
    # Register the worker node logic here
    return jsonify({"status": "Worker registered"}), 200

# Endpoint to handle file operations
@app.route('/file', methods=['POST', 'DELETE', 'GET'])
def file_operations():
    if request.method == 'POST':
        # Handle file creation
        pass
    elif request.method == 'DELETE':
        # Handle file deletion
        pass
    elif request.method == 'GET':
        # Handle file retrieval
        pass
    return jsonify({"status": "Operation successful"}), 200

if __name__ == "__main__":
    app.run(port=5000)
