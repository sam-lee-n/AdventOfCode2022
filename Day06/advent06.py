with open('input.txt') as f:
    lines = f.readlines()

for idx, _ in enumerate(lines[0], start = 4):
  items = set(lines[0][idx-4:idx])
  if len(items) == 4:
    break
print(idx)

for idx, _ in enumerate(lines[0], start = 14):
  items = set(lines[0][idx-14:idx])
  if len(items) == 14:
    break
print(idx)