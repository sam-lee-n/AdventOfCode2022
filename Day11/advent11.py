import re
from functools import reduce

with open('input.txt') as f:
    lines = f.readlines()

forest = {}
ans = {}

for x, line in enumerate(lines):
    if line.startswith('Monkey'):
        num = [int(s) for s in re.findall(r'\b\d+\b', line)][0]

        items = [int(s) for s in re.findall(r'\b\d+\b', lines[x+1].strip())]

        operation = lines[x+2].strip().split()[-2::]
        # print(operation)

        test = []
        for y in range (3):
            test.append (int(lines[x+3+y].strip().split()[-1]))
        # print(test)

        forest[num] = [items, operation, test]

allTest = []
for monkey in range(len(forest)):
    allTest.append(forest[monkey][2][0])
allTest = reduce(lambda x, y: x*y, allTest)

management = 1
for cycle in range(10000):
    for monkey in range(len(forest)):
        while(forest[monkey][0]):
            item = forest[monkey][0].pop(0)

            if forest[monkey][1][1].isdigit():
                num = int(forest[monkey][1][1])
                if forest[monkey][1][0] == '*':
                    worry = (item * num) // management
                else:
                    worry = (item + num) // management
            else:
                worry = (item * item) // management

            if worry %  forest[monkey][2][0] == 0:
                forest[forest[monkey][2][1]][0].append(worry % allTest)
            else:
                forest[forest[monkey][2][2]][0].append(worry % allTest)
            
            if monkey in ans:
                ans[monkey] += 1
            else:
                ans[monkey] = 1
            

print(ans)
sortedAns = [value for value in ans.values()]
sortedAns.sort()
print(sortedAns[-1]* sortedAns[-2])



