R, C = map(int, input().split())
squares = [list(map(int, input().split())) for _ in range(R)]

ans_squares = list(map(lambda square: [*square, sum(square)], squares))
last_row = []
for c in range(C+1):
  sum = 0
  for r in range(R):
    sum += ans_squares[r][c]
  last_row.append(sum)
ans_squares.append(last_row)

for row in ans_squares:
  print(*row)