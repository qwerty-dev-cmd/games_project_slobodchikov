#!/usr/bin/env python3
"""Точка входа для игры 'Простое число'."""

from games_project.VD_games.engine import run_game
from games_project.VD_games.games import prime


def main():
    """Запускает игру 'Простое число'."""
    run_game(prime, prime.DESCRIPTION)


if __name__ == "__main__":
    main()
