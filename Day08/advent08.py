with open('input.txt') as f:
    lines = f.readlines()

def accending(house, trees = [], reverse = 0):
    ans = 1
    if len(trees) == 1:
        return ans
    if reverse:
        trees.reverse()
    for idx, tree in enumerate(trees):
        if idx == 0:
            if tree >= house:
                return ans
        else:
            if tree >= house:
                return ans + 1
            else:
                ans += 1
    return ans

trees = []
for line in lines:
    trees.append([int(x) for x in line.strip()])

visMap = []

for row in range(1, len(trees)-1, 1):
    colMap = []

    for col in range(1, len(trees[:][0]) - 1, 1):
        treeCol = [x[col] for x in trees]
        tree = trees[row][col]
        if tree > max(trees[row][0:col]):
            colMap.append(1)
        elif tree > max(trees[row][col+1::]):
            colMap.append(1)
        elif tree > max(treeCol[0:row]):
            colMap.append(1)
        elif tree > max(treeCol[row+1::]):
            colMap.append(1)
        else:
            colMap.append(0)
    visMap.append(colMap)

total = 0
for x in visMap:
    total += sum(x)

tops = 2 * len(trees[:][0]) 
edge = 2 * len(trees[0][:])

print(total + edge + tops - 4)

scenMap = []
for row in range(1, len(trees)-1, 1):
    colMap = []

    for col in range(1, len(trees[:][0]) - 1, 1):
        # print(row, col, trees[row][0:col])
        tree = trees[row][col]
        treeCol = [x[col] for x in trees]
        ans = 0
        ans += accending(tree, trees[row][0:col], 1)
        ans *= accending(tree, trees[row][col+1::], 0)
        ans *= accending(tree, treeCol[0:row], 1)
        ans *= accending(tree, treeCol[row+1::], 0)
        colMap.append(ans)

    scenMap.append(colMap)

print(max([max(x) for x in scenMap]))