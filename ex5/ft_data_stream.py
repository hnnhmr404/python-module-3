#!/usr/bin/env python3

import random
from typing import Generator


def gen_event() -> Generator[tuple, None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
            "run", "eat", "sleep", "grab",
            "move", "climb", "swim", "release"
            ]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list) -> Generator[tuple, None, None]:
    while len(events) > 0:
        i = random.randrange(len(events))
        yield events.pop(i)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    gen = gen_event()

    for i in range(1000):
        e = next(gen)
        print(f"Event {i}: Player {e[0]} did action {e[1]}")

    events = [next(gen) for _ in range(10)]
    print(f"Built list of 10 events: {events}")

    for e in consume_event(events):
        print(f"Got event from list: {e}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
