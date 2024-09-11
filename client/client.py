import requests

# Client interface
class DFSClient:
    def __init__(self, master_url):
        self.master_url = master_url

    def upload_file(self, file_path):
        # Logic to upload file
        pass

    def download_file(self, file_name):
        # Logic to download file
        pass

    def delete_file(self, file_name):
        # Logic to delete file
        pass

if __name__ == "__main__":
    client = DFSClient(master_url="http://localhost:5000")
    # Example usage:
    # client.upload_file("example.txt")
    # client.download_file("example.txt")
