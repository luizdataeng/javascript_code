import json

def open_json_file(filepath):
    """
    Opens a JSON file and returns the data as a Python dictionary.

    Args:
        filepath (str): The path to the JSON file.

    Returns:
        dict: The JSON data as a dictionary, or None if an error occurs.
    """
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filepath}")
        return None
    except Exception as e: # Catch any other potential errors.
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
file_path = 'high.json' # Replace with the actual path to your JSON file.

data = open_json_file(file_path)

if data:
    print("JSON data loaded successfully:")
    print(json.dumps(data, indent=4)) # Pretty-print the JSON data.
    # Access data like a dictionary:
    # print(data["key"])
else:
    print("Failed to load JSON data.")
