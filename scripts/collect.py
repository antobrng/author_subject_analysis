import json
import requests
import os.path

script_dir = os.path.dirname(__file__)
raw_path = os.path.join(script_dir, "..", "data", "raw_data")



def main():
    author_name = r"george%20orwell"

    ##Query for the author

    query_url = "https://openlibrary.org/search/authors.json?q=" + author_name
    r = requests.get(query_url)
    author_data = r.json()
    author_key = author_data["docs"][0]["key"]

    print("Author key:", author_key)

    ## Query for the books

    books_url = "https://openlibrary.org/authors/" + author_key + "/works.json"
    r = requests.get(books_url)

    book_data = r.json()

    ## Write our the raw data 
    fname = f"author_{author_key}_works.json"
    with open(os.path.join(raw_path, fname), "w") as f:
        json.dump(book_data, f , indent = 4)


if __name__ == "__main__":
    main()