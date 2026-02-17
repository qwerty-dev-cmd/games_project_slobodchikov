#!/usr/bin/env python3
"""Точка входа для игры 'Проверка на чётность'."""

from games_project.VD_games.engine import run_game
from games_project.VD_games.games import even


def main():
    """Запускает игру 'Проверка на чётность'."""
    run_game(even, even.DESCRIPTION)


if __name__ == "__main__":
    main()
