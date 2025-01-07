n = int(input())
ans = ' '
for x in range(3, n+1):
  if x % 3 == 0 or str(x).find('3') != -1:
    ans += f'{x} '
print(ans)