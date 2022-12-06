with open('input.txt') as f:
    lines = f.readlines()

def find_start(text, length):
  for idx, _ in enumerate(text, start = length):
    items = set(text[idx-length:idx])
    if len(items) == length:
      return idx

print(find_start(lines[0], 4))
print(find_start(lines[0], 14))