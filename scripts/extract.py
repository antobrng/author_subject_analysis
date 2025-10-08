import json
import requests
import os

script_dir = os.path.dirname(__file__)
raw_path = os.path.join(script_dir, "..", "data", "raw_data")

def main():


    """ with open(os.path.join(raw_path, "author_OL13895412A_works.json"), 'r') as file:
        george_orwell_file = json.load(file)
    
    data_to_save = george_orwell_file["entries"][15]["subjects"]

    with open(os.path.join(raw_path, "author_themes", "george_orwell_themes.json"), 'w') as file:
        json.dump(data_to_save, file, indent= 4) """

    with open(os.path.join(raw_path, "author_OL217475A_works.json"), 'r') as file:
        bret_beaston_ellis = json.load(file)
    
    data_to_save = bret_beaston_ellis["entries"][0]["subjects"]

    with open(os.path.join(raw_path, "author_themes", "bret_beaston_ellis_themes.json"), 'w') as file:
        json.dump(data_to_save, file, indent= 4)


    


    exit()


if __name__ == "__main__":
    main()