"""Игра 'Арифметическая прогрессия': найти пропущенное число."""

import random


def generate_progression():
    """
    Генерирует арифметическую прогрессию со спрятанным элементом.
    
    Returns:
        tuple: (строка с прогрессией для вопроса, правильный ответ)
    """
    # Параметры прогрессии
    length = random.randint(5, 10)  # длина от 5 до 10
    start = random.randint(1, 20)    # начальное число
    step = random.randint(2, 5)       # шаг прогрессии
    
    # Создаём прогрессию
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))
    
    # Выбираем случайный индекс для пропуска
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    
    # Заменяем выбранный элемент на ".."
    progression[hidden_index] = ".."
    
    # Формируем вопрос
    question = " ".join(progression)
    
    return question, correct_answer


def get_question_and_answer():
    """
    Обёртка для совместимости с движком.
    
    Returns:
        tuple: (вопрос, правильный ответ)
    """
    return generate_progression()


# Описание игры для движка
DESCRIPTION = "What number is missing in the progression?"
