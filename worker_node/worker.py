import requests

class WorkerNode:
    def __init__(self, master_url, worker_id):
        self.master_url = master_url
        self.worker_id = worker_id
        self.storage = {}  # In-memory chunk storage

    def register_with_master(self):
        data = {"worker_id": self.worker_id, "address": "http://localhost:5001"}
        response = requests.post(f"{self.master_url}/register", json=data)
        print(response.json())

    def store_chunk(self, chunk_id, data):
        self.storage[chunk_id] = data
        return {"status": "Chunk stored"}

    def retrieve_chunk(self, chunk_id):
        if chunk_id in self.storage:
            return self.storage[chunk_id]
        else:
            return {"error": "Chunk not found"}

if __name__ == "__main__":
    worker = WorkerNode(master_url="http://localhost:5000", worker_id="worker_1")
    worker.register_with_master()
