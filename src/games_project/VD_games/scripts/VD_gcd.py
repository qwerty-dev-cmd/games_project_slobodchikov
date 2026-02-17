#!/usr/bin/env python3
"""Точка входа для игры 'НОД'."""

from games_project.VD_games.engine import run_game
from games_project.VD_games.games import gcd


def main():
    """Запускает игру 'НОД'."""
    run_game(gcd, gcd.DESCRIPTION)


if __name__ == "__main__":
    main()
