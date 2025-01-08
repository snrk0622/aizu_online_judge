n = int(input())
cards = {
  'S': [],
  'H': [],
  'C': [],
  'D': [],
}
for _ in range(n):
  str, num = input().split()
  num = int(num)
  cards[str].append(num)

for key in cards.keys:
  cards[str].sort()
  for num in range(1, 14):
    if not num in cards[key]: print(key, num)