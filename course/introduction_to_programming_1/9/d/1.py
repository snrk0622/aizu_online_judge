str = input()
n = int(input())

def printStr(s, a, b):
  a, b = int(a), int(b)
  print(s[a:b+1])

def reverseStr(s, a, b):
  a, b = int(a), int(b)
  return s[:a] + ''.join(reversed(s[a:b+1])) + s[b+1:]

def replaceStr(s, a, b, p):
  a, b = int(a), int(b)
  return s[:a] + p + s[b+1:]

ans = str
for _ in range(n):
  inputs = input().split()
  func = inputs[0]
  if func == 'print':
    _, a, b = inputs
    printStr(ans, a, b)
  elif func == 'reverse':
    _, a, b = inputs
    ans = reverseStr(ans, a, b)
  elif func == 'replace':
    _, a, b, p = inputs
    ans = replaceStr(ans, a, b, p)