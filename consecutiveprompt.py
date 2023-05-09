import sys
import os
import random
import argparse
import re

def main():
    parser = argparse.ArgumentParser(description='Generate consecutive prompts.')
    parser.add_argument('input_text', type=str, nargs='?', help='Your text with [placeholder]')
    args = parser.parse_args()

    if args.input_text is None:
        print("Usage: consecutiveprompt.py \"Your text with [placeholder]\"")
        return

    input_text = args.input_text

    placeholders = list(set(re.findall(r'\[([^\]]+)\]', input_text)))
    available_lists = {}

    for placeholder in placeholders:
        list_file = f'lists/{placeholder}.txt'
        if not os.path.isfile(list_file):
            print(f"The list '{placeholder}' does not exist.")
            available_lists_str = ', '.join([file[:-4] for file in os.listdir('lists') if file.endswith('.txt')])
            print(f"Available lists: {available_lists_str}")
            return
        with open(list_file, 'r') as file:
            available_lists[placeholder] = [line.strip() for line in file.readlines()]

    for line in zip(*available_lists.values()):
        output = input_text
        for idx, placeholder in enumerate(placeholders):
            output = re.sub(f"\[{placeholder}\]", line[idx], output)
        print(output)

if __name__ == "__main__":
    main()
