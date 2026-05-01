#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players = [
            'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
            'Gregory', 'john', 'kevin', 'Liam'
            ]

    print(f"Initial list of players: {players}")

    all_caps = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {all_caps}")

    already_caps = [p for p in players if p[0].isupper()]
    print(f"New list of capitalized names only: {already_caps}")

    scores = {p: random.randint(50, 1000) for p in all_caps}
    print(f"\nScore dict: {scores}")

    avg = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")

    high_scores = {k: v for k, v in scores.items() if v > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
