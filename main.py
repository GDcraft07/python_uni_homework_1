from fraction import *


def step():
    numerator_1 = input("Введите числитель первого числа: ")
    denominator_1 = input("Введите знаменатель первого числа: ")

    numerator_2 = input("Введите числитель второго числа: ")
    denominator_2 = input("Введите знаменатель второго числа: ")

    sign = input("Введите операцию: ")

    fraction_1 = Fraction(numerator_1, denominator_1)
    fraction_2 = Fraction(numerator_2, denominator_2)

    result = None

    if sign == "+":
        result = fraction_1.sumFractions(fraction_2)

    elif sign == "-":
        result = fraction_1.subFractions(fraction_2)

    elif sign == "*":
        result = fraction_1.multiFractions(fraction_2)

    elif sign == "/":
        result = fraction_1.divFractions(fraction_2)

    else:
        print("Введен неправильный символ операции.")

    if result:
        print(result)


if __name__ == "__main__":
    step()