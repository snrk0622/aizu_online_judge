S = input()
p = input()

for i in range(len(S)):
  s = [*S[i:], *S[:i]]
  if p in s:
    print('Yes')
    exit()
print('No')