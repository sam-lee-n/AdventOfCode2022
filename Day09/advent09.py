import math
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

def cmp(a, b):
    return (a > b) - (a < b)


# headLoc = [0, 0]
# tailLoc = [0, 0]
# history = [[0, 0]]

# for line in lines:
#     dir, steps = line.split()
#     lastHead = headLoc

#     for _ in range(int(steps)):
#         lastHead = headLoc
#         headLoc = [sum(x) for x in zip(headLoc, dirLut[dir])]

#         if tooFar(headLoc, tailLoc):
#             tailLoc = lastHead
#         # print(dir, steps, headLoc, tailLoc)
#         history.append(tailLoc)

# # Part 1
# print(len(set(tuple(row) for row in history)))

ropeLenght = 10
rope = [[0, 0]] * ropeLenght
history1 = [[0, 0]]
history9 = [[0, 0]]

for line in lines:
    dir, steps = line.split()

    for _ in range(int(steps)):
        preRope = rope.copy()
        rope[0] = [sum(x) for x in zip(rope[0], dirLut[dir])]

        for knot in range(1, ropeLenght):
            hx, hy = rope[knot - 1]
            tx, ty = rope[knot]
        
            if abs(hx - tx) >= 2 or abs(hy - ty) >= 2:
                tx += cmp(hx, tx)
                ty += cmp(hy, ty)
                rope[knot] = [tx, ty]

        history1.append(rope[1])
        history9.append(rope[-1])

# Part 2
print(len(set(tuple(row) for row in history1)))
print(len(set(tuple(row) for row in history9)))