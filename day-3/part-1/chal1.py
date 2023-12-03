import re

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
    print(numbers)

    
found = set()
possiblePositions = set()

for i, line in enumerate(lines2):
    maxRange = range(0,len(line))
    for j, char in enumerate(line):
        if(not char.isnumeric() and char != '.'):
            possiblePositions.update([(i-1+n//3, j-1+n%3) for n in range(9)])
            
for position in possiblePositions:
    i, j = position
    if (i in maxRange and j in maxRange and lines2[i][j].isnumeric()):
        #print(i,j,position, lines[i][j], lines2[i][j])
        found.add(lines2[i][j])
        engineSchematics = [int(numbers[int(n)]) for n in found]

print(sum(engineSchematics))
    