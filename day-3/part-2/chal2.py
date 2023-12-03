import re

"""
example:

123.........14..
..*........*$*..
...32......*1...
..1*4..3%.4....4

"""

filepath = 'example.txt'
lines = list()

with open(filepath, 'r') as f:
    for line in f:
        line = line.splitlines()[0]
        l = [char for char in line]
        lines.append(l)
        
        
lines2 = [line[:] for line in lines]
index = -1
lastWasNumeric = False

for line in lines2:
    for i, char in enumerate(line):
        if not str(char).isnumeric():
            lastWasNumeric = False
            continue
            
        if str(char).isnumeric() and lastWasNumeric:
            line[i] = str(index)
            continue
            
        if str(char).isnumeric() and not lastWasNumeric:
            lastWasNumeric = True;
            index += 1
            line[i] = str(index)
            

with open(filepath, 'r') as f:
    file = f.read()
    numbers = re.findall('\d+', file)
    
    
possibleGears = list()

for i, line in enumerate(lines2):
    maxRange = range(0,len(line))
    for j, char in enumerate(line):
        if(char == '*'):
            possiblePositions = list()
            possiblePositions.extend([(i-1+n//3, j-1+n%3) for n in range(9)])
            # Possible gears
            possibleGears.append(possiblePositions)

for gear in possibleGears:
    for position in gear.copy():
        i, j = position
        if (i not in range(len(lines2)) or j not in maxRange or not lines2[i][j].isnumeric()):
            gear.remove(position)


for c, gear in enumerate(possibleGears):
    for v, position in enumerate(gear.copy()):
        i, j = position
        gear[v] = lines2[i][j]
    
    possibleGears[c] = set(gear)
            

for gear in possibleGears.copy():
    if len(gear) != 2:
        possibleGears.remove(gear)
        

sumOfGears = 0

for gear in possibleGears:
    engineSchematics = list()
    engineSchematics = [int(numbers[int(n)]) for n in gear]
    sumOfGears += engineSchematics[0]*engineSchematics[1]

print(sumOfGears)