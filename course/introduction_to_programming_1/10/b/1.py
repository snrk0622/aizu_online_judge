import math
a, b, C = map(int, input().split())

S = a * b * math.sin(C) / 2
L = math.sprt(a**2 + b**2 - 2*a*b*math.cos(C))
h = S * 2 / a

print(S)
print(L)
print(h)