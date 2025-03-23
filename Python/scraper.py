import json
import os

# Obtaining data in JSON format
def load_data(filepath):
    try:
        with open(filepath, encoding="utf8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON data: {e}")
        exit(1)
