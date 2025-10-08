import os
import json
import pandas as pd

script_dir = os.path.dirname(__file__)
raw_path = os.path.join(script_dir, "..", "data", "raw_data")

dt = pd.DataFrame(pd.read_json(os.path.join(raw_path, "author_themes", "bret_beaston_ellis_themes.json")))

for i in range (0, len(dt) - 1):
    dt[0][i].str.replace(r"^", "f" , regex = True)
    i += 1


print(dt[0][1])

with open(os.path.join(raw_path, "author_themes", "bret_beaston_ellis_themes.json"), 'r') as file:
    bret_beaston_ellis = json.load(file)

print(bret_beaston_ellis[0])