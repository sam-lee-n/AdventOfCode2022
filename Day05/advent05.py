import re

with open('input.txt') as f:
    lines = f.readlines()

loaded = 1
track = 0

for line in lines:
    track += 1
    if '1' in line:
        break

valList = lines[track-1].split()

myShip = list = [[] for i in range(len(valList))]

for stack in range(len(valList)):
    for item in range(track-2, -1, -1):
        if lines[item][1+stack*4].isspace():
            break
        else:
            myShip[stack].append(lines[item][1+stack*4])

# for line in lines[track+1::]:
#   instuc = [int(s) for s in re.findall(r'\b\d+\b', line)]
#   for move in range(instuc[0]):
#     item = myShip[instuc[1]-1].pop()
#     myShip[instuc[2]-1].append(item)

# top = []
# for stack in range(len(valList)):
#   top.append(myShip[stack][-1])

for line in lines[track+1::]:
    instuc = [int(s) for s in re.findall(r'\b\d+\b', line)]
    item = []
    for move in range(instuc[0]):
        item.append(myShip[instuc[1]-1].pop())
    item.reverse()
    for i in item:
        myShip[instuc[2]-1].append(i)

top = []
for stack in range(len(valList)):
    top.append(myShip[stack][-1])

print(''.join(top))
