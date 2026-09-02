def gcd(number_1: int, number_2: int):
    while number_2:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1 if number_1 >= 0 else -number_1


is_digits = lambda str_number: str_number != "" and all(map(lambda x: x.isdigit(), list(str_number if str_number[0] != "-" else str_number[1:])))
