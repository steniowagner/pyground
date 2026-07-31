import json

import pandas as pd
from file_handlers.file_handler import FileHandler


class JSONFileHandler(FileHandler):
    def read(self):
        return pd.read_json(self.file_path)

    def write(self, json_object):
        with open(self.file_path, "w") as f:
            f.write(json.dumps(json_object))
