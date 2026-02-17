#!/usr/bin/env python3
"""Точка входа для игры 'Калькулятор'."""

from games_project.VD_games.engine import run_game
from games_project.VD_games.games import calculator


def main():
    """Запускает игру 'Калькулятор'."""
    run_game(calculator, calculator.DESCRIPTION)


if __name__ == "__main__":
    main()
