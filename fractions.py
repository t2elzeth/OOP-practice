SPLITTER = '/'


class Fraction:
    def __init__(self, str_fraction: str, splitter: str = SPLITTER):
        splitted_fraction = str_fraction.split(splitter)
        numerator = splitted_fraction[0]
        denominator = splitted_fraction[1]

        self.numerator = int(numerator)
        self.denominator = int(denominator)
        self.splitter = splitter

    def __format_fraction(self, numerator, denominator):
        return f'{numerator}{self.splitter}{denominator}'

    def __get_class(self, numerator, denominator):
        return self.__class__(self.__format_fraction(numerator, denominator), self.splitter)

    def __add__(self, other):
        if self.denominator != other.denominator:
            denominator = self.denominator * other.denominator
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            return self.__get_class(numerator, denominator)

        if self.denominator == other.denominator:
            numerator = self.numerator + other.numerator
            denominator = self.denominator
            return self.__get_class(numerator, denominator)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if self.denominator != other.denominator:
            denominator = self.denominator * other.denominator
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            return self.__get_class(numerator, denominator)

        if self.denominator == other.denominator:
            numerator = self.numerator - other.numerator
            denominator = self.denominator
            return self.__get_class(numerator, denominator)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return self.__get_class(numerator, denominator)

    def __imul__(self, other):
        return self.__mul__(other)

    def __divmod__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return self.__get_class(numerator, denominator)

    def __idiv__(self, other):
        return self.__divmod__(other)

    def __float__(self):
        return self.numerator / self.denominator

    def __str__(self):
        return f'{self.numerator}{self.splitter}{self.denominator}'

    def __bool__(self):
        return self.numerator > self.denominator


fr1 = Fraction('1/5')
fr2 = Fraction('3/5')
fr3 = Fraction('1/6')
print(fr1 + fr2)
print(fr1 + fr3)
print(fr2 - fr1)
print(float(fr1 + fr2))
