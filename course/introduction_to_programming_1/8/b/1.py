from functools import reduce

while True:
  x = input()
  if x == '0': break
  print(reduce(lambda acc, item: acc + int(item), list(x), 0))