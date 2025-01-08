n = int(input())
A = map(int, input().split())
print(*reversed(A))
# または
print(*A[::-1])