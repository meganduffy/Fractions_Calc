from fractions import Fraction, gcd


class FractionClass:
    def __init__(self, numerator, denominator):
        if float in [type(numerator), type(denominator)]:
            self.num = Fraction(numerator).limit_denominator()
            self.den = Fraction(denominator).limit_denominator()
        else:
            self.num = numerator
            self.den = denominator
        self.mod = divmod(self.num, self.den)

    def __repr__(self, num, den):
        return "%s %s/%s" % (self.mod[0], self.mod[1], self.den)

    def __add__(self, other):
        num = (self.num * other.den) + (self.den * other.num)
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __div__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __eq__(self, other):
        return Fraction(self.num, self.den) == Fraction(other.num, other.den)

    def __ne__(self, other):
        return Fraction(self.num, self.den) != Fraction(other.num, other.den)

    def __lt__(self, other):
        return Fraction(self.num, self.den) < Fraction(other.num, other.den)

    def __le__(self, other):
        return Fraction(self.num, self.den) <= Fraction(other.num, other.den)

    def __gt__(self, other):
        return Fraction(self.num, self.den) > Fraction(other.num, other.den)

    def __ge__(self, other):
        return Fraction(self.num, self.den) >= Fraction(other.num, other.den)


a = FractionClass(4, 1)
b = FractionClass(1, 3)
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

assert not f5
assert f6
assert not f8
assert f9
assert f10
print "All assertions passed."

