"""Игра 'Простое число': проверка, является ли число простым."""

import random


def is_prime(number):
    """
    Проверяет, является ли число простым.
    
    Args:
        number: целое положительное число
        
    Returns:
        bool: True если число простое, иначе False
    """
    if number < 2:
        return False
    
    # Проверяем делители до квадратного корня из числа
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


def get_question_and_answer():
    """
    Генерирует случайное число и правильный ответ (yes/no).
    
    Returns:
        tuple: (вопрос, правильный ответ)
    """
    number = random.randint(1, 50)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    
    return question, correct_answer


# Описание игры для движка
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
