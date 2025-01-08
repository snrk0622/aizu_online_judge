N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [int(input()) for _ in range(M)]

for i in range(N):
  ans = 0
  for m in range(M):
    ans += A[i][m] * B[m]
  print(ans)