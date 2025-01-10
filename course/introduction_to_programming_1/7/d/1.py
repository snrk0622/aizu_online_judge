N, M, L = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(M)]

C = [[0 for _ in range(L)] for _ in range(N)]
for i in range(N):
  for j in range(L):
    C[i][j] = sum([A[i][k] * B[k][j] for k in range(M)])
      

for row in C:
  print(*row)