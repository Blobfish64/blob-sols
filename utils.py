def about_equals(input, expected, amount = 1):
    result = False
    if (input >= (expected - amount)) and (input <= (expected + amount)):
        result = True
    return result