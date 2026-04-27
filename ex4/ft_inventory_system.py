#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error- invalid parameter '{arg}'")
            continue

        name, qty = arg.split(":", 1)

        if name in inventory:
            print(f"Redundant item '{name}'- discarding")
            continue

        try:
            inventory[name] = int(qty)
        except Exception as e:
            print(f"Quantity error for '{name}': {e}")

    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    for k in inventory:
        percent = round((inventory[k] / total) * 100, 1)
        print(f"Item {k} represents {percent}%")

    if inventory:
        max_item = max(inventory, key=lambda k: inventory[k])
        min_item = min(inventory, key=lambda k: inventory[k])

        print(
            f"Item most abundant: {max_item} "
            f"with quantity {inventory[max_item]}"
        )
        print(
            f"Item least abundant: {min_item} "
            f"with quantity {inventory[min_item]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
