import requests

# Worker Node logic
class WorkerNode:
    def __init__(self, master_url, worker_id):
        self.master_url = master_url
        self.worker_id = worker_id
        self.storage = {}  # In-memory chunk storage

    def register_with_master(self):
        data = {"worker_id": self.worker_id}
        response = requests.post(f"{self.master_url}/register", json=data)
        print(response.json())

    def store_chunk(self, chunk_id, data):
        self.storage[chunk_id] = data
        # Logic to replicate chunk to other nodes

if __name__ == "__main__":
    worker = WorkerNode(master_url="http://localhost:5000", worker_id="worker_1")
    worker.register_with_master()
