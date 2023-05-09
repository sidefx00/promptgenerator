import re
import argparse
import configparser
import openai
import os

def get_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["openai"]["api_key"]

def save_list(filename, items):
    existing_items = set()
    
    # Read existing items if the file exists
    if os.path.exists(filename):
        with open(filename, "r") as f:
            existing_items = set(line.strip() for line in f.readlines())

    with open(filename, "a") as f:
        for item in items:
            if item and item not in existing_items:
                item = item.replace("-", "")
                f.write(f"{item}\n")

def get_list(prompt, existing_items):
    openai.api_key = get_api_key()
    
    items = []

    while len(items) < 25:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"List at least 25 different types of {prompt} that are not in the following list:\n{', '.join(existing_items)}\n",
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7,
        )
        generated_items = response.choices[0].text.strip().replace(",", "\n").split("\n")
        generated_items = [re.sub(r"^\d+\.", "", item).strip() for item in generated_items]

        # Filter out existing items
        generated_items = [item for item in generated_items if item and item not in existing_items]

        # Update the existing items and the final list of items
        existing_items.update(generated_items)
        items.extend(generated_items)

    return items
def main():
    parser = argparse.ArgumentParser(description="Generate a list of items using OpenAI API")
    parser.add_argument("content", type=str, help="Content type for the list")
    args = parser.parse_args()

    list_filename = f"lists/{args.content}.txt"

    existing_items = set()
    if os.path.exists(list_filename):
        with open(list_filename, "r") as f:
            existing_items = set(line.strip() for line in f.readlines())

    items = get_list(args.content, existing_items)
    save_list(list_filename, items)

if __name__ == "__main__":
    main()

