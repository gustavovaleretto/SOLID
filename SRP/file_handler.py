import json


class FileHandler:
    def __init__(self, filename: str):
        self.filename = filename

    def load_data(self) -> dict:
        with open(self.filename, "r") as f:
            data = json.load(f)
        return data

    def save_data(self, data: dict):
        with open(self.filename, "w") as f:
            json.dump(data, f)
