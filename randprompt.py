import sys
import os
import random
import argparse
import re

def main():
    parser = argparse.ArgumentParser(description='Generate random prompts.')
    parser.add_argument('-n', '--number', type=int, help='Number of prompts to generate.')
    parser.add_argument('input_text', type=str, nargs='?', help='Your text with [placeholder]')
    args = parser.parse_args()

    if args.number is None or args.input_text is None:
        print("Usage: randprompt.py -n <number_of_prompts> \"Your text with [placeholder]\"")
        return

    num_prompts = args.number
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

    for _ in range(num_prompts):
        output = input_text
        for placeholder in placeholders:
            output = re.sub(f"\[{placeholder}\]", random.choice(available_lists[placeholder]), output)
        print(output)

if __name__ == "__main__":
    main()
