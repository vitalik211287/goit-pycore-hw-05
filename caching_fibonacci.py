def caching_fibonacci():
    # Створюємо кеш для зберігання обчислених значень
    cache = {}

    # Внутрішня функція для обчислення числа Фібоначчі
    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Якщо число вже є у кеші, повертаємо його
        if n in cache:
            return cache[n]

        # Інакше обчислюємо його рекурсивно і зберігаємо в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        print(cache[n])
        return cache[n]
    print(cache)
    # Повертаємо внутрішню функцію fibonacci
    return fibonacci


fib = caching_fibonacci()
print(fib(20)) 
print(fib(5))  
