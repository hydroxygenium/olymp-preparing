a, b, c, d = map(int, input('nums: ').split())
F = lambda x: a * x**4 + b * x**3 + c * x**2 + d * x
print(F(2))
