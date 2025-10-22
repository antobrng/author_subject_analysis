import json
import os

script_dir = os.path.dirname(__file__)
raw_path = os.path.join(script_dir, "..", "data", "raw_data")


def extract_subject(file_name, output_file):
    subjects = []

    with open(os.path.join(raw_path, file_name), 'r', encoding='utf-8') as file:
        data = json.load(file)

    for entry in data["entries"]:
        if "subjects" in entry:
            subjects.append(entry["subjects"])

    # Optional: print for debugging
    print(f"Extracted {len(subjects)} subject lists from {file_name}")

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(subjects, file, indent=4, ensure_ascii=False)


def main():
    extract_subject("author_OL217475A_works.json", os.path.join(raw_path, "bret_theme.json"))
    extract_subject("author_OL13895412A_works.json", os.path.join(raw_path, "orwell_theme.json"))


if __name__ == "__main__":
    main()
