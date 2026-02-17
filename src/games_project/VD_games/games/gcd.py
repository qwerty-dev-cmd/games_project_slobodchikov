"""Игра 'НОД': нахождение наибольшего общего делителя."""

import random
import math


def get_question_and_answer():
    """
    Генерирует два случайных числа и их НОД.
    
    Returns:
        tuple: (вопрос в виде строки, правильный ответ)
    """
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    
    # Вычисляем НОД с помощью встроенной функции math.gcd
    correct_answer = math.gcd(num1, num2)
    
    # Формируем вопрос
    question = f"{num1} {num2}"
    
    return question, correct_answer


# Описание игры для движка
DESCRIPTION = "Find the greatest common divisor of given numbers."
