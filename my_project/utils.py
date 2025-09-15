# utils.py

def list_to_string(input_list):
    """Converts a list of items to a comma-separated string."""
    result = ""
    for item in input_list:
        result += str(item) + ", "
    return result.strip().strip(',')

def add_numbers(a, b):
    return a + b