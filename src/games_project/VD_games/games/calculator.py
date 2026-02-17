"""Игра 'Калькулятор': вычисление случайного математического выражения."""

import random
import operator


# Словарь с операциями: символ -> функция
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_question_and_answer():
    """
    Генерирует случайное математическое выражение и правильный ответ.
    
    Returns:
        tuple: (вопрос в виде строки, правильный ответ)
    """
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op_symbol = random.choice(list(OPERATIONS.keys()))
    
    # Вычисляем правильный ответ
    op_func = OPERATIONS[op_symbol]
    correct_answer = op_func(num1, num2)
    
    # Формируем вопрос
    question = f"{num1} {op_symbol} {num2}"
    
    return question, correct_answer


# Описание игры для движка
DESCRIPTION = "What is the result of the expression?"
