while True:
  H, W = map(int, input().split())
  if H == 0 and W == 0: break
  for h in range(H):
    h += 1
    for w in range(W):
      w += 1
      print('#' if h % 2 == w % 2 else '.', end='')
    print()
  print()