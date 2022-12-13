with open('input.txt') as f:
    lines = f.readlines()

cycle = 1
xReg = 1
signal = 0
screen = ''

for line in lines:
    if line.startswith('noop'):
        cycle += 1
    else:
        instuc, value = line.split()
        if (cycle+1-20) % 40 == 0:
            signal += (cycle+1) * xReg
        
        if (cycle+1) % 40 < xReg or (cycle+1) % 40 > xReg + 2:
            ans = '.'
        else:
            ans = '#'  
        screen += ans


        xReg += int(value)
        cycle += 2
    if (cycle-20) % 40 == 0:
        signal += cycle * xReg

    if cycle % 40 < xReg or cycle % 40 > xReg + 2:
        ans = '.'
    else:
        ans = '#'  
    screen += ans

print('Part 1', signal)

for x in range(len(screen)//40):
    print(screen[x*40:x*40+40])


