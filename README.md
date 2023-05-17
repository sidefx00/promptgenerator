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


GetList.py

getlist.py is a Python script that uses the OpenAI API to generate a list of items based on a given subject. The script reads the API key from a config.ini file and appends the generated list to a text file in the lists directory. If the list file already exists, it will request new, unique items from the API and append them to the existing list.
Prerequisites

    Python 3
    openai Python package
    An OpenAI API key

Configuration

Before using the script, create a config.ini file in the same directory as the script. Use the following format to store your API key:

[openai]
api_key = your_api_key_here


Replace your_api_key_here with your actual OpenAI API key.
Usage

To run the script, use the following command:

python getlist.py "subject"

Replace subject with the desired subject for the list (e.g., "vehicles", "animals", etc.).

Example:
python getlist.py "vehicle"

This command will generate a list of vehicles and save it to the lists/vehicle.txt file. If the file already exists, new vehicles will be appended to the existing list.
