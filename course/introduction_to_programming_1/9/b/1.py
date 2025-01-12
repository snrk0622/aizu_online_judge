while True:
  cards = input()
  if cards == '-': break
  m = int(input())
  ans = cards
  for _ in range(m):
    h = int(input())
    ans = [*ans[h:], *ans[:h]]
  print(''.join(ans))