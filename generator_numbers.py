import re
from typing import Callable

# Функція, яка генерує дійсні числа з тексту
def generator_numbers(text: str):
    # Регулярний вираз для пошуку чисел (включаючи дробові)
    pattern = r'\b\d+\.\d+|\b\d+'
    
    # Пошук усіх збігів у тексті
    matches = re.findall(pattern, text)
    
    # Повертаємо кожне число як float через yield
    for match in matches:
        yield float(match)

# Функція для обчислення загальної суми чисел
def sum_profit(text: str, func: Callable):
    # Викликаємо функцію для генерації чисел і підсумовуємо їх
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
