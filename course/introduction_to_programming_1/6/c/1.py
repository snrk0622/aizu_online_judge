n = int(input())
ans = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]
for _ in range(n):
  b, f, r, v = map(int, input().split())
  b, f, r = b-1, f-1, r-1
  ans[b][f][r] = max(ans[b][f][r] + v, 0)

for b in range(len(ans)):
  for f in range(len(ans[b])):
    for r in ans[b][f]:
      print(f' {r}', end="")
    print()
  if b != len(ans) - 1: print('####################')