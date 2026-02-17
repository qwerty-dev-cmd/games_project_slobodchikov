"""Модуль для взаимодействия с пользователем."""

import prompt


def welcome_user():
    """Приветствует пользователя и запрашивает имя."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    
    # Возвращаем имя на случай, если понадобится в других модулях
    return name


if __name__ == "__main__":
    # Для тестирования при прямом запуске
    welcome_user()
