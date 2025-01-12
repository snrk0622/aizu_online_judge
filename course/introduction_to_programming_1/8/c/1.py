import string
import sys

str = sys.stdin.read()
for char in string.ascii_lowercase:
  print(f'{char} : {str.lower().count(char)}')