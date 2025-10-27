import json
from datetime import datetime

# Global variable to store stock data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add a specified quantity of an item to the inventory.
    Creates a new item entry if it does not exist.
    """
    if logs is None:
        logs = []

    if not item or not isinstance(item, str) or not isinstance(qty, int):
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove a specified quantity of an item from the inventory.
    Deletes the item entry if quantity becomes zero or negative.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: '{item}' not found in inventory.")


def get_qty(item):
    """Return the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        stock_data = {}
        print("No inventory file found. Starting with empty inventory.")


def save_data(file_path="inventory.json"):
    """Save current inventory data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """Print all items and their quantities."""
    print("\n--- Inventory Report ---")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold=5):
    """Return a list of items with stock below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("mango", 8)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print("Low stock items:", check_low_items())
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
