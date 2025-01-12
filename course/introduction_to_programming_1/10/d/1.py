import math
n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

p1 = 0
for i in range(n):
  p1 += abs(X[i] - Y[i])
print(p1)

p2 = 0
for i in range(n):
  p2 += (X[i] - Y[i])**2
print(math.sqrt(p2))

p3 = 0
for i in range(n):
  p3 += (X[i] - Y[i])**3
print(math.pow(p3, 1/3))

pn = 0
for i in range(n):
  pn = max(pn, abs(X[i] - Y[i]))
print(pn)