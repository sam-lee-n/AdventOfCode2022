with open('.txt') as f:
    lines = f.readlines()

total = 0
elf = []
for line in lines:
  if line != '\n':
    total += int(line)
  else:
    elf.append(total)
    total = 0

print(max(elf))
print(sum(sorted(elf)[-3::]))
