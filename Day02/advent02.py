with open('input.txt') as f:
    lines = f.readlines()

combat = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0,
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6,
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3,
    }
}

shape = {
    "X": 1,
    "Y": 2,
    "Z": 3,

}

toPlay = {
    "A": {
        "X": "Z",
        "Y": "X",
        "Z": "Y",
    },
    "B": {
        "X": "X",
        "Y": "Y",
        "Z": "Z",
    },
    "C": {
        "X": "Y",
        "Y": "Z",
        "Z": "X",
    }
}

total = 0
total2 = 0
for line in lines:
    total += combat[line[0]][line[2]] + shape[line[2]]
    total2 += combat["B"][line[2]] + shape[toPlay[line[0]][line[2]]]

print(total)
print(total2)
