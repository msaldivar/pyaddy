"""
Class to handle writing and reading the addy api key

"""
import os


class AddyKey:
    def __init__(self) -> None:
        filename = "addy_key.cfg"
        dir_path = os.path.dirname(os.path.abspath(__file__))

        self.full_path = os.path.join(dir_path, filename)

    def write_to_config(self, key) -> None:
        with open(self.full_path, "w") as f:
            f.write(key)

    def load_key(self) -> None:
        key = None
        try:
            with open(self.full_path, "r") as f:
                key = f.readline()
        except OSError:
            if not self.api_key:
                raise ("No api key present: Run load-key")

        return key
