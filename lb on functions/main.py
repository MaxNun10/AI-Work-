def calculator(a, b, operation="add", *args, **kwargs):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else float('inf')
    }

    if operation not in operations:
        raise ValueError("Unsupported operation")

    result = operations[operation](a, b)

    for num in args:
        result = operations[operation](result, num)

    if kwargs.get("round_result", False):
        result = round(result)

    if kwargs.get("log_result", False):
        print(f"Result: {result}")

    return result



print(calculator(10, 5, "add", 2, 3, round_result=True, log_result=True))  # Додавання з округленням і логуванням
print(calculator(10, 5, "divide", log_result=True))  # Ділення з логуванням