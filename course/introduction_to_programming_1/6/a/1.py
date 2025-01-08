n = int(input())
A = map(int, input().split())
for i in range(1, n+1):
  print(A[-i])