def chaib_sum(number):
    result = number
    def wrapper(number2 = None):
        nonlocal result
        if number2 is None:
            return result
        result += number2
        return result
    return wrapper

print(chaib_sum(5)())
print(chaib_sum(5)(2))