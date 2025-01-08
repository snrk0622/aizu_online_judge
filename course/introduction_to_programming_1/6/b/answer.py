n = int(input())
d = [i + ' ' + str(j) for i in 'SHCD' for j in range(1, 14)]
for _ in range(n):
  d.remove(input())
for i in d:
  print(i)