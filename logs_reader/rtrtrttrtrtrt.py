from pathlib import Path  # Для роботи з шляхами до файлів
import re  # Для парсингу логів за допомогою регулярних виразів
import sys  # Для роботи з аргументами командного рядка
from collections import Counter  # Для підрахунку кількості логів за рівнями

def reed_logs_from_file(path: str) -> list[str]:
    """
    Функція для читання логів із файлу.
    Перевіряє наявність файлу та чи його можна відкрити.
    """
    path_path = Path(path)

    # Перевірка, чи існує файл
    if not path_path.exists():
        raise FileNotFoundError(f"Файл за шляхом {path} не знайдено.")
    
    # Перевірка на можливість читання файлу
    if not path_path.is_file():
        raise IsADirectoryError(f"{path} є директорією, а не файлом.")

    try:
        with open(f"{path_path}", 'r') as log_file:
            return log_file.readlines()  # Читання всіх рядків файлу
    except Exception as e:
        raise IOError(f"Помилка під час читання файлу {path}: {e}")

def parse_log_line(logs: list[str]):
    """
    Функція для парсингу логів. Витягає з кожного рядка дату, рівень та повідомлення.
    Перевіряє кожен рядок на відповідність шаблону.
    """
    result_list = []
    named_log_pattern = r'(?P<date_time>\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>[\w \.]+)'
    
    for log in logs:
        match = re.search(named_log_pattern, log)

        # Перевірка відповідності формату лог-рядка
        if match:
            result_list.append(match.groupdict())
        else:
            print(f"Попередження: Невірний формат логу в рядку: {log.strip()}")
    return result_list

def count_logs_by_level(parsed_logs: list) -> dict:
    """
    Функція для підрахунку кількості записів кожного рівня логування.
    """
    count = [log['level'] for log in parsed_logs]  # Збір рівнів логування
    counts = dict(Counter(count))  # Підрахунок частоти кожного рівня
    return counts

def filter_logs_by_level(parsed_logs, all_ifo_log: str):
    """
    Фільтрація логів за вказаним рівнем.
    Виводить лише ті логи, що відповідають вказаному рівню.
    """
    print(f"Деталі логів для рівня '{all_ifo_log.upper()}':")
    filtered_logs = [log for log in parsed_logs if log["level"].lower() == all_ifo_log.lower()]

    if not filtered_logs:
        print(f"Логи з рівнем '{all_ifo_log.upper()}' не знайдені.")
    else:
        for log in filtered_logs:
            print(log)

def display_log_counts(counts: dict):
    """
    Функція для відображення кількості логів за рівнями.
    """
    print(f"{'Level':<10} | {'Count':<5}")
    print("-" * 20)
    for level, count in counts.items():
        print(f"{level:<10} | {count:<5}")

# Основна частина програми
if __name__ == "__main__":
    try:
        # Перевірка на наявність аргументів командного рядка
        if len(sys.argv) < 2:
            raise IndexError("Usage: python parse_log_line.py <path_to_log_file> [log_level]")

        log_file_path = sys.argv[1]  # Отримання шляху до файлу логів
        all_ifo_log = sys.argv[2] if len(sys.argv) > 2 else None  # Опціональний аргумент для рівня логів

        # Виконання основних операцій
        logs = reed_logs_from_file(log_file_path)  # Читання лог-файлу
        parsed_logs = parse_log_line(logs)  # Парсинг логів
        log_counts = count_logs_by_level(parsed_logs)  # Підрахунок логів за рівнями
        display_log_counts(log_counts)  # Виведення результату

        # Якщо вказаний рівень логування, фільтруємо та відображаємо відповідні логи
        if all_ifo_log:
            filter_logs_by_level(parsed_logs, all_ifo_log)
    
    except (IndexError, FileNotFoundError, IsADirectoryError, IOError) as e:
        print(f"Помилка: {e}")
        sys.exit(1)
