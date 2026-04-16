#!/usr/bin/env python3

import random


def gen_player_achievements() -> set:
    achievements = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Strategist", "Speed Runner", "Survivor",
        "Treasure Hunter", "First Steps", "Sharp Mind"
    ]

    count = random.randint(5, len(achievements))
    return set(random.sample(achievements, count))


def main() -> None:
    print("=== Achievement Tracker System ===")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, ach in players.items():
        print(f"Player {name}: {ach}")

    all_ach: set[str] = set()
    for ach in players.values():
        all_ach = all_ach.union(ach)

    common = set.intersection(*players.values())

    print(f"All distinct achievements: {all_ach}")
    print(f"Common achievements: {common}")

    for name, ach in players.items():
        others = all_ach.difference(ach)
        only = ach.difference(all_ach - ach)
        print(f"Only {name} has: {only}")
        print(f"{name} is missing: {others}")


if __name__ == "__main__":
    main()
