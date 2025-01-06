W, H, x, y, r = map(int, input().split())
max_x, min_x = x + r, x - r
max_y, min_y = y + r, y - r

if max_x <= W and min_x >= 0 and max_y <= H and min_y >= 0:
  print('Yes')
else:
  print('No')