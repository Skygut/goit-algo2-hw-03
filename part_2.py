import csv
from BTrees.OOBTree import OOBTree
import timeit


# Load data from CSV
def load_data(filename):
    items = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["ID"] = int(row["ID"])
            row["Price"] = float(row["Price"])
            items.append(row)
    return items


# Add items to OOBTree
def add_item_to_tree(tree, item):
    tree[item["ID"]] = item


# Add items to dictionary
def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = item


# Range query for OOBTree
def range_query_tree(tree, min_price, max_price):
    return [
        value for key, value in tree.items() if min_price <= value["Price"] <= max_price
    ]


# Range query for dictionary
def range_query_dict(dictionary, min_price, max_price):
    return [
        value
        for key, value in dictionary.items()
        if min_price <= value["Price"] <= max_price
    ]


# Main program
def main():
    # Load data
    filename = "./generated_items_data.csv"  # Path updated to root folder
    data = load_data(filename)

    # Initialize data structures
    tree = OOBTree()
    dictionary = {}

    # Add items to both structures
    for item in data:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    # Define range query parameters
    min_price = 10.0
    max_price = 50.0

    # Measure performance for OOBTree
    tree_time = timeit.timeit(
        lambda: range_query_tree(tree, min_price, max_price), number=100
    )

    # Measure performance for dictionary
    dict_time = timeit.timeit(
        lambda: range_query_dict(dictionary, min_price, max_price), number=100
    )

    # Output results
    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")


if __name__ == "__main__":
    main()
