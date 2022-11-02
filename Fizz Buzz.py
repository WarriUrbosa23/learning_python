def fizz_buzz(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    if number % 3 == 0 and number % 5 != 0:
        return "Fizz"
    if number % 5 == 0 and number % 3 != 0:
        return "Buzz"
    else:
        return str(number)
a = input("Input any number: ")
a = float(a)

assert fizz_buzz(a) == "Fizz Buzz"
assert fizz_buzz(a) == "Fizz"
assert fizz_buzz(a) == "Buzz"
assert fizz_buzz(a) == "7"
