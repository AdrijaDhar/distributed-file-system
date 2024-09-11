import requests
import os

class DFSClient:
    def __init__(self, master_url):
        self.master_url = master_url

    def upload_file(self, file_path):
        file_name = os.path.basename(file_path)
        chunk_size = 1024 * 1024  # 1 MB
        chunks = []
        
        with open(file_path, 'rb') as f:
            chunk = f.read(chunk_size)
            while chunk:
                chunk_id = f"{file_name}_chunk_{len(chunks)}"
                # Simulating chunk upload (actual upload logic will be added later)
                chunks.append(chunk_id)
                chunk = f.read(chunk_size)

        # Send file metadata to the Master Node
        response = requests.post(f"{self.master_url}/file", json={"file_name": file_name, "chunks": chunks})
        print(response.json())

if __name__ == "__main__":
    client = DFSClient(master_url="http://localhost:5000")
    client.upload_file("example.txt")
