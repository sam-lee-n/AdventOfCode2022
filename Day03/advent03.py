with open('input.txt') as f:
    lines = f.readlines()

total = 0
for line in lines:
    mid = len(line)//2
    commonItem = ''.join(set(line[0:mid]).intersection(line[mid::]))
    if commonItem.isupper():
        total += ord(commonItem) - 64 + 26
    else:
        total += ord(commonItem) - 96

print(total)

total = 0
for x in range(len(lines)//3):
    y = int(x * 3)
    commonItem = set(lines[y]).intersection(
        lines[y+1])
    commonItem = ''.join(commonItem.intersection(lines[y+2])).strip()
    if commonItem.isupper():
        total += ord(commonItem.strip()) - 64 + 26
    else:
        total += ord(commonItem) - 96
print(total)
