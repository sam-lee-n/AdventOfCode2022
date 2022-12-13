with open('input.txt') as f:
    lines = f.readlines()


def tooFar(headLoc, tailLoc):
    dis = (headLoc[0]-tailLoc[0])**2 + (headLoc[1]-tailLoc[1])**2
    if dis > 2:
        return True
    return False


dirLut = {
    'U': [0,   1],
    'D': [0,  -1],
    'L': [-1,  0],
    'R': [1,  0]
}

headLoc = [0, 0]
tailLoc = [0, 0]
history = [[0, 0]]

for line in lines:
    dir, steps = line.split()
    lastHead = headLoc

    for _ in range(int(steps)):
        lastHead = headLoc
        headLoc = [sum(x) for x in zip(headLoc, dirLut[dir])]

        if tooFar(headLoc, tailLoc):
            tailLoc = lastHead
        # print(dir, steps, headLoc, tailLoc)
        history.append(tailLoc)

# Part 1
print(len(set(tuple(row) for row in history)))
