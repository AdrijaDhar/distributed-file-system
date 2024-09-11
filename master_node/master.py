from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory metadata storage
file_metadata = {}
worker_nodes = {}

@app.route('/register', methods=['POST'])
def register_worker():
    data = request.json
    worker_id = data.get('worker_id')
    worker_nodes[worker_id] = data.get('address')
    return jsonify({"status": f"Worker {worker_id} registered"}), 200

@app.route('/file', methods=['POST', 'DELETE', 'GET'])
def file_operations():
    if request.method == 'POST':
        file_name = request.json.get('file_name')
        file_chunks = request.json.get('chunks')
        file_metadata[file_name] = file_chunks
        return jsonify({"status": "File created"}), 200
    elif request.method == 'DELETE':
        file_name = request.json.get('file_name')
        if file_name in file_metadata:
            del file_metadata[file_name]
            return jsonify({"status": "File deleted"}), 200
        else:
            return jsonify({"error": "File not found"}), 404
    elif request.method == 'GET':
        file_name = request.args.get('file_name')
        if file_name in file_metadata:
            return jsonify({"chunks": file_metadata[file_name]}), 200
        else:
            return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(port=5000)
