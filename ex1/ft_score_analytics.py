#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    args = sys.argv[1:]

    if len(args) == 0:
        print("No scores provided.")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")

        return

    scores = []

    for arg in args:
        try:
            scores.append(int(arg))
        except Exception:
            print(f"Invalid parameter: '{arg}'")

    if len(scores) == 0:
        print("No scores provided.")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total_player = len(scores)
    total_score = sum(scores)
    average_score = (sum(scores) / len(scores))
    high_score = max(scores)
    low_score = min(scores)
    score_range = max(scores) - min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_player}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
