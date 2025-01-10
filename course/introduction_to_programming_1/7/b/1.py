import itertools
while True:
  n, x = map(int, input().split())
  if n == 0 and x == 0: break
  ans = 0
  combinations = itertools.combinations(range(1, n+1), 3)
  for combi in combinations:
    if sum(combi) == x: ans += 1
  print(ans)