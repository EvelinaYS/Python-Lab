def limit_calls(max_calls=None):
    if callable(max_calls):
        func = max_calls
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            print(f"Вызов №{count}")
            return func(*args, **kwargs)

        return wrapper

    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count

            if count >= max_calls:
                print("Стоп: слишком много вызовов")
                return None

            count += 1

            print(f"Вызов №{count}")

            return func(*args, **kwargs)

        return wrapper

    return decorator

@limit_calls
def hello(name):
    print(f"Привет, {name}!")

hello("Анна")
hello("Иван")

@limit_calls(3)
def square(x):
    return x * x

print(square(2))
print(square(3))
print(square(4))
print(square(5))

@limit_calls(10)
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))