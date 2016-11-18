from fractions import Fraction, gcd

class Fraction_class:
    def __init__(self, numerator, denominator):
        if numerator == float or denominator == float:
            new = Fraction(self.num).limit_denominator()
            self.num = int(str(new)[0])
            self.den = int(str(new)[2])

        self.num = numerator
        self.den = denominator
        self.mod = divmod(self.num, self.den)


    def __repr__(self, num, den):
        return "%s %s/%s" % (self.mod[0], self.mod[1], self.den)

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        if num < den:
            return Fraction(num, den)
        else:
            return "%s %s" % (self.mod[0], Fraction(self.mod[1], self.den))

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        if num < den:
            return Fraction(num, den)
        else:
            return "%s %s" % (self.mod[0], Fraction(self.mod[1], self.den))

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)
    def __div__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)


    def __eq__(self, other):
        if Fraction(self.num, self.den) == Fraction(other.num, other.den):
            return "True"
        else:
            return "False"
    def __ne__(self, other):
        if Fraction(self.num, self.den) != Fraction(other.num, other.den):
            return "True"
        else:
            return "False"
    def __lt__(self, other):
        if Fraction(self.num, self.den) < Fraction(other.num, other.den):
            return "True"
        else:
            return "False"
    def __le__(self, other):
        if Fraction(self.num, self.den) <= Fraction(other.num, other.den):
            return "True"
        else:
            return "False"
    def __gt__(self, other):
        if Fraction(self.num, self.den) > Fraction(other.num, other.den):
            return "True"
        else:
            return "False"
    def __ge__(self, other):
        if Fraction(self.num, self.den) >= Fraction(other.num, other.den):
            return "True"
        else:
            return "False"


a = Fraction_class(0.4, 1)
b = Fraction_class(1, 3)
f1 = a + b
f2 = a - b
f3 = a * b
f4 = a / b
f5 = a == b
f6 = a != b
f7 = a < b
f8 = a <= b
f9 = a > b
f10 = a >= b

print f1
