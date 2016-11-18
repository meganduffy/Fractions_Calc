import fractions

a = 11
b = 8
c = 0.2

new = fractions.Fraction(c).limit_denominator()
print new
print int(str(new)[2])