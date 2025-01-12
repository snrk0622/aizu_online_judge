import math

while True:
  n = int(input())
  if n == 0: break
  S = list(map(int, input().split()))

  m = sum(S) / len(S)
  a = math.sqrt(sum(map(lambda x: (x - m)**2, S)) / n)
  print(a)