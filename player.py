import json


class Player:
    def __init__(self, name, score=100):
        self.name = name
        self.score = score

    def create_player(self):
        player_dict = {self.name: self.score}
        return player_dict

    def append_to_file(self, filename):
        player_data = self.create_player()
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        data.update(player_data)

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
