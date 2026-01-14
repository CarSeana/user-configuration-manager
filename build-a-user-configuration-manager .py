** start of main.py **

def add_setting(dic,tup):
    """
    Adds a key-value setting to the dictionary.
    Converts both key and value to lowercase.
    Returns a message indicating success or if the key already exists.
    """
    key, value = tup
    key = key.lower()
    value = value.lower()

    if key in dic:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    else:
        dic[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dic,tup):
    """
    Updates the value of an existing key in the dictionary.
    Converts both key and value to lowercase.
    Returns a message indicating success or if the key does not exist.
    """
    key, value = tup
    key = key.lower()
    value = value.lower()

    if key in dic:
        dic[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dic,k):
    """
    Deletes a key from the dictionary if it exists.
    Returns a message indicating success or if the key is not found.
    """
    key = k.lower()

    if key in dic:
        del dic[key] 
        return f"Setting '{key}' deleted successfully!"

    else:
        return "Setting not found!"

def view_settings(dic):
    """
    Returns a formatted string of all key-value pairs in the dictionary.
    If the dictionary is empty, returns a message indicating no settings.
    """
    if not dic:
        return 'No settings available.'

    prompt = "Current User Settings:"

    for key, value in dic.items():
        prompt += f"\n{key.capitalize()}: {value}"
    return prompt + "\n"

# Demo usage
if __name__ == "__main__":
    print("=== User Configuration Manager Demo ===")

    test_settings = {
    "theme": "light",
    "volume": "high",
    "notifications": "enabled"
}

print(add_setting(test_settings, ("Theme", "Dark")))
print(update_setting(test_settings, ("Volume", "Low")))
print(delete_setting(test_settings, "Notifications"))
print(view_settings(test_settings))






** end of main.py **

