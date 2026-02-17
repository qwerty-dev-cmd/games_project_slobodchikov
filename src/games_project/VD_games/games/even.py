"""Игра 'Проверка на чётность'."""

import random


def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0


def get_question_and_answer():
    """
    Генерирует случайное число и правильный ответ (yes/no).
    
    Returns:
        tuple: (вопрос в виде строки, правильный ответ)
    """
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    
    return question, correct_answer


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
