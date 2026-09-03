from help_func import *

class Fraction:
    def __init__(self, numerator: str, denominator: str):
        if (not is_digits(numerator)) or (not is_digits(denominator)):
            raise TypeError("Введите в полях числителей и знаменатилей целые числа!")

        if denominator == "0":
            raise ZeroDivisionError("На ноль делить нельзя!")

        self.numerator = int(numerator)
        self.denominator = int(denominator)

        if self.denominator < 0:
            self.denominator *= -1
        
        gcd_of_numbers = gcd(self.denominator, self.numerator)

        self.numerator //= gcd_of_numbers
        self.denominator //= gcd_of_numbers


    def getInfo(self):
        return (int(self.numerator), int(self.denominator))


    def sumFractions(self, other):
        other_numerator, other_denominator = other.getInfo()
        return Fraction(str(self.numerator * other_denominator + other_numerator * self.denominator), str(self.denominator * other_denominator))


    def multiFractions(self, other):
        other_numerator, other_denominator = other.getInfo()
        return Fraction(str(self.numerator * other_numerator), str(self.denominator * other_denominator))


    def subFractions(self, other):
        return self.sumFractions(other.multiFractions(Fraction("-1", "1")))


    def divFractions(self, other):
        other_numerator, other_denominator = other.getInfo()
        return self.multiFractions(Fraction(str(other_denominator * (-1 if int(other_numerator) < 0 else 1)), str(other_numerator)))


    def __str__(self):
        return f"{self.numerator} / {self.denominator}"