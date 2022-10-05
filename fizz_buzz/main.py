def fizz_buzz(value: int) -> str:
    result = ''
    if value % 3 == 0 and value % 5 == 0:
        result = 'fizzBuzz'
    elif value % 3 == 0:
        result = 'fizz'
    elif value % 5 == 0:
        result = 'buzz'

    return result
