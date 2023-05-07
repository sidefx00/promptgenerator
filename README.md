# Prompt Generator

The Prompt Generator is a simple Python script that generates randomized prompts based on input text with placeholders. This project is useful for generating a variety of randomized text outputs for creative writing, brainstorming ideas, or simply for fun.

## Requirements

- Python 3.6 or higher

## Usage

```bash
python randprompt.py -n <number_of_prompts> "Your text with [placeholder]"

    <number_of_prompts>: The number of randomized prompts you want to generate.
    [placeholder]: Placeholders in the input text that will be replaced with random items from the corresponding list. Placeholders should be enclosed in square brackets, and the name should match the name of a list file (without the .txt extension) in the lists directory.

For example:

python randprompt.py -n 3 "I saw a [animal] at the [location] wearing a [clothing]."

This command will generate three randomized prompts using items from the animal, location, and clothing lists.
Adding New Lists

To add a new list of items for use as placeholders:

    Create a new text file in the lists directory with a descriptive name.
    Add one item per line in the text file.
    Use the name of the text file (without the .txt extension) as a placeholder in your input text.
