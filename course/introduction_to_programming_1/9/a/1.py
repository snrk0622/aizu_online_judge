W = input()

ans = 0
while True:
  T = input().split()
  if T[0] == 'END_OF_TEXT': break
  for t in T:
    if t.lower() == W: ans += 1

print(ans)