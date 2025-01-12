n = int(input())
scores = [0, 0]
for _ in range(n):
  cards = input().split()
  if cards[0] == cards[1]:
    scores[0], scores[1] = scores[0] + 1, scores[1] + 1
  elif cards[0] > cards[1]:
    scores[0] += 3
  else:
    scores[1] += 3
print(*scores)