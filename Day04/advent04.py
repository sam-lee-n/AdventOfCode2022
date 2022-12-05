import re

with open('input.txt') as f:
    lines = f.readlines()

total = 0
for line in lines:
  groups = [int(s) for s in re.findall(r'\b\d+\b', line)]
  if groups[3] < groups[1]:
    if groups[2] >= groups[0]:
      total += 1
  elif groups[3] > groups[1]:
    if groups[0] >= groups[2]:
      total += 1
  else:
    total += 1

print(total)

total = 0
for line in lines:
  groups = [int(s) for s in re.findall(r'\b\d+\b', line)]
  if groups[3] < groups[1]:
    if groups[3] >= groups[0]:
      total += 1
  elif groups[3] > groups[1]:
    if groups[1] >= groups[2]:
      total += 1
  else:
    total += 1

print(total)