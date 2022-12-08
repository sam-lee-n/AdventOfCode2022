with open('input.txt') as f:
    lines = f.readlines()

folder = {}
location = "/"

for line in lines[1:]:
    instuc = line.strip().split(' ')
    if instuc[1] == 'cd':
        if instuc[2] == '..':
            subSum = folder[location]
            temp = location.split('/')[0:-1]
            if len(temp) > 1:
                location = '/'.join(temp)
            else:
                location = '/'
            if location in folder:
                folder[location] += subSum
            else:
                folder[location] = subSum
        else:
            if not location.endswith('/'):
                location += "/" + instuc[2]
            else:
                location += instuc[2]
    elif instuc[0].isdigit():
        if location in folder:
            folder[location] += int(instuc[0])
        else:
            folder[location] = int(instuc[0])

while (location != '/'):
    subSum = folder[location]
    temp = location.split('/')[0:-1]
    if len(temp) > 1:
        location = '/'.join(temp)
    else:
        location = '/'
    # print(location)
    if location in folder:
        folder[location] += subSum
    else:
        folder[location] = subSum

# for key, value in folder.items():
#     print(key, ' : ', value)

print('Part 1' , sum(v for v in folder.values() if v <= 100000))

spacefree = 70000000 - folder['/']
needSpace = 30000000 - spacefree
print('Part 1' , min(v for v in folder.values() if v >= needSpace))
