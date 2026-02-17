#!/usr/bin/env python3
"""Точка входа для игры 'Арифметическая прогрессия'."""

from games_project.VD_games.engine import run_game
from games_project.VD_games.games import progression


def main():
    """Запускает игру 'Арифметическая прогрессия'."""
    run_game(progression, progression.DESCRIPTION)


if __name__ == "__main__":
    main()
