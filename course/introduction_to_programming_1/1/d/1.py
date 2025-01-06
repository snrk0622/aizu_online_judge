S = int(input())
h, M = divmod(S, 3600)
m, s = divmod(M, 60)
print(f'{h}:{m}:{s}')